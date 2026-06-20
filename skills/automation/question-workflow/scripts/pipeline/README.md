# 題目處理管線

此子工具用於自動化處理 Word (`.docx`)、PDF 與 Excel 來源資料，整理成標準題庫 CSV 與圖片資源。支援**教師檢定**與**國中會考數學**兩種格式。

## 專案結構設計

專案採用物件導向與模組化的設計，以 `src/` 為主要核心程式庫，並由 `run.py` 進行自動批次調度。

* `run.py`: 入口程式，自動偵測 `input/` 下的 `.docx`、`.pdf` 與 `.xlsx` 檔案，自動識別檔案類型並分送處理流程。
* `src/main.py`: 定義處理單一文件的完整流程（CLI 介面），支援 `--mode docx` 與 `--mode pdf`。
* `src/docx_parser.py`: 透過 `python-docx` 解析 Word 表格，提取題目、圖片與分類。
* `src/pdf_parser.py`: **數學試題 PDF 解析器**，支援：
  - 圖片擷取（逐頁渲染為 JPG，透過 PyMuPDF）
  - 數學公式轉 LaTeX（分數、根號、指數、角度、希臘字母等）
  - 選擇題 / 題組 / 混合題解析
* `src/excel_handler.py`: 載入知識樹、難度評分，匯出 CSV。
* `src/models.py`: `Question` 資料模型，定義題目完整屬性。
* `src/teacher_exam_parser.py`: 教師檢定專用解析器（保留既有功能）。
* `scripts/convert_math_csv_to_latex_template.py`: 將既有會考數學主檔轉為 `template.csv` schema，並做 LaTeX 友善符號轉換。
* `scripts/render_pdf_pages_to_latex_assets.py`: 將每年度數學 PDF 逐頁渲染為 `output/latex/assets/{year}/page-XX.png`。
* `scripts/extract_individual_fig_assets.py`: 從逐頁 PNG 自動裁切 individual figure assets，輸出 `{year}-math-assets/fig-XX.png` 與索引。

## 支援的題目格式

| 格式 | 解析器 | 檔案類型 | 特色 |
|------|--------|----------|------|
| 教師檢定 | `docx_parser` | .docx | 知識樹分類、難度評分 |
| 會考國文/英語 | `docx_parser` | .docx | 同上 |
| 會考數學 | `pdf_parser` | .pdf | 圖片擷取、LaTeX 公式 |

## 輸出資料欄位定義

| 欄位 | 說明 |
|------|------|
| year | 年度（民國年） |
| number | 題號 |
| level_1/2/3 | 知識樹分類 |
| question_stem | 題幹（含 LaTeX 公式） |
| option_a/b/c/d | 選項 |
| answer | 正確答案 |
| explanation | 題目解析 |
| explanation_a/b/c/d | 選項解析 |
| difficulty | 難度 |
| subject_category | 科目/類科 |
| question_type | 題型（單選、混合題等） |
| category | 內容類別（純文字、文字+圖片、文字+公式、文字+圖片+公式） |

## 執行環境與套件需求

```bash
pip install pandas python-docx openpyxl PyMuPDF
```

外部工具（需系統安裝）:
- `pdftotext`: `brew install poppler`（macOS）或 `apt install poppler-utils`（Linux）

## 使用方式

### 方法一：全自動批次處理

```bash
cd skills/automation/question-workflow/scripts/pipeline
python run.py
```

支援 `.docx` 與 `.pdf` 混放在 `input/` 目錄。

### 方法二：處理數學 PDF

```bash
python -m src.main \
  --input input/114年數學試題本.pdf \
  --output output/csv/歷屆試題-數學-114.csv \
  --image-dir output/images \
  --mode pdf \
  --subject 數學 \
  --year 114
```

### 方法三：既有數學主檔轉 LaTeX template CSV

適合已經有 `歷屆試題-Final/歷屆試題-數學.csv`、`template.csv` 與年度 PDF 題本時使用：

```bash
python scripts/convert_math_csv_to_latex_template.py --root /path/to/project
```

輸出：

- `output/csv/all-years-math-latex-template.csv`
- `output/csv/by-year/{year}-math-latex-template.csv`

### 方法四：輸出 LaTeX 圖片資源

先將 PDF 逐頁渲染：

```bash
python scripts/render_pdf_pages_to_latex_assets.py --root /path/to/project --dpi 180
```

再自動裁切題圖候選：

```bash
python scripts/extract_individual_fig_assets.py --root /path/to/project --years 102-114
```

輸出：

- `output/latex/assets/{year}/page-XX.png`
- `output/latex/{year}-math-assets/fig-XX.png`
- `output/latex/assets/index.csv`
- `output/latex/figure-assets-index.csv`

### 方法五：處理 Word 文件

```bash
python -m src.main \
  --input input/114-國文-考題分類.docx \
  --output output/csv/114-國文.csv \
  --image-dir output/images \
  --mode docx \
  --difficulty input/難易度評分.xlsx \
  --knowledge input/知識樹架構.xlsx
```

## 數學 PDF 解析注意事項

1. **LaTeX 公式**: 題幹中的數學符號會自動轉換為 LaTeX 格式（如 `\frac{4}{5}`、`\sqrt{10}`、`30^\circ`）
2. **圖片檔案**: 每個含圖題目的對應頁面會渲染為 JPG，檔名格式為 `{年}-{科目}-Q{題號}.jpg`
3. **題幹中的圖片引用**: 以 `[IMAGE:檔名.jpg]` 註解附加在題幹末尾
4. **Category 欄位**: 根據內容自動判定為「純文字」「文字+圖片」「文字+公式」或「文字+圖片+公式」
5. **混合題**: 第 29-36 題（非典型四選項）的 `question_type` 標為「混合題」

## 注意事項

- `run.py` 以腳本所在目錄為基準，不依賴 shell 工作目錄
- `src/pdf_parser.py` 依賴 `pdftotext`（poppler）與 `PyMuPDF`（fitz）
- 若未安裝 `PyMuPDF`，文字解析仍正常運作，僅跳過圖片擷取
- LaTeX template CSV 與 figure assets 的批次腳本以 `--root` 指向題庫工作區，避免綁死 skill 目錄。
- 自動裁切的 individual figure assets 是候選資源；若要出版級品質，仍需逐張人工抽查。
