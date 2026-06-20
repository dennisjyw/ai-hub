#!/usr/bin/env python3
from __future__ import annotations

import csv
import argparse
import re
from pathlib import Path


ROOT = Path.cwd()
TEMPLATE = ROOT / "template.csv"
SOURCE = ROOT / "歷屆試題-Final" / "歷屆試題-數學.csv"
PDF_DIR = ROOT / "歷屆試題-試題本"
OUT_DIR = ROOT / "output" / "csv"
COMBINED_OUT = OUT_DIR / "all-years-math-latex-template.csv"
PER_YEAR_DIR = OUT_DIR / "by-year"
REVIEWED_114 = OUT_DIR / "114-math-questions-template.csv"


SUPERSCRIPT_MAP = str.maketrans(
    {
        "⁰": "0",
        "¹": "1",
        "²": "2",
        "³": "3",
        "⁴": "4",
        "⁵": "5",
        "⁶": "6",
        "⁷": "7",
        "⁸": "8",
        "⁹": "9",
    }
)

SYMBOL_MAP = {
    "×": r"\times",
    "÷": r"\div",
    "≠": r"\ne",
    "≤": r"\le",
    "≥": r"\ge",
    "＝": "=",
    "−": "-",
    "＋": "+",
    "∠": r"\angle",
    "∆": r"\triangle",
    "△": r"\triangle",
    "π": r"\pi",
    "θ": r"\theta",
    "°": r"^\circ",
    "√": r"\sqrt",
}


def read_header(path: Path) -> list[str]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return next(csv.reader(f))


def normalize_punctuation(text: str) -> str:
    # Keep CSV delimiters outside field values by using full-width punctuation in prose.
    return (
        text.replace(",", "，")
        .replace("(", "（")
        .replace(")", "）")
        .replace("～", "~")
    )


