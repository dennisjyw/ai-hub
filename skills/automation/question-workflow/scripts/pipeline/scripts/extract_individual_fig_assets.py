#!/usr/bin/env python3
from __future__ import annotations

import csv
import argparse
import re
import shutil
import subprocess
from collections import deque
from pathlib import Path
from xml.etree import ElementTree as ET

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from lxml import etree


ROOT = Path.cwd()
PDF_DIR = ROOT / "歷屆試題-試題本"
PAGE_ASSETS = ROOT / "output" / "latex" / "assets"
OUT_ROOT = ROOT / "output" / "latex"
INDEX_PATH = OUT_ROOT / "figure-assets-index.csv"
SOURCE_CSV = ROOT / "歷屆試題-Final" / "歷屆試題-數學.csv"

PDFINFO = Path("/Users/denniswang/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/pdfinfo")
PDFTOTEXT = Path("/opt/homebrew/bin/pdftotext")


def pdf_page_size(pdf_path: Path) -> tuple[float, float]:
    output = subprocess.check_output([str(PDFINFO), str(pdf_path)], text=True)
    for line in output.splitlines():
        if line.startswith("Page size:"):
            match = re.search(r"Page size:\s+([0-9.]+)\s+x\s+([0-9.]+)", line)
            if match:
                return float(match.group(1)), float(match.group(2))
    raise RuntimeError(f"Could not read page size from {pdf_path}")


def pdftotext_bbox_xml(pdf_path: Path) -> ET.Element:
    output = subprocess.check_output(
        [str(PDFTOTEXT), "-bbox", str(pdf_path), "-"],
        text=True,
        stderr=subprocess.DEVNULL,
    )
    parser = etree.XMLParser(recover=True)
    return etree.fromstring(output.encode("utf-8", errors="ignore"), parser=parser)


def word_items_by_page(root: ET.Element) -> dict[int, list[dict[str, object]]]:
    pages: dict[int, list[dict[str, object]]] = {}
    ns = {"x": "http://www.w3.org/1999/xhtml"}
    page_elements = root.findall(".//x:page", ns)
    if not page_elements:
        page_elements = root.findall(".//page")
    for idx, page in enumerate(page_elements, start=1):
        items = []
        words = page.findall(".//x:word", ns) or page.findall(".//word")
        for word in words:
            try:
                items.append(
                    {
                        "text": "".join(word.itertext()),
                        "box": (
                            float(word.attrib["xMin"]),
                            float(word.attrib["yMin"]),
                            float(word.attrib["xMax"]),
                            float(word.attrib["yMax"]),
                        ),
                    }
                )
            except KeyError:
                continue
        pages[idx] = items
    return pages


def word_boxes(items: list[dict[str, object]]) -> list[tuple[float, float, float, float]]:
    return [item["box"] for item in items]  # type: ignore[misc]


def question_positions_px(
    items: list[dict[str, object]],
    page_size_pt: tuple[float, float],
    image_size_px: tuple[int, int],
) -> list[tuple[int, int]]:
    page_w, page_h = page_size_pt
    image_w, image_h = image_size_px
    sx = image_w / page_w
    sy = image_h / page_h
    positions: list[tuple[int, int]] = []
    for item in items:
        text = str(item["text"]).strip()
        if not re.fullmatch(r"\d{1,2}\.", text):
            continue
        x0, y0, x1, y1 = item["box"]  # type: ignore[misc]
        if x0 > page_w * 0.24:
            continue
        number = int(text[:-1])
        positions.append((int(y0 * sy), number))
    return sorted(positions)


def load_image_questions() -> dict[str, set[int]]:
    image_questions: dict[str, set[int]] = {}
    with SOURCE_CSV.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            number = row.get("number", "")
            if not number.isdigit():
                continue
            category = row.get("category", "")
            stem = row.get("question_stem", "")
            if "圖片" in category or "圖" in stem:
                image_questions.setdefault(row["year"], set()).add(int(number))
    return image_questions


def infer_question_for_box(box: tuple[int, int, int, int], positions: list[tuple[int, int]]) -> int | None:
    if not positions:
        return None
    center_y = (box[1] + box[3]) // 2
    candidates = [number for y, number in positions if y <= center_y + 80]
    if not candidates:
        return positions[0][1]
    return candidates[-1]


def erase_text_mask(
    mask: Image.Image,
    boxes_pt: list[tuple[float, float, float, float]],
    page_size_pt: tuple[float, float],
    inflate_px: int = 5,
) -> None:
    width_px, height_px = mask.size
    page_w, page_h = page_size_pt
    sx = width_px / page_w
    sy = height_px / page_h
    draw = ImageDraw.Draw(mask)
    for x0, y0, x1, y1 in boxes_pt:
        box = (
            max(0, int(x0 * sx) - inflate_px),
            max(0, int(y0 * sy) - inflate_px),
            min(width_px, int(x1 * sx) + inflate_px),
            min(height_px, int(y1 * sy) + inflate_px),
        )
        draw.rectangle(box, fill=0)


