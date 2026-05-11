"""
PDF Parser - 解析數學試題 PDF（國中會考數學格式）
支援：
  - 圖片擷取並輸出為 JPG
  - 數學公式轉 LaTeX
  - 選擇題 / 題組 / 混合題解析
"""
from __future__ import annotations

import re
import subprocess
import unicodedata
from pathlib import Path
from typing import Optional

try:
    import fitz  # pyMuPDF
    HAS_FITZ = True
except ImportError:
    HAS_FITZ = False


# ============================================================
# LaTeX 數學符號轉換
# ============================================================

MATH_SYMBOL_MAP = {
    '×': chr(92) + 'times ',
    '÷': chr(92) + 'div ',
    '±': chr(92) + 'pm ',
    '∵': chr(92) + 'because ',
    '∴': chr(92) + 'therefore ',
    '∪': chr(92) + 'cup ',
    '∩': chr(92) + 'cap ',
    '⊂': chr(92) + 'subset ',
    '⊃': chr(92) + 'supset ',
    '⊆': chr(92) + 'subseteq ',
    '⊇': chr(92) + 'supseteq ',
    '∈': chr(92) + 'in ',
    '∉': chr(92) + 'notin ',
    '≤': chr(92) + 'leq ',
    '≥': chr(92) + 'geq ',
    '≠': chr(92) + 'neq ',
    '∠': chr(92) + 'angle ',
    '∟': chr(92) + 'rightangle ',
    '△': chr(92) + 'triangle ',
    '○': chr(92) + 'bigcirc ',
    '⊙': chr(92) + 'odot ',
    '≡': chr(92) + 'equiv ',
    '≅': chr(92) + 'cong ',
    '∼': chr(92) + 'sim ',
    '≌': chr(92) + 'cong ',
    '≈': chr(92) + 'approx ',
    '∞': chr(92) + 'infty ',
    'α': chr(92) + 'alpha ',
    'β': chr(92) + 'beta ',
    'γ': chr(92) + 'gamma ',
    'δ': chr(92) + 'delta ',
    'ε': chr(92) + 'epsilon ',
    'ζ': chr(92) + 'zeta ',
    'θ': chr(92) + 'theta ',
    'λ': chr(92) + 'lambda ',
    'μ': chr(92) + 'mu ',
    'π': chr(92) + 'pi ',
    'ρ': chr(92) + 'rho ',
    'σ': chr(92) + 'sigma ',
    'τ': chr(92) + 'tau ',
    'φ': chr(92) + 'phi ',
    'ψ': chr(92) + 'psi ',
    'ω': chr(92) + 'omega ',
    'Δ': chr(92) + 'Delta ',
    'Σ': chr(92) + 'Sigma ',
    'Π': chr(92) + 'Pi ',
    'Ω': chr(92) + 'Omega ',
}


def convert_to_latex(text: str) -> str:
    """將數學表達式轉換為 LaTeX 格式"""
    if not text:
        return text

    # 分數：4/5 -> \frac{4}{5}
    text = re.sub(r'(\d+)\s*/\s*(\d+)', lambda m: chr(92) + 'frac{' + m.group(1) + '}{' + m.group(2) + '}', text)

    # 根號：√10 -> \sqrt{10}
    text = re.sub(r'√\s*(\d+)', lambda m: chr(92) + 'sqrt{' + m.group(1) + '}', text)
    text = re.sub(r'√\s*([a-zA-Z])', lambda m: chr(92) + 'sqrt{' + m.group(1) + '}', text)

    # 全形上標數字
    sup_map = {'²': '^2', '³': '^3', '⁴': '^4',
               '⁵': '^5', '⁶': '^6', '⁷': '^7',
               '⁸': '^8', '⁹': '^9', '⁰': '^0'}
    for ch, repl in sup_map.items():
        text = text.replace(ch, repl)

    # 次方：x^2 -> x^{2}
    text = re.sub(r'(\w)\^(\w)', lambda m: m.group(1) + '^{' + m.group(2) + '}', text)
    text = re.sub(r'\(([^)]+)\)\^(\d)', lambda m: '(' + m.group(1) + ')^{' + m.group(2) + '}', text)

    # 角度
    text = text.replace('°', '^\\circ ')

    # 百分比
    text = text.replace('％', '\\% ')

    # 通用符號替換
    for ch, repl in MATH_SYMBOL_MAP.items():
        text = text.replace(ch, repl)

    # 連字號
    text = text.replace('–', '-')
    text = text.replace('—', '-')

    # 清理多餘空白
    text = re.sub(r'\s+', ' ', text).strip()

    return text


