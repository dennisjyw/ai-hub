# Math PDF To LaTeX CSV Workflow

Use this reference when converting 國中會考數學 PDF or an existing math-question CSV into LaTeX-friendly CSV that follows a canonical `template.csv`, and when extracting page or figure assets for LaTeX.

## Expected Workspace Shape

```text
project/
├── template.csv
├── 歷屆試題-Final/
│   └── 歷屆試題-數學.csv
├── 歷屆試題-試題本/
│   ├── 102-數學-試題本.pdf
│   └── ...
└── output/
```

The scripts accept `--root <project>` and default to the current working directory.

## Workflow

1. Inspect source inventory before writing:
   - `template.csv` header.
   - source CSV row count by `year`.
   - PDF list and page counts.
2. Normalize CSV into template schema:

```bash
python scripts/pipeline/scripts/convert_math_csv_to_latex_template.py --root /path/to/project
```

Outputs:
   - `output/csv/all-years-math-latex-template.csv`
   - `output/csv/by-year/{year}-math-latex-template.csv`

3. Render PDF pages when figure extraction is needed:

```bash
python scripts/pipeline/scripts/render_pdf_pages_to_latex_assets.py --root /path/to/project --dpi 180
```

Outputs:
   - `output/latex/assets/{year}/page-XX.png`
   - `output/latex/assets/index.csv`

4. Extract individual figure assets:

```bash
python scripts/pipeline/scripts/extract_individual_fig_assets.py --root /path/to/project --years 102-114
```

Outputs:
   - `output/latex/{year}-math-assets/fig-XX.png`
   - `output/latex/figure-assets-index.csv`

By default, existing `114-math-assets` is treated as reviewed/manual and is not overwritten. Use `--overwrite-reviewed` only when intentional.

## CSV Rules

- Treat `template.csv` as canonical header and keep the output header exactly equal.
- Preserve existing `answer`, `difficulty`, `question_type`, `category`, and `level_1/2/3` from the source CSV.
- Use `subject_category=數學` unless a project specifies otherwise.
- Convert common math notation to LaTeX-friendly text:
  - superscripts: `7¹⁰` -> `7^{10}`
  - roots: `√3` -> `\sqrt{3}`
  - fractions: `5/8` -> `\dfrac{5}{8}`
  - symbols: `×`, `÷`, `∠`, `△`, `°`
- Replace half-width commas inside fields with full-width commas. Do not alter CSV delimiters.
- For image questions where option text is missing, fill missing option cells with `[PDF_IMAGE_SOURCE:...]` instead of leaving them blank.

## Asset Extraction Notes

- Page assets are full rendered pages and are useful as a stable source for manual crop work.
- Individual figure assets for older years are automatic candidates. Treat them as useful first-pass crops, not fully reviewed final art.
- The figure extraction script removes text using `pdftotext -bbox`, detects remaining line/table/diagram components, maps candidates to likely question numbers, and keeps only source CSV rows categorized as image-like or containing `圖`.
- Formula strokes such as root bars or fraction bars are filtered by residual stroke count.

## Verification Checklist

After conversion, run checks equivalent to:

- Output header equals `template.csv`.
- `year + number` duplicate count is 0.
- Required fields are not empty:
  - `subject_category`, `year`, `number`, `question_stem`
  - for choice questions: `option_a`～`option_d`, `answer`
- Half-width comma count inside CSV fields is 0.
- Per-year output file count matches expected years.
- Asset index rows match actual files and no crop is tiny or missing.

## Known Limits

- Existing source CSV quality controls text quality. If a historic row already has OCR damage, the script preserves structure but does not reconstruct missing prose from PDF.
- Automatic figure crops may merge adjacent option diagrams or retain small bits of surrounding text. Record this as a review task rather than silently claiming manual quality.
- If `pdftotext`, `pdfinfo`, or `pdftoppm` paths differ, prefer passing explicit paths or editing script constants for the environment.
