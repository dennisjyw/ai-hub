"""
提取教師檢定 PDF 中的答案，並補全到 Excel

此腳本為特定教師檢定資料集的輔助工具，內含硬編碼檔名與輸出路徑。
執行前請先確認 `input/` 中的實際檔案名稱是否一致。
"""
import re
import subprocess
from pathlib import Path
import pandas as pd

# 定義檔案
SUBJECT_FILES = {
    '課程教學與評量': [
        ('110', 'input/110_中等學校_課程教學與評量.pdf'),
        ('112', 'input/112_中等學校_課程教學與評量.pdf'),
        ('113', 'input/113_中等學校_課程教學與評量.pdf'),
        ('114', 'input/114_中等學校_課程教學與評量.pdf'),
    ],
    '教育理念與實務': [
        ('110', 'input/110_中等學校_教育理念與實務.pdf'),
        ('111', 'input/111_中等學校_教育理念與實務.pdf'),
        ('112', 'input/112_中等學校_教育理念與實務.pdf'),
        ('113', 'input/113_中等學校_教育理念與實務.pdf'),
        ('114', 'input/114_中等學校_教育理念與實務.pdf'),
    ],
    '學習者發展與適性輔導': [
        ('110', 'input/110_中等學校_學習者發展與適性輔導.pdf'),
        ('112', 'input/112_中等學校_學習者發展與適性輔導.pdf'),
        ('113', 'input/113_中等學校類科_學習者發展與適性輔導.pdf'),
        ('114', 'input/114_中等學校類科_學習者發展與適性輔導.pdf'),
    ],
}

# 根據「缺少題號統計.md」定義的缺少題號
MISSING_QUESTIONS = {
    '課程教學與評量': {
        110: [4, 5, 6, 7, 8, 9],
        112: [7, 8],
        113: [6, 7],
        114: [4, 5, 6, 7],
    },
    '教育理念與實務': {
        110: [4, 5, 6, 7, 24, 25],
        111: [4, 5, 6, 7, 8, 9],
        112: [4, 5, 6],
        113: [4, 5, 6, 7],
        114: [4, 5, 6],
    },
    '學習者發展與適性輔導': {
        110: [4, 5, 6, 7, 8, 9],
        112: [4, 5, 6, 7, 8],
        113: [4, 5, 6, 7, 8, 25],
        114: [4, 5, 6, 7, 9, 24, 25],
    },
}


def extract_text_from_pdf(pdf_path: str) -> str:
    """從 PDF 提取文字"""
    result = subprocess.run(
        ['pdftotext', '-layout', pdf_path, '-'],
        capture_output=True,
        text=True
    )
    return result.stdout


def extract_answers(text: str) -> dict:
    """
    從 PDF 文字中提取選擇題答案
    返回：{題號: 答案}
    """
    answers = {}

    # 尋找答案區域（通常在文件末尾）
    lines = text.split('\n')
    answer_section_start = -1

    for i, line in enumerate(lines):
        if '選擇題參考答案' in line or '選擇題答案' in line:
            answer_section_start = i
            break

    if answer_section_start == -1:
        return answers

    # 從答案區提取答案
    # 收集答案區域的所有行（擴大到30行以涵蓋所有答案）
    answer_lines = []
    for i in range(answer_section_start, min(answer_section_start + 30, len(lines))):
        line = lines[i]
        # 匹配「答案」開頭的行（包含答案字母）
        if re.match(r'^\s*答案\s+[A-D]', line):
            answer_lines.append(line)

    # 解析答案 - 按行順序提取字母
    all_answers = []
    for line in answer_lines:
        # 提取該行的所有 A-D 字母
        matches = re.findall(r'[A-D]', line)
        all_answers.extend(matches)

    # 分配題號（1-25）
    for i, ans in enumerate(all_answers[:25]):
        answers[i + 1] = ans

    return answers


def process_subject(subject: str, excel_path: str, pdf_files: list):
    """處理單一科目"""
    print(f"\n=== 處理 {subject} ===")

    # 讀取現有 Excel
    df = pd.read_excel(excel_path)
    print(f"  原始筆數: {len(df)}")

    # 修正 subject_category（因為有些檔案的 subject_category 是「中等學校」）
    df['subject_category'] = subject

    # 收集所有答案
    all_answers = {}
    for year, pdf_path in pdf_files:
        if not Path(pdf_path).exists():
            print(f"  警告: {pdf_path} 不存在")
            continue

        text = extract_text_from_pdf(pdf_path)
        answers = extract_answers(text)

        # 存入字典 {(subject, year, number): answer}
        for num, ans in answers.items():
            all_answers[(subject, int(year), num)] = ans

    print(f"  提取到 {len(all_answers)} 個答案")

    # 補全答案欄位
    def fill_answer(row):
        key = (subject, row['year'], row['number'])
        if key in all_answers:
            return all_answers[key]
        return row.get('answer', '')

    df['answer'] = df.apply(fill_answer, axis=1)

    # 統計有答案的題目
    has_answer = df[df['answer'].notna() & (df['answer'] != '')]
    print(f"  有答案的題目: {len(has_answer)} 題")

    # 過濾出缺少的題目
    missing_filter = []
    for _, row in df.iterrows():
        year = row['year']
        num = row['number']

        if subject in MISSING_QUESTIONS:
            if year in MISSING_QUESTIONS[subject]:
                if num in MISSING_QUESTIONS[subject][year]:
                    missing_filter.append(True)
                else:
                    missing_filter.append(False)
            else:
                missing_filter.append(False)
        else:
            missing_filter.append(False)

    df_filtered = df[missing_filter].copy()
    print(f"  過濾後筆數（缺少的題目）: {len(df_filtered)}")

    # 顯示統計
    if len(df_filtered) > 0:
        print("\n  各年份缺少題目統計:")
        stats = df_filtered.groupby('year').size().reset_index(name='題數')
        print(stats.to_string(index=False))

        print("\n  各年份題號:")
        for year, group in df_filtered.groupby('year'):
            numbers = sorted(group['number'].tolist())
            print(f"    {year}年: {numbers}")

    return df_filtered


def main():
    """主函數"""
    subjects = {
        '教育理念與實務': 'input/教育理念與實務.xlsx',
        '課程教學與評量': 'input/課程教學與評量.xlsx',
        '學習者發展與適性輔導': 'input/學習者發展與適性輔導.xlsx',
    }

    for subject, excel_path in subjects.items():
        if subject in SUBJECT_FILES:
            df_filtered = process_subject(subject, excel_path, SUBJECT_FILES[subject])

            # 輸出到 input 目錄
            output_path = f'input/{subject}_缺少題目.xlsx'
            df_filtered.to_excel(output_path, index=False, engine='openpyxl')
            print(f"  已輸出到: {output_path}")


if __name__ == "__main__":
    main()