# ============================================================
# 文字正規化
# ============================================================

def normalize_text(text: str) -> str:
    """統一 PDF 擷取後的相容字與空白"""
    normalized = unicodedata.normalize("NFKC", text or "")
    normalized = normalized.replace("　", " ")
    normalized = re.sub(r"\s+", " ", normalized)
    normalized = re.sub(r"(?<=[一-鿿])\s+(?=[一-鿿])", "", normalized)
    normalized = re.sub(r"\s+(?=[，。．！？；：、）】」』》])", "", normalized)
    normalized = re.sub(r"([,;:!?，。．！？；：、)\]）】」』》])\s+(?=[一-鿿A-Z「『（(《])", r"\1", normalized)
    normalized = re.sub(r"(?<=[一-鿿])\s+(?=[「『（《])", "", normalized)
    return normalized.strip()


def normalize_csv_punctuation(text: str) -> str:
    """統一 CSV 欄位標點，避免與分隔符衝突"""
    return text.replace(",", "，").replace("(", "（").replace(")", "）")


# ============================================================
# PDF 文字提取
# ============================================================

def extract_text_from_pdf(pdf_path: str | Path) -> str:
    """從 PDF 提取文字（layout 模式）"""
    result = subprocess.run(
        ['pdftotext', '-layout', str(pdf_path), '-'],
        capture_output=True, text=True,
    )
    return result.stdout


def extract_raw_text_from_pdf(pdf_path: str | Path) -> str:
    """從 PDF 提取文字（raw 模式）"""
    result = subprocess.run(
        ['pdftotext', '-raw', str(pdf_path), '-'],
        capture_output=True, text=True,
    )
    return result.stdout


# ============================================================
# 圖片擷取
# ============================================================

def extract_images_from_pdf(
    pdf_path: str | Path,
    output_dir: str | Path,
    dpi: int = 200,
) -> dict[int, str]:
    """逐頁渲染為 JPG，回傳 {頁碼: 檔名}"""
    if not HAS_FITZ:
        print("警告: 未安裝 pyMuPDF，跳過圖片擷取")
        return {}

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(pdf_path))
    image_map = {}

    for page_num in range(len(doc)):
        page = doc[page_num]
        zoom = dpi / 72
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        jpg_filename = f"page-{page_num + 1:02d}.jpg"
        pix.save(str(output_dir / jpg_filename))
        image_map[page_num + 1] = jpg_filename

    doc.close()
    return image_map


def extract_region_images(
    pdf_path: str | Path,
    output_dir: str | Path,
    regions: list[dict],
    dpi: int = 250,
) -> list[str]:
    """從 PDF 特定區域裁剪圖片"""
    if not HAS_FITZ:
        print("警告: 未安裝 pyMuPDF，跳過區域圖片擷取")
        return []

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(pdf_path))
    saved = []

    for region in regions:
        page_num = region["page"] - 1
        rect = fitz.Rect(
            region["left"], region["top"],
            region["right"], region["bottom"],
        )
        zoom = dpi / 72
        mat = fitz.Matrix(zoom, zoom)
        pix = doc[page_num].get_pixmap(matrix=mat, clip=rect)
        jpg_filename = region["filename"]
        pix.save(str(output_dir / jpg_filename))
        saved.append(jpg_filename)

    doc.close()
    return saved


# ============================================================
# 題目解析
# ============================================================

def _detect_math_symbols(text: str) -> bool:
    """偵測是否含數學符號"""
    math_chars = r'[√²³⁴⁵⁶⁷⁸⁹⁰∠°≤≥≠×÷±αβγθπ∑∏∫∞]'
    fraction = r'\d+\s*/\s*\d+'
    return bool(re.search(math_chars, text) or re.search(fraction, text))


