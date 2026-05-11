---
name: obsidian-bases
description: 當使用者要建立或修改 Obsidian `.base` 檔、做 table／cards／list／map 視圖、設定 filters、formulas、summaries 或疑難排解 Base YAML 時使用。這個技能要先維持 YAML 正確，再處理視圖與公式。
---

# Obsidian Bases

## 何時使用
- `.base` 檔建立、修改、除錯。
- Obsidian Bases 的 filters、views、formulas、summaries。

## 載入策略
- 主技能只保留流程與常見陷阱。
- 公式或函式細節再讀 [references/FUNCTIONS_REFERENCE.md](references/FUNCTIONS_REFERENCE.md)。

## 執行流程
1. 先確認資料來源、要顯示哪些筆記、需要哪些欄位。
2. 先寫 `filters`，再寫 `formulas`，最後配置 `views`。
3. 優先驗證 YAML 結構，再檢查屬性名稱與公式引用。
4. 交付前明講全域 filter 與 view-specific filter 的差異。

## 常見陷阱
- YAML 引號錯誤。
- 引用了不存在的 `formula.*`。
- 日期差值是 Duration，不是 Number。
- `views.order` 內的欄位未定義。
