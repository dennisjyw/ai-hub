# 分析器

此區塊負責 `level` 與 `explanation` 題目解析撰寫，是 `question-workflow` 內的第三個子功能。

## 核心能力

- 自動識別考點與核心概念
- 生成整體解析 `explanation`
- 生成選項解析 `explanation_a` ~ `explanation_d`
- 評估難度或補齊 `difficulty`
- 搭配知識樹維持分類與術語一致性

## 建議輸入欄位

- `question_stem`
- `option_a`
- `option_b`
- `option_c`
- `option_d`
- `answer`
- `subject_category`
- `year`
- `number`
- `level_1`
- `level_2`
- `level_3`

## 建議輸出欄位

- `explanation`
- `explanation_a`
- `explanation_b`
- `explanation_c`
- `explanation_d`
- `difficulty`

## 撰寫原則

- 先指出題目考查的核心概念，再說明答案判斷依據。
- 各選項解析要明確說清楚正誤原因。
- 若已有知識樹欄位，優先延續既有分類詞彙。
- 難度評級須與題目所需推理深度一致。
