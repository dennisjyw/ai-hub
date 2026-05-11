"""
Main Module - 主流程整合
支援：Word (.docx)、PDF（數學試題）
"""
import argparse
from pathlib import Path

from .pdf_parser import process_math_pdf


def process_pipeline(
    docx_path: str,
    difficulty_path: str,
    knowledge_path: str,
    output_path: str,
    image_dir: str,
):
    """
    處理單一 docx 檔案的完整流程（保留既有功能）
    """
    print(f"開始處理: {docx_path}")

    from .docx_parser import DocxParser
    from .excel_handler import ExcelHandler

    # 1. 解析 docx 檔案
    parser = DocxParser(docx_path, image_dir)
    questions = parser.parse()
    print(f"解析完成，共找到 {len(questions)} 題")

    # 2. 載入知識樹和難度評分
    handler = ExcelHandler(knowledge_path, difficulty_path)

    # 3. 豐富題目資料
    questions = handler.enrich_questions(questions)

    # 4. 匯出 CSV
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    handler.export_to_csv(questions, output_path)

    print(f"處理完成！輸出: {output_path}")


def process_math_pipeline(
    pdf_path: str,
    output_path: str,
    image_dir: str,
    subject: str = "數學",
    year: str = "114",
):
    """
    處理數學試題 PDF 的完整流程

    Args:
        pdf_path: 數學試題 PDF 路徑
        output_path: 輸出 CSV 路徑
        image_dir: 圖片輸出目錄
        subject: 科目名稱
        year: 年度
    """
    from .pdf_parser import process_math_pdf

    print(f"開始處理數學 PDF: {pdf_path}")

    process_math_pdf(
        pdf_path=pdf_path,
        output_csv=output_path,
        image_dir=image_dir,
        subject=subject,
        year=year,
    )

    print(f"數學 PDF 處理完成！輸出: {output_path}")


def main():
    """命令列介面"""
    parser = argparse.ArgumentParser(
        description="題目提取整合工具（支援 docx 與數學 PDF）"
    )

    parser.add_argument(
        "--input", required=True,
        help="輸入檔案路徑（.docx 或 .pdf）",
    )
    parser.add_argument(
        "--output", required=True,
        help="輸出 CSV 檔案路徑",
    )
    parser.add_argument(
        "--image-dir", required=True,
        help="圖片輸出目錄",
    )

    # PDF 模式參數
    parser.add_argument(
        "--mode", choices=["docx", "pdf"], default=None,
        help="處理模式（預設依副檔名自動判斷）",
    )
    parser.add_argument(
        "--subject", default="數學",
        help="科目名稱（PDF 模式）",
    )
    parser.add_argument(
        "--year", default="114",
        help="年度（PDF 模式）",
    )

    # DOCX 模式參數（保留既有）
    parser.add_argument(
        "--difficulty",
        help="難度評分 Excel 檔案路徑（DOCX 模式）",
    )
    parser.add_argument(
        "--knowledge",
        help="知識樹架構 Excel 檔案路徑（DOCX 模式）",
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    mode = args.mode or ("pdf" if input_path.suffix == ".pdf" else "docx")

    if mode == "pdf":
        process_math_pipeline(
            pdf_path=str(input_path),
            output_path=args.output,
            image_dir=args.image_dir,
            subject=args.subject,
            year=args.year,
        )
    else:
        if not args.difficulty or not args.knowledge:
            parser.error("DOCX 模式需要提供 --difficulty 和 --knowledge 參數")
        process_pipeline(
            docx_path=str(input_path),
            difficulty_path=args.difficulty,
            knowledge_path=args.knowledge,
            output_path=args.output,
            image_dir=args.image_dir,
        )


if __name__ == "__main__":
    main()
