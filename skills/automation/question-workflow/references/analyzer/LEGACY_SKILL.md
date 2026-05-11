# 分析器規格

此文件定義 `question-workflow/references/analyzer` 的完整分析與撰寫規格。

## 目標

- 依題幹、選項與答案生成整體解析。
- 補寫各選項解析。
- 補齊 `difficulty` 或 level 相關欄位。
- 在同一批題目中維持術語、分類與難度標準一致。

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

## 主要輸出欄位

- `explanation`
- `explanation_a`
- `explanation_b`
- `explanation_c`
- `explanation_d`
- `difficulty`

## 處理流程

1. 讀取題目內容與既有分類欄位。
2. 判斷題目考查的核心概念與答案依據。
3. 撰寫整體解析 `explanation`。
4. 逐一撰寫各選項解析 `explanation_a` ~ `explanation_d`。
5. 評估題目難度並補齊 `difficulty`。
6. 檢查同批題目的術語與分類是否一致。

## 解析撰寫規範

### 整體解析 `explanation`

- 第一段先指出本題考查的核心概念或理論。
- 第二段說明題幹關鍵資訊與正確答案的對應依據。
- 內容須具備教學性，避免只寫結論。
- 長度以精準完整為原則，不刻意冗長。

### 選項解析 `explanation_a` ~ `explanation_d`

- 正確選項要說明為何成立。
- 錯誤選項要指出錯誤原因、誤解點或與題意不符之處。
- 各選項解析應避免模板化重複句型。
- 若選項差異細微，需明確指出關鍵辨識點。

## 難度評級原則

- `1-3`：單一概念、可直接判斷。
- `4-6`：需要理解概念並做基本應用。
- `7-8`：需整合多個概念或進行分析。
- `9-10`：需跨概念整合、深度推理或高度辨析。

## 品質要求

- 解析內容必須與標準答案一致。
- 理論名稱、學者名稱與專有名詞需正確。
- 同一知識點在同一批資料中應使用一致術語。
- 若已有 `level_1` ~ `level_3`，解析內容應與分類相互對齊。