def connected_components(binary: np.ndarray) -> list[tuple[int, int, int, int, int]]:
    height, width = binary.shape
    seen = np.zeros_like(binary, dtype=bool)
    components: list[tuple[int, int, int, int, int]] = []
    ys, xs = np.nonzero(binary)
    for start_y, start_x in zip(ys.tolist(), xs.tolist()):
        if seen[start_y, start_x]:
            continue
        q: deque[tuple[int, int]] = deque([(start_y, start_x)])
        seen[start_y, start_x] = True
        min_x = max_x = start_x
        min_y = max_y = start_y
        count = 0
        while q:
            y, x = q.popleft()
            count += 1
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y
            for ny in (y - 1, y, y + 1):
                if ny < 0 or ny >= height:
                    continue
                for nx in (x - 1, x, x + 1):
                    if nx < 0 or nx >= width or seen[ny, nx] or not binary[ny, nx]:
                        continue
                    seen[ny, nx] = True
                    q.append((ny, nx))
        components.append((min_x, min_y, max_x + 1, max_y + 1, count))
    return components


def expand_box(box: tuple[int, int, int, int], image_size: tuple[int, int], pad: int) -> tuple[int, int, int, int]:
    x0, y0, x1, y1 = box
    width, height = image_size
    return (
        max(0, x0 - pad),
        max(0, y0 - pad),
        min(width, x1 + pad),
        min(height, y1 + pad),
    )


def box_area(box: tuple[int, int, int, int]) -> int:
    x0, y0, x1, y1 = box
    return max(0, x1 - x0) * max(0, y1 - y0)


def boxes_close(a: tuple[int, int, int, int], b: tuple[int, int, int, int], gap: int) -> bool:
    ax0, ay0, ax1, ay1 = a
    bx0, by0, bx1, by1 = b
    return not (
        ax1 + gap < bx0
        or bx1 + gap < ax0
        or ay1 + gap < by0
        or by1 + gap < ay0
    )


def merge_boxes(boxes: list[tuple[int, int, int, int]], gap: int = 45) -> list[tuple[int, int, int, int]]:
    merged = boxes[:]
    changed = True
    while changed:
        changed = False
        next_boxes: list[tuple[int, int, int, int]] = []
        used = [False] * len(merged)
        for i, box in enumerate(merged):
            if used[i]:
                continue
            x0, y0, x1, y1 = box
            used[i] = True
            for j in range(i + 1, len(merged)):
                if used[j] or not boxes_close((x0, y0, x1, y1), merged[j], gap):
                    continue
                bx0, by0, bx1, by1 = merged[j]
                x0, y0, x1, y1 = min(x0, bx0), min(y0, by0), max(x1, bx1), max(y1, by1)
                used[j] = True
                changed = True
            next_boxes.append((x0, y0, x1, y1))
        merged = next_boxes
    return merged


def find_figure_boxes(page_path: Path, boxes_pt: list[tuple[float, float, float, float]], page_size_pt: tuple[float, float]) -> list[tuple[int, int, int, int]]:
    image = Image.open(page_path).convert("L")
    width, height = image.size
    # Dark strokes only. Text is removed using pdftotext word boxes, leaving lines, charts, tables, and diagrams.
    mask = image.point(lambda p: 255 if p < 210 else 0, mode="L")
    erase_text_mask(mask, boxes_pt, page_size_pt)

    # Remove footer page number / navigation box area unless a real figure is very large there.
    draw = ImageDraw.Draw(mask)
    draw.rectangle((0, int(height * 0.91), width, height), fill=0)

    scale = 0.34
    small_size = (max(1, int(width * scale)), max(1, int(height * scale)))
    small_mask = mask.resize(small_size, Image.Resampling.NEAREST)
    grouped = small_mask.filter(ImageFilter.MaxFilter(11))
    binary = np.array(grouped) > 0
    components = connected_components(binary)

    boxes: list[tuple[int, int, int, int]] = []
    for x0, y0, x1, y1, count in components:
        x0 = int(x0 / scale)
        y0 = int(y0 / scale)
        x1 = int(x1 / scale)
        y1 = int(y1 / scale)
        w = x1 - x0
        h = y1 - y0
        area = w * h
        if w < 100 or h < 70:
            continue
        if area < 12_000:
            continue
        if count < 35:
            continue
        if w > width * 0.92 and h > height * 0.75:
            continue
        expanded = expand_box((x0, y0, x1, y1), (width, height), 45)
        residual_pixels = int((np.array(mask.crop(expanded)) > 0).sum())
        if residual_pixels < 900:
            continue
        boxes.append(expanded)

    boxes = merge_boxes(boxes, gap=65)
    filtered: list[tuple[int, int, int, int]] = []
    for box in boxes:
        x0, y0, x1, y1 = box
        w = x1 - x0
        h = y1 - y0
        area = w * h
        if w < 130 or h < 90 or area < 20_000:
            continue
        if y0 < 90 and h < 180:
            continue
        # Drop boxes that are almost the entire page text block.
        if w > width * 0.85 and h > height * 0.65:
            continue
        filtered.append(box)

    return sorted(filtered, key=lambda b: (b[1], b[0]))