def detect_question_types(text: str) -> tuple[bool, bool]:
    """偵測試卷是否含圖形與數學公式"""
    has_math = _detect_math_symbols(text)
    has_graphics = bool(re.search(
        r'如圖|數線|坐標|圖形|三角形|圓|圓心|半徑|周長|面積', text
    ))
    return has_graphics, has_math


def categorize_question(has_text: bool, has_graphics: bool, has_formula: bool) -> str:
    """根據內容決定 category 欄位"""
    if has_graphics and has_formula:
        return "文字+圖片+公式"
    if has_graphics:
        return "文字+圖片"
    if has_formula:
        return "文字+公式"
    return "純文字"


def parse_choice_questions(text: str, subject: str = "數學", year: str = "114") -> list[dict]:
    """解析數學選擇題（含題組）"""
    questions = []

    # 全形數字轉半形
    text = text.replace('１', '1').replace('２', '2').replace('３', '3')
    text = text.replace('４', '4').replace('５', '5')
    text = text.replace('６', '6').replace('７', '7').replace('８', '8')
    text = text.replace('９', '9').replace('０', '0')

    lines = text.split('\n')

    # 找到選擇題起始
    start_idx = 0
    for i, line in enumerate(lines):
        if '選擇題' in line or ('一、' in line and '選擇' in line):
            start_idx = i
            break

    # 找到第二部分起始
    end_idx = len(lines)
    for i in range(start_idx, len(lines)):
        if '二、' in lines[i]:
            end_idx = i
            break

    content = '\n'.join(lines[start_idx:end_idx])

    # 分割題目
    question_pattern = r'(?:^|\n)\s*(\d+)[\.．]\s*'
    matches = list(re.finditer(question_pattern, content, re.MULTILINE))

    # 偵測題組
    group_ranges = _detect_groups(content, matches)

    for i, match in enumerate(matches):
        number = int(match.group(1))
        start_pos = match.start()
        end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        question_block = content[start_pos:end_pos]

        # 若是題組成員，加入前言
        prefix = ""
        for gs, ge, gp in group_ranges:
            if number >= gs and number <= ge and number > gs:
                prefix = gp
                break

        q_data = _parse_single_math_question(number, question_block, prefix)
        if q_data:
            questions.append(q_data)

    return questions


def _detect_groups(content: str, matches: list) -> list[tuple]:
    """偵測題組（如「25-26 為題組」）"""
    groups = []
    group_pattern = r'(\d+)\s*-\s*(\d+)\s*為題組'
    group_matches = list(re.finditer(group_pattern, content))

    for gm in group_matches:
        gs = int(gm.group(1))
        ge = int(gm.group(2))
        prefix_text = content[gm.end():gm.end() + 300]
        prefix_lines = []
        for pl in prefix_text.split('\n'):
            pl = pl.strip()
            if pl and not re.match(r'^\d+[\.．]', pl):
                prefix_lines.append(pl)
            else:
                break
        groups.append((gs, ge, ' '.join(prefix_lines)))

    return groups


def _parse_single_math_question(number: int, block: str, prefix: str = "") -> Optional[dict]:
    """解析單一數學選擇題"""
    lines = [line.strip() for line in block.split('\n') if line.strip()]
    if not lines:
        return None

    first_line = lines[0]
    stem_match = re.match(r'\d+[\.．]\s*(.*)', first_line)
    if not stem_match:
        return None

    question_stem = stem_match.group(1)
    if prefix:
        question_stem = prefix + "\n" + question_stem

    remaining_text = '\n'.join(lines[1:])
    full_text = question_stem + '\n' + remaining_text

    # 找選項標記
    option_positions = []
    for letter in ['A', 'B', 'C', 'D']:
        for m in re.finditer(r'[\(（]' + letter + r'[\)）]', full_text):
            option_positions.append((m.start(), letter, m.end()))

    if len(option_positions) < 2:
        return None

    option_positions.sort()

    # 題幹
    question_stem = full_text[:option_positions[0][0]].strip()

    # 選項
    options = {'A': '', 'B': '', 'C': '', 'D': ''}
    for i, (pos, letter, end_pos) in enumerate(option_positions):
        if i + 1 < len(option_positions):
            next_pos = option_positions[i + 1][0]
            opt_text = full_text[end_pos:next_pos].strip()
        else:
            opt_text = full_text[end_pos:].strip()
        opt_text = re.sub(r'\s*【.*?】', '', opt_text)
        opt_text = re.sub(r'\s*\(\d+\)\s*$', '', opt_text)
        options[letter] = opt_text

    if sum(1 for v in options.values() if v) < 2:
        return None

    return {
        'number': number,
        'question_stem': question_stem,
        'option_a': options['A'],
        'option_b': options['B'],
        'option_c': options['C'],
        'option_d': options['D'],
        'question_type': '單選題',
    }