def convert_superscripts(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        base = match.group(1)
        exponent = match.group(2).translate(SUPERSCRIPT_MAP)
        return f"{base}^{{{exponent}}}"

    return re.sub(r"([A-Za-z0-9）\)])([⁰¹²³⁴⁵⁶⁷⁸⁹]+)", repl, text)


def convert_roots(text: str) -> str:
    text = re.sub(r"√\s*([0-9A-Za-z]+)", lambda m: rf"\sqrt{{{m.group(1)}}}", text)
    return text.replace("√", r"\sqrt{}")


def convert_simple_fractions(text: str) -> str:
    return re.sub(
        r"(?<![A-Za-z0-9])(\d+)\s*/\s*(\d+)(?![A-Za-z0-9])",
        lambda m: rf"\dfrac{{{m.group(1)}}}{{{m.group(2)}}}",
        text,
    )


def replace_symbols(text: str) -> str:
    for src, dst in SYMBOL_MAP.items():
        text = text.replace(src, dst)
    return text


def likely_math_only(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if re.search(r"[\u4e00-\u9fff]", stripped):
        return False
    return bool(re.search(r"[\\^_=\+\-\*/<>]|[A-Za-z]\d|\d[A-Za-z]", stripped))


def protect_inline_math(text: str) -> str:
    text = text.strip()
    if not text:
        return text
    if r"\(" in text or r"\[" in text:
        return text
    if likely_math_only(text):
        return rf"\({text}\)"
    return text


def to_latex_cell(value: str) -> str:
    text = (value or "").strip()
    if not text:
        return ""
    text = normalize_punctuation(text)
    text = convert_superscripts(text)
    text = convert_roots(text)
    text = convert_simple_fractions(text)
    text = replace_symbols(text)
    text = re.sub(r"\s+", " ", text).strip()
    return protect_inline_math(text)


def cleanup_reviewed_latex_cell(value: str) -> str:
    text = value or ""
    text = re.sub(r"(?<=[A-Za-z0-9])-?,(?=[A-Za-z0-9-])", lambda m: m.group(0).replace(",", "，"), text)
    text = re.sub(r"(?<=[A-Za-z0-9])-?,(?=\\)", lambda m: m.group(0).replace(",", "，"), text)
    text = text.replace(", leftmargin=2.2em", "; leftmargin=2.2em")
    return text


def numeric_sort_key(row: dict[str, str]) -> tuple[int, int]:
    year = int(row["year"])
    number_text = row["number"]
    number = int(number_text) if number_text.isdigit() else 999
    return year, number


def append_pdf_reference(row: dict[str, str]) -> None:
    category = row.get("category", "")
    if "圖片" not in category and "圖" not in row.get("question_stem", ""):
        return

    year = row["year"]
    pdf_name = f"{year}-數學-試題本.pdf"
    if not (PDF_DIR / pdf_name).exists():
        return

    ref = f"[PDF_IMAGE_SOURCE:歷屆試題-試題本/{pdf_name}]"
    stem = row["question_stem"].strip()
    if ref not in stem:
        row["question_stem"] = f"{stem} {ref}".strip()


def pdf_source_ref(year: str) -> str:
    return f"[PDF_IMAGE_SOURCE:歷屆試題-試題本/{year}-數學-試題本.pdf]"


def build_rows() -> list[dict[str, str]]:
    header = read_header(TEMPLATE)
    with SOURCE.open(newline="", encoding="utf-8-sig") as f:
        source_rows = list(csv.DictReader(f))

    output_rows: list[dict[str, str]] = []
    for src in sorted(source_rows, key=numeric_sort_key):
        row = {field: "" for field in header}
        row.update(
            {
                "subject_category": "數學",
                "year": src.get("year", ""),
                "number": src.get("number", ""),
                "level_1": src.get("level_1", ""),
                "level_2": src.get("level_2", ""),
                "level_3": src.get("level_3", ""),
                "question_stem": to_latex_cell(src.get("question_stem", "")),
                "option_a": to_latex_cell(src.get("option_a", "")),
                "option_b": to_latex_cell(src.get("option_b", "")),
                "option_c": to_latex_cell(src.get("option_c", "")),
                "option_d": to_latex_cell(src.get("option_d", "")),
                "answer": src.get("answer", ""),
                "explanation": to_latex_cell(src.get("explanation", "")),
                "explanation_a": to_latex_cell(src.get("explanation_a", "")),
                "explanation_b": to_latex_cell(src.get("explanation_b", "")),
                "explanation_c": to_latex_cell(src.get("explanation_c", "")),
                "explanation_d": to_latex_cell(src.get("explanation_d", "")),
                "difficulty": src.get("difficulty", ""),
                "question_type": src.get("question_type", ""),
                "category": src.get("category", ""),
            }
        )
        append_pdf_reference(row)
        if row.get("question_type") != "非選題":
            missing_options = [
                field for field in ["option_a", "option_b", "option_c", "option_d"]
                if not row.get(field)
            ]
            if missing_options:
                ref = pdf_source_ref(row["year"])
                for field in missing_options:
                    row[field] = ref
                if ref not in row["question_stem"]:
                    row["question_stem"] = f"{row['question_stem']} {ref}".strip()
        output_rows.append(row)

    if REVIEWED_114.exists():
        with REVIEWED_114.open(newline="", encoding="utf-8-sig") as f:
            reviewed = list(csv.DictReader(f))
        for row in reviewed:
            for field, value in list(row.items()):
                row[field] = cleanup_reviewed_latex_cell(value)
        output_rows = [
            row for row in output_rows
            if row.get("year") != "114"
        ] + reviewed

    return sorted(output_rows, key=numeric_sort_key)


def write_csv(path: Path, rows: list[dict[str, str]], header: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)


def validate(rows: list[dict[str, str]], header: list[str]) -> dict[str, object]:
    keys = [(row["year"], row["number"]) for row in rows]
    duplicates = sorted({key for key in keys if keys.count(key) > 1})
    required_missing = []
    for row in rows:
        for field in ["subject_category", "year", "number", "question_stem"]:
            if not row.get(field):
                required_missing.append((row["year"], row["number"], field))
        if row.get("question_type") != "非選題":
            for field in ["option_a", "option_b", "option_c", "option_d", "answer"]:
                if not row.get(field):
                    required_missing.append((row["year"], row["number"], field))

    by_year: dict[str, int] = {}
    for row in rows:
        by_year[row["year"]] = by_year.get(row["year"], 0) + 1

    return {
        "row_count": len(rows),
        "header": header,
        "duplicates": duplicates,
        "required_missing": required_missing,
        "by_year": by_year,
    }


def main() -> None:
    global ROOT, TEMPLATE, SOURCE, PDF_DIR, OUT_DIR, COMBINED_OUT, PER_YEAR_DIR, REVIEWED_114

    parser = argparse.ArgumentParser(
        description="Normalize math exam CSV rows to template.csv schema with LaTeX-friendly cells."
    )
    parser.add_argument("--root", default=".", help="題庫工作區根目錄，預設為目前工作目錄")
    parser.add_argument("--template", default="template.csv", help="template.csv 路徑，可相對於 --root")
    parser.add_argument("--source", default="歷屆試題-Final/歷屆試題-數學.csv", help="來源主檔 CSV，可相對於 --root")
    parser.add_argument("--pdf-dir", default="歷屆試題-試題本", help="PDF 題本資料夾，可相對於 --root")
    parser.add_argument("--out-dir", default="output/csv", help="輸出資料夾，可相對於 --root")
    parser.add_argument("--reviewed-year-csv", default="output/csv/114-math-questions-template.csv", help="已人工校對年度 CSV；不存在時略過")
    args = parser.parse_args()

    ROOT = Path(args.root).resolve()
    TEMPLATE = (ROOT / args.template).resolve() if not Path(args.template).is_absolute() else Path(args.template)
    SOURCE = (ROOT / args.source).resolve() if not Path(args.source).is_absolute() else Path(args.source)
    PDF_DIR = (ROOT / args.pdf_dir).resolve() if not Path(args.pdf_dir).is_absolute() else Path(args.pdf_dir)
    OUT_DIR = (ROOT / args.out_dir).resolve() if not Path(args.out_dir).is_absolute() else Path(args.out_dir)
    COMBINED_OUT = OUT_DIR / "all-years-math-latex-template.csv"
    PER_YEAR_DIR = OUT_DIR / "by-year"
    REVIEWED_114 = (ROOT / args.reviewed_year_csv).resolve() if not Path(args.reviewed_year_csv).is_absolute() else Path(args.reviewed_year_csv)

    header = read_header(TEMPLATE)
    rows = build_rows()
    write_csv(COMBINED_OUT, rows, header)

    years = sorted({row["year"] for row in rows}, key=int)
    for year in years:
        year_rows = [row for row in rows if row["year"] == year]
        write_csv(PER_YEAR_DIR / f"{year}-math-latex-template.csv", year_rows, header)

    report = validate(rows, header)
    print(f"combined={COMBINED_OUT.relative_to(ROOT)}")
    print(f"per_year_dir={PER_YEAR_DIR.relative_to(ROOT)}")
    print(f"row_count={report['row_count']}")
    print(f"by_year={report['by_year']}")
    print(f"duplicates={report['duplicates']}")
    print(f"required_missing={report['required_missing'][:20]}")
    if report["duplicates"] or report["required_missing"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