def crop_year(year: str, skip_existing: bool = True) -> list[dict[str, str]]:
    out_dir = OUT_ROOT / f"{year}-math-assets"
    if out_dir.exists() and skip_existing:
        return existing_asset_rows(year, out_dir)
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    pdf_path = PDF_DIR / f"{year}-數學-試題本.pdf"
    page_size = pdf_page_size(pdf_path)
    page_items = word_items_by_page(pdftotext_bbox_xml(pdf_path))
    image_questions = load_image_questions().get(year, set())
    fig_counter = 1
    rows: list[dict[str, str]] = []

    page_paths = sorted((PAGE_ASSETS / year).glob("page-*.png"))
    last_page = len(page_paths)
    for page_path in page_paths:
        page = int(page_path.stem.split("-")[1])
        if page == 1 or page == last_page:
            continue
        items = page_items.get(page, [])
        boxes = find_figure_boxes(page_path, word_boxes(items), page_size)
        original = Image.open(page_path).convert("RGB")
        q_positions = question_positions_px(items, page_size, original.size)
        for box in boxes:
            question_number = infer_question_for_box(box, q_positions)
            if question_number is not None and question_number not in image_questions:
                continue
            x0, y0, x1, y1 = box
            crop = original.crop(box)
            name = f"fig-{fig_counter:02d}.png"
            crop.save(out_dir / name, optimize=True)
            rows.append(
                {
                    "year": year,
                    "figure": name,
                    "page": str(page),
                    "asset_path": str((out_dir / name).relative_to(ROOT)),
                    "bbox_px": f"{x0},{y0},{x1},{y1}",
                    "source_page": str(page_path.relative_to(ROOT)),
                    "method": "auto",
                }
            )
            fig_counter += 1
    return rows


def existing_asset_rows(year: str, out_dir: Path) -> list[dict[str, str]]:
    rows = []
    for path in sorted(out_dir.glob("fig-*.png")):
        rows.append(
            {
                "year": year,
                "figure": path.name,
                "page": "",
                "asset_path": str(path.relative_to(ROOT)),
                "bbox_px": "",
                "source_page": "",
                "method": "existing",
            }
        )
    return rows


def main() -> None:
    global ROOT, PDF_DIR, PAGE_ASSETS, OUT_ROOT, INDEX_PATH, SOURCE_CSV

    parser = argparse.ArgumentParser(
        description="Crop individual figure assets from rendered math exam page PNGs."
    )
    parser.add_argument("--root", default=".", help="題庫工作區根目錄，預設為目前工作目錄")
    parser.add_argument("--pdf-dir", default="歷屆試題-試題本", help="PDF 題本資料夾，可相對於 --root")
    parser.add_argument("--page-assets", default="output/latex/assets", help="逐頁 PNG assets 資料夾，可相對於 --root")
    parser.add_argument("--out-root", default="output/latex", help="fig assets 輸出根目錄，可相對於 --root")
    parser.add_argument("--source-csv", default="歷屆試題-Final/歷屆試題-數學.csv", help="既有題庫 CSV，用於判斷圖片題，可相對於 --root")
    parser.add_argument("--years", default="102-114", help="年度範圍，例如 102-114 或 102,103,114")
    parser.add_argument("--overwrite-reviewed", action="store_true", help="若設定，連既有人工校對年度 assets 也覆蓋")
    args = parser.parse_args()

    ROOT = Path(args.root).resolve()
    PDF_DIR = (ROOT / args.pdf_dir).resolve() if not Path(args.pdf_dir).is_absolute() else Path(args.pdf_dir)
    PAGE_ASSETS = (ROOT / args.page_assets).resolve() if not Path(args.page_assets).is_absolute() else Path(args.page_assets)
    OUT_ROOT = (ROOT / args.out_root).resolve() if not Path(args.out_root).is_absolute() else Path(args.out_root)
    INDEX_PATH = OUT_ROOT / "figure-assets-index.csv"
    SOURCE_CSV = (ROOT / args.source_csv).resolve() if not Path(args.source_csv).is_absolute() else Path(args.source_csv)

    all_rows: list[dict[str, str]] = []
    if "-" in args.years:
        start, end = [int(part) for part in args.years.split("-", 1)]
        years = [f"{year}" for year in range(start, end + 1)]
    else:
        years = [part.strip() for part in args.years.split(",") if part.strip()]
    for year in years:
        skip_existing = (not args.overwrite_reviewed) and year == "114" and (OUT_ROOT / f"{year}-math-assets").exists()
        rows = crop_year(year, skip_existing=skip_existing)
        all_rows.extend(rows)
        print(f"{year}: {len(rows)} figures")

    with INDEX_PATH.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["year", "figure", "page", "asset_path", "bbox_px", "source_page", "method"],
        )
        writer.writeheader()
        writer.writerows(all_rows)
    print(f"index={INDEX_PATH.relative_to(ROOT)}")
    print(f"total_figures={len(all_rows)}")


if __name__ == "__main__":
    main()
