---
name: question-workflow
description: 當使用者要整理題庫欄位、把 Word／Excel／PDF 題本轉成結構化 CSV、補寫題目解析、做 explanation 查重與改寫、補難度或 level 時使用。只要任務核心是題庫加工流程，就應直接觸發此技能。
---

# Question Workflow

## 何時使用
- 題目匯入、欄位整理、題庫 CSV 正規化。
- 建立或重整題庫知識樹。
- explanation 改寫、查重風險檢查、格式統一。
- 補寫 `difficulty`、`level`、整體解析與選項解析。
- **批次撰寫題目解析（explanation、explanation_a/b/c/d），採分段執行（每10題一階段）與定期審查（每20題 Review）模式。**

## 子流程
1. 題目來源轉結構化欄位。
2. 建立或重整知識樹。
3. 補寫或修正 explanation / level。
4. 做 explanation 查重分析與最終格式校正。
5. **批次解析撰寫：分段撰寫 explanation 與選項解析（每10題一階段，每20題 Review）。**

## 載入策略
- 做欄位整理時，先讀 [scripts/pipeline/README.md](scripts/pipeline/README.md)。
- 做知識樹建立或重整時，先讀 [references/knowledge-tree/README.md](references/knowledge-tree/README.md)。
- 做 explanation 改寫時，讀 [references/explanation-review/README.md](references/explanation-review/README.md)；需要範例再看 [EXAMPLES.md](references/explanation-review/EXAMPLES.md)。
- 做解析與難度補寫時，讀 [references/analyzer/README.md](references/analyzer/README.md)。
- **做批次解析撰寫（每10題一階段、定期Review）時，讀 [references/batch-explanation/README.md](references/batch-explanation/README.md)**。
- 只有在需要完整背景時才讀 [README.md](README.md)。

## 執行流程
1. 先確認來源格式、目標欄位、既有命名規則與是否有知識樹。
2. 只啟動當前需要的子流程，不要預設整包全做。
3. 優先維持既有 CSV 欄位順序、術語與分類。
4. 若是建立知識樹，先比對既有同類知識樹的欄位、層級、空白沿用方式與命名粒度，再決定輸出 schema。
5. 若輸出是 CSV，需同步做欄位內容標點正規化：把欄位值中的半形逗號 `,` 改成全形 `，`，把半形括號 `()` 改成全形 `（）`；不得動到 CSV 分隔符本身。
6. 交付時說清楚本次執行了哪些步驟、哪些欄位是新增或改寫。

## 輸出要求
- 結構化 CSV 或明確欄位對照。
- 若有改寫 explanation，需保留原意並修正常見格式問題。
- 若輸出 CSV，欄位內容不得保留會與分隔符混淆的半形逗號；中文語境下的括號一律使用全形 `（）`。
- 若補寫難度或解析，必須沿用既有分類語言，不自創新體系。
