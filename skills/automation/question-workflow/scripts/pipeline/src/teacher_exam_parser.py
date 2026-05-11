"""
教師檢定 PDF 解析器 - 提取選擇題內容（改進版）
"""
import re
import subprocess
from typing import List, Optional, Dict, Tuple
from pathlib import Path
import pandas as pd

# 科目對應檔案名稱映射
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
        ('113', 'input/113_中等學校_學習者發展與適性輔導.pdf'),
        ('114', 'input/114_中等學校類科_學習者發展與適性輔導.pdf'),
    ],
}


def extract_text_from_pdf(pdf_path: str) -> str:
    """從 PDF 提取文字"""
    result = subprocess.run(
        ['pdftotext', '-layout', pdf_path, '-'],
        capture_output=True,
        text=True
    )
    return result.stdout


def parse_choice_questions(text: str, subject: str, year: str) -> List[Dict]:
    """
    解析選擇題，包括單獨選擇題和題組中的選擇題
    """
    questions = []

    # 轉換全形數字為半形
    text = text.replace('１', '1').replace('２', '2').replace('３', '3').replace('４', '4').replace('５', '5')
    text = text.replace('６', '6').replace('７', '7').replace('８', '8').replace('９', '9').replace('０', '0')

    # 找到選擇題區域
    lines = text.split('\n')

    # 找到 "第壹部分" 的位置
    start_idx = 0
    for i, line in enumerate(lines):
        if '第壹部分' in line and '選擇題' in line:
            start_idx = i
            break

    # 提取選擇題區域到 "第貳部分" 或 "第參部分" 或結束
    end_idx = len(lines)
    for i in range(start_idx, len(lines)):
        if '第貳部分' in lines[i] or '第贰部分' in lines[i] or '第參部分' in lines[i]:
            end_idx = i
            break

    content = '\n'.join(lines[start_idx:end_idx])

    # 匹配題目模式：數字. 或 數字． 開頭
    question_pattern = r'(?:^|\n)\s*(\d+)[\.．]\s*'
    matches = list(re.finditer(question_pattern, content, re.MULTILINE))

    for i, match in enumerate(matches):
        number = int(match.group(1))
        start_pos = match.start()

        if i + 1 < len(matches):
            end_pos = matches[i + 1].start()
        else:
            end_pos = len(content)

        question_block = content[start_pos:end_pos]
        q_data = parse_single_choice_question(number, question_block)
        if q_data:
            questions.append(q_data)

    return questions


def parse_single_choice_question(number: int, block: str) -> Optional[Dict]:
    """解析單一選擇題"""
    lines = block.split('\n')

    # 去除空行
    lines = [line.strip() for line in lines if line.strip()]

    if not lines:
        return None

    # 第一行包含題號
    first_line = lines[0]

    # 移除題號部分
    stem_match = re.match(r'\d+[\.．]\s*(.*)', first_line)
    if not stem_match:
        return None

    question_stem = stem_match.group(1)

    # 初始化選項
    options = {'A': '', 'B': '', 'C': '', 'D': ''}

    # 收集所有後續行
    remaining_text = ' '.join(lines[1:])

    # 檢查是否有選項標記 (A) (B) (C) (D)
    has_options = False
    for letter in ['A', 'B', 'C', 'D']:
        if f'({letter})' in remaining_text or f'（{letter}）' in remaining_text:
            has_options = True
            break

    if not has_options:
        # 沒有選項，可能是非選擇題
        return None

    # 提取選項 - 改進的解析邏輯
    # 題幹可能在第一行，也可能跨多行
    # 我們需要找到第一個選項的位置

    full_text = question_stem + ' ' + remaining_text

    # 找到所有選項的位置
    option_positions = []
    for letter in ['A', 'B', 'C', 'D']:
        # 匹配 (A) 或 （A）
        pattern = f'[\(（]{letter}[\)）]'
        matches = list(re.finditer(pattern, full_text))
        for match in matches:
            option_positions.append((match.start(), letter, match.end()))

    if len(option_positions) < 2:
        # 選項太少，可能解析錯誤
        return None

    # 按位置排序
    option_positions.sort(key=lambda x: x[0])

    # 提取題幹（第一個選項之前的內容）
    first_opt_pos = option_positions[0][0]
    question_stem = full_text[:first_opt_pos].strip()

    # 提取各選項
    for i, (pos, letter, end_pos) in enumerate(option_positions):
        if i + 1 < len(option_positions):
            next_pos = option_positions[i + 1][0]
            opt_text = full_text[end_pos:next_pos].strip()
        else:
            opt_text = full_text[end_pos:].strip()

        # 清理選項文字
        opt_text = opt_text.strip()
        # 移除可能的題目來源標記，如 "(1)" 或 "【題目來源】"
        opt_text = re.sub(r'\s*【.*?】', '', opt_text)
        opt_text = re.sub(r'\s*\(\d+\)\s*$', '', opt_text)

        options[letter] = opt_text

    # 檢查是否有有效選項內容
    valid_options = sum(1 for v in options.values() if v)
    if valid_options < 2:
        return None

    return {
        'number': number,
        'question_stem': question_stem,
        'option_a': options['A'],
        'option_b': options['B'],
        'option_c': options['C'],
        'option_d': options['D'],
        'answer': '',
        'explanation': '',
    }