def parse_mixed_questions(text: str, subject: str = "數學", year: str = "114") -> list[dict]:
    """解析混合題（非典型四選項格式）"""
    questions = []

    text = text.replace('１', '1').replace('２', '2').replace('３', '3')
    text = text.replace('４', '4').replace('５', '5')
    text = text.replace('６', '6').replace('７', '7').replace('８', '8')
    text = text.replace('９', '9').replace('０', '0')

    lines = text.split('\n')

    mixed_start = -1
    for i, line in enumerate(lines):
        if '二、' in line and ('混合題' in line or '非選擇題' in line):
            mixed_start = i
            break

    if mixed_start < 0:
        return questions

    content = '\n'.join(lines[mixed_start:])

    question_pattern = r'(?:^|\n)\s*(\d+)[\.．]\s*'
    matches = list(re.finditer(question_pattern, content, re.MULTILINE))

    for i, match in enumerate(matches):
        number = int(match.group(1))
        start_pos = match.start()
        end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        block = content[start_pos:end_pos]
        q_data = _parse_single_mixed_question(number, block)
        if q_data:
            questions.append(q_data)

    return questions


def _parse_single_mixed_question(number: int, block: str) -> Optional[dict]:
    """解析單一混合題"""
    lines = [line.strip() for line in block.split('\n') if line.strip()]
    if not lines:
        return None

    first_line = lines[0]
    stem_match = re.match(r'\d+[\.．]\s*(.*)', first_line)
    if not stem_match:
        return None

    question_stem = stem_match.group(1)
    remaining_text = '\n'.join(lines[1:])

    option_pattern = r'\(([A-Z0-9])\)\s*([^\n]*)'
    option_matches = list(re.finditer(option_pattern, remaining_text))

    options = {'A': '', 'B': '', 'C': '', 'D': ''}

    if option_matches:
        for om in option_matches:
            letter = om.group(1)
            if letter in options:
                options[letter] = om.group(2).strip()
        valid = sum(1 for v in options.values() if v)
        if valid >= 2:
            question_stem += '\n' + remaining_text[:option_matches[0].start()].strip()
        else:
            question_stem += '\n' + remaining_text
    else:
        question_stem += '\n' + remaining_text

    return {
        'number': number,
        'question_stem': question_stem,
        'option_a': options['A'],
        'option_b': options['B'],
        'option_c': options['C'],
        'option_d': options['D'],
        'question_type': '混合題',
    }


# ============================================================
# 主流程
# ============================================================

