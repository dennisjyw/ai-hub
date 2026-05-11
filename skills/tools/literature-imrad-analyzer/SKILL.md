---
name: literature-imrad-analyzer
description: 學術論文 IMRaD 結構分析。觸發時機：使用者上傳 PDF 論文並要求分析、拆解結構、整理方法或說「幫我讀這篇 paper」。自動拆解 Introduction, Method, Results, Discussion，萃取研究設計、變項、統計、限制。不適用：文獻搜尋、論文撰寫、全文翻譯。
---

# Literature & IMRaD Structure Analyzer

## 核心理念

「IMRaD 結構」是學術思考的基本邏輯：
- **I**ntroduction（引言）
- **M**ethod（方法）
- **R**esults（結果）
- **D**iscussion（討論）

本技能幫助使用者系統化拆解學術論文，內化這種思維方式。

---

## 觸發時機

**使用此技能當：**
1. 使用者上傳 PDF 學術論文，要求分析、拆解、整理結構
2. 使用者說「幫我讀這篇 paper」、「分析 IMRaD」、「整理研究方法」
3. 使用者詢問論文的研究設計、變項、限制

**不要使用此技能當：**
- 使用者只要論文摘要或翻譯
- 使用者要找新文獻（這是文獻搜尋）
- 使用者要寫新論文（這是寫作）

---

## 工作流程

### Step 1: 確認輸入

1. 檢查是否有 PDF 檔案
2. 確認輸出語言（預設繁體中文）

### Step 2: IMRaD 結構拆解

| 部分 | 提取重點 |
|------|---------|
| **Introduction** | 研究問題、文獻缺口、研究目的、假設 |
| **Method** | 研究設計、樣本、變項、測量工具、分析方法 |
| **Results** | 主要發現、統計結果、圖表重點 |
| **Discussion** | 詮釋、研究限制、貢獻、未來方向 |

→ 詳細格式見 `references/output-formats.md`

### Step 3: 整合性摘要

產出一頁速覽表格，包含核心問題、方法、樣本、發現、限制。

### Step 4: 方法論學習重點

針對碩博士生整理可借鑑之處，包含研究設計優點、變項操作化、分析策略、可改進之處。

---

## 輸出規格

| 格式 | 說明 |
|------|------|
| **預設** | Markdown 檔案，檔名 `[標題]_IMRaD_analysis.md` |
| **可選** | Word 檔案（使用 docx skill） |

**存放位置**：`/mnt/user-data/outputs/`

---

## 語言處理規則

- 預設繁體中文輸出
- 專有名詞保留原文附中文翻譯：`自變項(Independent Variable, IV)`
- 統計術語首次出現時中英對照

---

## 技能限制

本技能 **不包含**：
- 文獻搜尋
- 文獻管理
- 論文撰寫
- 深度統計分析
- 全文翻譯

---

## 載入策略

- 主流程與規格看本檔
- 輸出格式範例 → `references/output-formats.md`
- 範例互動 → `references/example-interactions.md`
- 特殊情況處理 → `references/special-cases.md`
- 品質檢查清單 → `references/quality-checklist.md`