def process_all_pdfs():
    """處理所有 PDF 並返回整理後的資料"""
    all_data = []

    for subject, files in SUBJECT_FILES.items():
        for year, pdf_path in files:
            if not Path(pdf_path).exists():
                print(f"檔案不存在: {pdf_path}")
                continue

            print(f"處理: {subject} {year}年 - {pdf_path}")

            try:
                text = extract_text_from_pdf(pdf_path)
                questions = parse_choice_questions(text, subject, year)

                print(f"  找到 {len(questions)} 題選擇題")

                # 檢查題號是否連續
                numbers = [q['number'] for q in questions]
                expected = set(range(1, 26))
                missing = expected - set(numbers)
                if missing:
                    print(f"  警告: 缺少題號 {sorted(missing)}")

                for q in questions:
                    row = {
                        'subject_category': subject,
                        'year': year,
                        'number': q['number'],
                        'level_1': '',
                        'level_2': '',
                        'level_3': '',
                        'question_stem': q['question_stem'],
                        'option_a': q['option_a'],
                        'option_b': q['option_b'],
                        'option_c': q['option_c'],
                        'option_d': q['option_d'],
                        'answer': q['answer'],
                        'explanation': q['explanation'],
                        'explanation_a': '',
                        'explanation_b': '',
                        'explanation_c': '',
                        'explanation_d': '',
                        'difficulty': '',
                        'question_type': '單選',
                        'category': '純文字',
                    }
                    all_data.append(row)

            except Exception as e:
                print(f"  錯誤: {e}")
                import traceback
                traceback.print_exc()

    return all_data


def export_to_excel(data: List[Dict], output_path: str):
    """匯出到 Excel"""
    if not data:
        print("沒有資料可匯出")
        return

    columns = [
        'subject_category', 'year', 'number', 'level_1', 'level_2', 'level_3',
        'question_stem', 'option_a', 'option_b', 'option_c', 'option_d',
        'answer', 'explanation', 'explanation_a', 'explanation_b', 'explanation_c', 'explanation_d',
        'difficulty', 'question_type', 'category'
    ]

    df = pd.DataFrame(data, columns=columns)
    df = df.sort_values(['subject_category', 'year', 'number'])
    df.to_excel(output_path, index=False, engine='openpyxl')

    print(f"\n已匯出 {len(data)} 題到 {output_path}")

    print("\n各科各年份題數統計:")
    stats = df.groupby(['subject_category', 'year']).size().reset_index(name='題數')
    print(stats.to_string(index=False))

    # 顯示每個科目年份的題號範圍
    print("\n各科目年份題號範圍:")
    for (subject, year), group in df.groupby(['subject_category', 'year']):
        numbers = sorted(group['number'].tolist())
        print(f"{subject} {year}年: {numbers}")

    return df


if __name__ == "__main__":
    data = process_all_pdfs()
    output_path = "教師檢定選擇題彙整.xlsx"
    export_to_excel(data, output_path)