def process_math_pdf(
    pdf_path: str | Path,
    output_csv: str | Path,
    image_dir: str | Path | None = None,
    subject: str = "數學",
    year: str = "114",
    answers: dict[int, str] | None = None,
) -> list[dict]:
    """
    完整處理數學試題 PDF
    回傳標準格式的题目列表（dict）
    """
    pdf_path = Path(pdf_path)
    output_csv = Path(output_csv)

    COLUMNS = [
        "subject_category", "year", "number",
        "level_1", "level_2", "level_3",
        "question_stem", "option_a", "option_b", "option_c", "option_d",
        "answer", "explanation",
        "explanation_a", "explanation_b", "explanation_c", "explanation_d",
        "difficulty", "question_type", "category",
    ]

    # 提取文字
    print(f"提取文字: {pdf_path}")
    text = extract_text_from_pdf(pdf_path)

    # 解析題目
    choice_questions = parse_choice_questions(text, subject, year)
    mixed_questions = parse_mixed_questions(text, subject, year)
    all_questions = choice_questions + mixed_questions

    if len(all_questions) < 20:
        raw_text = extract_raw_text_from_pdf(pdf_path)
        choice_questions = parse_choice_questions(raw_text, subject, year)
        mixed_questions = parse_mixed_questions(raw_text, subject, year)
        all_questions = choice_questions + mixed_questions

    print(f"解析到 {len(all_questions)} 題")

    # 圖片擷取
    image_filenames = {}
    if image_dir:
        image_dir = Path(image_dir)
        image_dir.mkdir(parents=True, exist_ok=True)
        page_images = extract_images_from_pdf(pdf_path, image_dir, dpi=200)
        for q in all_questions:
            num = q['number']
            page_num = _question_to_page(num)
            if page_num in page_images:
                src = image_dir / page_images[page_num]
                dst_name = f"{year}-{subject}-Q{num:02d}.jpg"
                dst = image_dir / dst_name
                if src.exists():
                    src.rename(dst)
                    image_filenames[num] = dst_name

    # 建立 CSV rows
    rows = []
    for q in all_questions:
        num = q['number']
        stem = q['question_stem']
        opts = [q.get(f'option_{o}', '') for o in ['a', 'b', 'c', 'd']]
        all_content = stem + ' ' + ' '.join(opts)

        q_has_graphics = bool(re.search(
            r'如圖|所示|數線|坐標|圖形|三角形|圓|圓心|半徑', all_content
        ))
        q_has_formula = _detect_math_symbols(all_content)
        category = categorize_question(True, q_has_graphics, q_has_formula)

        # LaTeX 轉換
        q['question_stem'] = normalize_csv_punctuation(
            normalize_text(convert_to_latex(stem))
        )
        for ok in ['option_a', 'option_b', 'option_c', 'option_d']:
            q[ok] = normalize_csv_punctuation(
                normalize_text(convert_to_latex(q.get(ok, '')))
            )

        answer = answers[num] if answers and num in answers else ""

        row = {
            "subject_category": subject,
            "year": year,
            "number": num,
            "level_1": "",
            "level_2": "",
            "level_3": "",
            "question_stem": q['question_stem'],
            "option_a": q['option_a'],
            "option_b": q['option_b'],
            "option_c": q['option_c'],
            "option_d": q['option_d'],
            "answer": answer,
            "explanation": "",
            "explanation_a": "",
            "explanation_b": "",
            "explanation_c": "",
            "explanation_d": "",
            "difficulty": "",
            "question_type": q.get('question_type', '單選題'),
            "category": category,
        }

        if num in image_filenames:
            img_ref = f"\n[IMAGE:{image_filenames[num]}]"
            row["question_stem"] += normalize_csv_punctuation(img_ref)

        rows.append(row)

    # 輸出 CSV
    import pandas as pd
    df = pd.DataFrame(rows, columns=COLUMNS)
    df = df.sort_values("number").reset_index(drop=True)
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_csv, index=False, encoding='utf-8-sig')

    print(f"已輸出 {len(df)} 題到 {output_csv}")
    print(f"  單選題: {len([r for r in rows if r['question_type'] == '單選題'])}")
    print(f"  混合題: {len([r for r in rows if r['question_type'] == '混合題'])}")
    print(f"  含圖題: {len([r for r in rows if '圖片' in r['category']])}")
    print(f"  含公式題: {len([r for r in rows if '公式' in r['category']])}")

    return rows


def _question_to_page(question_num: int) -> int:
    """根據題號推算頁碼"""
    if question_num <= 0:
        return 1
    if question_num <= 28:
        return min(2 + (question_num - 1) // 6, 7)
    return 8 + (question_num - 29) // 4


if __name__ == "__main__":
    import sys
    pdf_path = "input/114會考數學.pdf"
    output_csv = "output/114數學.csv"
    image_dir = "output/images"

    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    if len(sys.argv) > 2:
        output_csv = sys.argv[2]

    Path("output").mkdir(exist_ok=True)
    Path(image_dir).mkdir(parents=True, exist_ok=True)

    process_math_pdf(pdf_path, output_csv, image_dir, year="114")
