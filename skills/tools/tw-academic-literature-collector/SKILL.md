---
name: tw-academic-literature-collector
description: 繁體中文學術文獻蒐集與整理。觸發時機：使用者需要蒐集台灣學術文獻、進行文獻回顧、需要 APA 格式引文整理、社會科學領域研究文獻分析。輸出 Excel 文獻表(7工作表)、Word 綜述(4章)、視覺化網絡圖、AI 缺口分析。
---

# 繁體中文學術文獻蒐集與整理系統

## 核心功能

1. **多資料庫搜尋**：Google Scholar 直接搜尋 + 碩博網/華藝/TCI-HSS 搜尋指引
2. **文獻品質評估**：TSSCI/THCI 期刊等級、引用數、年份、方法嚴謹度評分
3. **雙格式輸出**：Excel 文獻整理表 + Word APA 7th 格式綜述
4. **視覺化網絡**：引用網絡圖、研究趨勢圖、關鍵字共現圖、作者合作圖
5. **AI 智能分析**：IMRAD 摘要、主題整合、五維度缺口分析、未來研究建議

---

## 工作流程路由

| Phase | 功能 | 核心動作 |
|-------|------|---------|
| 1 | 需求釐清 | 詢問主題、年份範圍、文獻類型、預期數量 |
| 2 | 搜尋執行 | web_search Google Scholar + 生成其他資料庫指引 |
| 3 | 品質評估 | 評分、分級(A/B/C/D) → 詳見 references/quality-criteria.md |
| 4 | Excel 生成 | 7 工作表：總覽/摘要/引文/方法統計/主題/AI摘要/主題整合 |
| 5 | Word 生成 | 4 章：概述/主題綜述/缺口分析/AI報告 |
| 6 | 視覺化 | React Artifacts 建立 4 種互動圖 → 詳見 scripts/citation-network.jsx |
| 7 | AI 分析 | IMRAD 摘要 + 主題整合 + 缺口分析 → 詳見 scripts/ai-summary-prompts.md |
| 8 | 整合輸出 | present_files 呈現所有檔案 |

---

## 輸出規格

### Excel (7 工作表)
```
文獻整理_{主題}_{日期}.xlsx
├── Sheet1: 文獻總覽 (分級、期刊等級、引用數)
├── Sheet2: 文獻摘要 (中英文摘要)
├── Sheet3: 引文清單 (APA 7th 格式)
├── Sheet4: 研究方法統計
├── Sheet5: 主題分類
├── Sheet6: AI 智能摘要
├── Sheet7: 主題整合分析
```

### Word (4 章)
```
文獻綜述_{主題}_{日期}.docx
├── 第一章：文獻綜述概述
├── 第二章：主題分類文獻綜述
├── 第三章：研究趨勢與缺口分析
├── 第四章：AI 智能分析報告
├── 參考文獻 (APA 7th)
```

### 視覺化
```
文獻視覺化_{主題}_{日期}.html (互動式)
視覺化圖表/ (靜態 PNG)
├── 引用網絡圖.png
├── 研究趨勢圖.png
├── 關鍵字共現圖.png
├── 作者合作網絡.png
```

---

## 觸發條件

**明確觸發關鍵字**：蒐集台灣文獻、查找繁體中文研究、碩博士論文搜尋、華藝資料庫、TCI-HSS、文獻回顧、APA格式

**情境觸發**：使用者提到「寫文獻探討」、「如何找台灣的研究」、「APA格式中文引用」

---

## 重要限制

- 碩博網、華藝、TCI-HSS **需學術機構登入**，本技能僅提供搜尋指引
- 品質評估為輔助參考，使用者需自行判讀文獻適切性
- AI 分析結果需批判性檢視，非絕對標準

---

## 輸出存放位置

所有檔案儲存至 `/mnt/user-data/outputs/`

---

## 載入策略

- 主流程與規格看本檔
- 資料庫搜尋細節 → `references/databases.md`
- 品質評估指標 → `references/quality-criteria.md`
- APA 格式範例 → `references/apa-format.md`
- 視覺化程式碼 → `scripts/citation-network.jsx`
- AI 摘要 prompts → `scripts/ai-summary-prompts.md`
- 測試案例 → `references/test-cases.md`
- 範例對話 → `references/example-conversations.md`