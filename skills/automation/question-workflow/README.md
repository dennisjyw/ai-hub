# 題庫工作流程

此技能將原本分散的三個題庫技能整併為單一入口，方便在同一個工作流中處理：

1. 題目處理至指定欄位
2. 知識樹建立與重整
3. explanation 解析查重分析
4. level & explanation 題目解析撰寫

## 目錄結構

```text
question-workflow/
├── SKILL.md
├── README.md
├── scripts/
│   └── pipeline/              # 題目來源整理與欄位轉換工具
└── references/
    ├── knowledge-tree/        # 知識樹建立、重整與欄位對齊規範
    ├── batch-explanation/     # 批次解析撰寫與 review 節奏
    ├── explanation-review/    # 解析查重改寫與格式規範
    └── analyzer/              # 解析與難度撰寫規範
```

## 功能一：題目處理至指定欄位

- 可將 `.docx` 題本、知識樹 Excel、難度評分 Excel 整理成標準題庫 CSV。
- 保留可重用程式碼於 `scripts/pipeline/`。
- 適用情境：
  - 題目匯入
  - 欄位清洗
  - 圖片抽取
  - 指定欄位輸出

常見輸出欄位：

- `subject_category`
- `year`
- `number`
- `level_1`
- `level_2`
- `level_3`
- `question_stem`
- `option_a`
- `option_b`
- `option_c`
- `option_d`
- `answer`
- `explanation`
- `explanation_a`
- `explanation_b`
- `explanation_c`
- `explanation_d`
- `difficulty`
- `question_type`
- `category`

## 功能二：知識樹建立與重整

- 可從課綱、歷屆試題、教材目錄或既有題庫建立知識樹。
- 先對齊同工作區參考檔的欄位、層級、空白沿用方式與命名粒度。
- 不直接照抄課綱條文；要整理成題庫標註可用的穩定概念節點。
- 若參考檔採 `Subject,L1,L2,L3`，應沿用該欄位與空白沿用上一層的格式。
- `L3` 應短、名詞化、可重用；避免條文式長句。
- 詳見 `references/knowledge-tree/README.md`。

## 功能三：explanation 解析重複檢查分析

- 檢查 `explanation` 與 `explanation_a` ~ `explanation_d`。
- 目標是降低重複風險，同時保留教學意義與答案邏輯。
- 附帶檢查：
  - 中文、英文、數字間距
  - 全形與半形標點
  - 填空題下劃線長度一致性

建議輸出：

- `optimized_questions.csv`
- `optimization_report.md`
- `changes_log.csv`

## 功能四：level 與 explanation 題目解析撰寫

- 依題幹、選項與答案撰寫整體解析。
- 補寫各選項解析。
- 補齊難度評級或 level 相關欄位。
- 可搭配知識樹與既有分類欄位一起使用，提升術語一致性。

## 建議使用方式

- 若手上是原始題本，先走 `scripts/pipeline/`。
- 若要建立或重整知識樹，先走 `references/knowledge-tree/`。
- 若欄位已完整但 explanation 品質不穩，走 `references/explanation-review/`。
- 若缺少解析或難度，走 `references/analyzer/`。
- 若要做完整題庫加工，依序執行需要的子流程。
