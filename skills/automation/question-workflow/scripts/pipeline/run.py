"""
Run Script - 批次處理入口
自動偵測 input/ 目錄下的所有檔案（.docx、.pdf、.xlsx），進行批次處理
"""
import os
import sys
from pathlib import Path
from typing import List, Tuple, Dict
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.docx_parser import DocxParser
from src.excel_handler import ExcelHandler
from src.models import Question
from src.pdf_parser import process_math_pdf


def find_files(input_dir: str) -> Tuple[List[str], Dict[str, str], str, List[str]]:
    """
    尋找 input 目錄下的所有檔案

    Returns:
        (docx_files, difficulty_files, knowledge_file, pdf_files)
    """
    input_path = Path(input_dir)

    # 尋找所有 docx 檔案
    docx_files = sorted(str(f) for f in input_path.glob("*.docx"))

    # 尋找所有 PDF 檔案
    pdf_files = sorted(str(f) for f in input_path.glob("*.pdf"))

    # 尋找所有難度評分檔案
    difficulty_files = {}
    for file in input_path.glob("*難度*.xlsx"):
        file_path = str(file)
        if "國文" in file_path:
            difficulty_files["國文"] = file_path
        elif "英語" in file_path:
            difficulty_files["英語"] = file_path
        else:
            difficulty_files["default"] = file_path

    # 尋找知識樹架構檔案
    knowledge_file = None
    for file in input_path.glob("*知識樹*.xlsx"):
        knowledge_file = str(file)
        break

    return docx_files, difficulty_files, knowledge_file, pdf_files


def process_single_file(
    docx_path: str,
    difficulty_path: str,
    knowledge_path: str,
    image_dir: str,
) -> List[Question]:
    """
    處理單一 docx 檔案
    """
    print(f"開始處理: {docx_path}")

    parser = DocxParser(docx_path, image_dir)
    questions = parser.parse()
    print(f"解析完成，共找到 {len(questions)} 題")

    handler = ExcelHandler(knowledge_path, difficulty_path)
    questions = handler.enrich_questions(questions)

    return questions


def main():
    """主執行程式"""
    input_dir = BASE_DIR / "input"
    output_dir = BASE_DIR / "output"
    csv_dir = output_dir / "csv"
    image_dir = output_dir / "images"

    output_dir.mkdir(parents=True, exist_ok=True)
    csv_dir.mkdir(parents=True, exist_ok=True)
    image_dir.mkdir(parents=True, exist_ok=True)

    docx_files, difficulty_files, knowledge_file, pdf_files = find_files(str(input_dir))

    print("=" * 60)
    print("批次處理模式")
    print("=" * 60)
    print(f"找到 {len(docx_files)} 個 docx 檔案")
    print(f"找到 {len(pdf_files)} 個 PDF 檔案")
    print(f"難度評分檔案: {difficulty_files}")
    print(f"知識樹架構檔案: {knowledge_file}")
    print(f"輸出目錄: {output_dir}")
    print(f"CSV 目錄: {csv_dir}")
    print(f"圖片目錄: {image_dir}")
    print("=" * 60)

    # 處理 docx 檔案
    questions_by_subject: Dict[str, List[Question]] = defaultdict(list)

    for docx_file in docx_files:
        try:
            current_difficulty = None
            subject_key = None
            if "國文" in docx_file:
                current_difficulty = difficulty_files.get("國文")
                subject_key = "國文"
            elif "英語" in docx_file:
                current_difficulty = difficulty_files.get("英語")
                subject_key = "英語"
            else:
                current_difficulty = difficulty_files.get("default")
                subject_key = "default"

            if current_difficulty is None:
                print(f"警告: 找不到難度評分檔案，跳過 {docx_file}")
                continue

            questions = process_single_file(
                docx_file, current_difficulty,
                knowledge_file if knowledge_file else "", image_dir,
            )

            if subject_key and questions:
                actual_subject = questions[0].subject_category if questions else subject_key
                questions_by_subject[actual_subject].extend(questions)

        except Exception as e:
            print(f"處理 {docx_file} 時發生錯誤: {e}")
            import traceback
            traceback.print_exc()
            continue

    # 匯出 docx 結果
    if questions_by_subject:
        handler = ExcelHandler(knowledge_file if knowledge_file else "", "")

        for subject, questions in questions_by_subject.items():
            if not questions:
                continue

            questions.sort(key=lambda q: (q.year, q.number))
            output_path = os.path.join(str(csv_dir), f"歷屆試題-{subject}.csv")
            handler.export_to_csv(questions, output_path)

    # 處理數學 PDF
    for pdf_file in pdf_files:
        try:
            # 從檔名提取資訊
            filename = Path(pdf_file).stem
            year = "114"
            subject = "數學"

            # 嘗試從檔名提取年份
            import re
            year_match = re.search(r'(\d{3})', filename)
            if year_match:
                year = year_match.group(1)

            # 嘗試從檔名提取科目
            if "數學" in filename or "math" in filename.lower():
                subject = "數學"

            output_csv = str(csv_dir / f"歷屆試題-{subject}-{year}.csv")

            print(f"\n處理數學 PDF: {pdf_file}")
            rows = process_math_pdf(
                pdf_path=pdf_file,
                output_csv=output_csv,
                image_dir=str(image_dir),
                subject=subject,
                year=year,
            )
            print(f"已輸出 {len(rows)} 題")

        except Exception as e:
            print(f"處理 {pdf_file} 時發生錯誤: {e}")
            import traceback
            traceback.print_exc()
            continue

    total = sum(len(q) for q in questions_by_subject.values())
    print("\n" + "=" * 60)
    print("批次處理完成！")
    print(f"docx 共處理 {total} 題")
    if pdf_files:
        print(f"PDF 已另存於 {csv_dir}")
    print("=" * 60)


if __name__ == "__main__":
    main()
