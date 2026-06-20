#!/usr/bin/env python3
from __future__ import annotations

import csv
import argparse
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path.cwd()
PDF_DIR = ROOT / "歷屆試題-試題本"
OUT_ROOT = ROOT / "output" / "latex" / "assets"
INDEX_PATH = OUT_ROOT / "index.csv"

PDFINFO = Path("/Users/denniswang/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/pdfinfo")
PDFTOPPM = Path("/Users/denniswang/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/pdftoppm")


def get_year(pdf_path: Path) -> str:
    match = re.match(r"(\d{3})-數學-試題本\.pdf$", pdf_path.name)
    if not match:
        raise ValueError(f"Unexpected PDF name: {pdf_path.name}")
    return match.group(1)


def get_page_count(pdf_path: Path) -> int:
    output = subprocess.check_output([str(PDFINFO), str(pdf_path)], text=True)
    for line in output.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise RuntimeError(f"Could not determine page count for {pdf_path}")


def render_pdf(pdf_path: Path, year: str, dpi: int = 180) -> list[dict[str, str]]:
    year_dir = OUT_ROOT / year
    if year_dir.exists():
        shutil.rmtree(year_dir)
    year_dir.mkdir(parents=True, exist_ok=True)

    prefix = year_dir / "page"
    subprocess.run(
        [
            str(PDFTOPPM),
            "-png",
            "-r",
            str(dpi),
            str(pdf_path),
            str(prefix),
        ],
        check=True,
    )

    expected_pages = get_page_count(pdf_path)
    rendered = sorted(year_dir.glob("page-*.png"))
    if len(rendered) != expected_pages:
        raise RuntimeError(
            f"{pdf_path.name}: expected {expected_pages} pages， rendered {len(rendered)}"
        )

    rows: list[dict[str, str]] = []
    for page_path in rendered:
        page_match = re.search(r"page-(\d+)\.png$", page_path.name)
        page_number = int(page_match.group(1)) if page_match else 0
        rows.append(
            {
                "year": year,
                "page": str(page_number),
                "asset_path": str(page_path.relative_to(ROOT)),
                "source_pdf": str(pdf_path.relative_to(ROOT)),
            }
        )
    return rows


def main() -> None:
    global ROOT, PDF_DIR, OUT_ROOT, INDEX_PATH

    parser = argparse.ArgumentParser(
        description="Render each math exam PDF page into output/latex/assets/{year}/page-XX.png."
    )
    parser.add_argument("--root", default=".", help="題庫工作區根目錄，預設為目前工作目錄")
    parser.add_argument("--pdf-dir", default="歷屆試題-試題本", help="PDF 題本資料夾，可相對於 --root")
    parser.add_argument("--out-root", default="output/latex/assets", help="輸出資料夾，可相對於 --root")
    parser.add_argument("--dpi", type=int, default=180, help="渲染解析度")
    args = parser.parse_args()

    ROOT = Path(args.root).resolve()
    PDF_DIR = (ROOT / args.pdf_dir).resolve() if not Path(args.pdf_dir).is_absolute() else Path(args.pdf_dir)
    OUT_ROOT = (ROOT / args.out_root).resolve() if not Path(args.out_root).is_absolute() else Path(args.out_root)
    INDEX_PATH = OUT_ROOT / "index.csv"

    if not PDFINFO.exists():
        raise SystemExit(f"Missing pdfinfo: {PDFINFO}")
    if not PDFTOPPM.exists():
        raise SystemExit(f"Missing pdftoppm: {PDFTOPPM}")

    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    all_rows: list[dict[str, str]] = []
    pdfs = sorted(PDF_DIR.glob("*-數學-試題本.pdf"))
    for pdf_path in pdfs:
        year = get_year(pdf_path)
        rows = render_pdf(pdf_path, year, dpi=args.dpi)
        all_rows.extend(rows)
        print(f"{year}: {len(rows)} pages")

    with INDEX_PATH.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["year", "page", "asset_path", "source_pdf"],
        )
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"index={INDEX_PATH.relative_to(ROOT)}")
    print(f"total_pages={len(all_rows)}")


if __name__ == "__main__":
    main()
