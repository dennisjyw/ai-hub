# 技能索引

此檔只做兩件事：列出可用技能，並提供最小觸發規則。

## 使用規則
- 啟動時只讀本檔，不預先展開各技能內容。
- 本索引只列頂層入口 skill；像 `pm-dev/skills/*`、`frontend-design/skills/*` 這類內部子技能不在此表展開。
- 只有在需求明確符合時，才讀取對應技能的 `SKILL.md`、`CLAUDE.md` 或 `references/`。
- 若多個技能同時符合，優先選最少且最直接的一組，避免上下文膨脹。
- 索引文案統一用「當……時使用」描述 trigger，不在這裡塞教學細節。
- 所有互動使用繁體中文（台灣）。

## 技能清單

| 技能 | Trigger 文案 | 路徑 |
| --- | --- | --- |
| `pm-dev` | 當使用者要做新產品、工具或 MVP，但平台尚未明確時使用。 | `skills/product/pm-dev/` |
| `pm-web` | 當需求明確是網站、Web app、瀏覽器介面或前後端 Web 功能時使用。 | `skills/product/pm-web/` |
| `pm-ios` | 當需求明確是 iPhone、iPad、iOS app、Apple HIG 或 iOS 優先專案時使用。 | `skills/product/pm-ios/` |
| `pm-assistant` | 當提到需求分析、PRD、用戶故事、產品規劃、競品分析、OKR、路線圖時使用。 | `skills/product/pm-assistant/` |
| `tech-lead-mentor` | 當要新增功能、重構、做工程決策或拆技術風險時使用。 | `skills/engineering/tech-lead-mentor/` |
| `n8n-agent` | 當需求核心是 n8n workflow、AI Agent 流程或可匯入的 workflow JSON 時使用。 | `skills/automation/n8n-agent/` |
| `question-workflow` | 當要整理題庫欄位、轉結構化 CSV、補解析、做 explanation 改寫或補難度時使用。 | `skills/automation/question-workflow/` |
| `pdf` | 當主要輸入或輸出是 PDF，且任務涉及讀取、拆併、抽字、OCR 或文件操作時使用。 | `skills/tools/pdf/` |
| `docx` | 當主要輸入或輸出是 Word `.docx`，且任務涉及建立、修改、分析或格式化文件時使用。 | `skills/tools/docx/` |
| `xlsx` | 當主要輸入或輸出是 Excel `.xlsx`，且任務涉及讀寫、整理、重算或模板更新時使用。 | `skills/tools/xlsx/` |
| `pptx` | 當主要輸入或輸出是 PowerPoint `.pptx`，且任務涉及建立、修改、整理或抽取簡報內容時使用。 | `skills/tools/pptx/` |
| `auth` | 當使用者提到「註冊」、「登入」、「用戶認證」、「帳號系統」或需要實作身份驗證功能時使用。 | `skills/tools/auth/` |
| `skill-creator` | 當要建立新 skill、改寫既有 skill、瘦身 `SKILL.md`、優化 trigger 或做 skill 評估時使用。 | `skills/tools/skill-creator/` |
| `tw-academic-literature-collector` | 當需要蒐集台灣學術文獻、進行文獻回顧、需要 APA 格式引文整理時使用。輸出 Excel、Word、視覺化網絡圖、AI 缺口分析。 | `skills/tools/tw-academic-literature-collector/` |
| `literature-imrad-analyzer` | 當使用者上傳 PDF 論文並要求分析、拆解結構、整理方法或說「幫我讀這篇 paper」時使用。 | `skills/tools/literature-imrad-analyzer/` |
| `citation-integrity-assistant` | 當使用者要查引用是否存在、補充文獻、追蹤理論源頭或找替代文獻時使用。 | `skills/tools/citation-integrity-assistant/` |
| `design-library` | 當要參考 Stripe、Linear、Apple、Figma 等知名產品的設計語言時使用。 | `skills/design/design-library/` |
| `design-kungfu` | 當說「幫我設計一個...」、「給我推薦設計風格」、「設計建議」時使用。 | `skills/design/design-kungfu/` |
| `clone-website` | 當要 clone、重建或高擬真還原現有網站頁面時使用。 | `skills/frontend/clone-website/` |
| `frontend-design` | 當要做前端介面設計、改版、設計 review 或使用 `/audit`、`/polish` 等子技能時使用。 | `skills/frontend/frontend-design/` |
| `impeccable` | 當需要高品質前端設計總控，或說「讓設計更大膽」、「簡化介面」等自然語言需求時使用。 | `skills/frontend/impeccable/` |
| `react-best-practices` | 當編寫、審查或重構 React/Next.js 代碼，需要性能優化指南時使用。 | `skills/frontend/react-best-practices/` |
| `tailwind` | 當要用 Tailwind CSS 建立設計系統、遷移至 v4、實作設計令牌，或需要打磨 UI 細節時使用。 | `skills/frontend/tailwind/` |
| `neat` | 當對話結束後要同步文件、更新記憶、清理過期資訊，或使用者說「整理一下文件」、「更新記憶」時使用。 | `skills/tools/neat/` |
| `excalidraw` | 當使用者要求「建立圖表」、「畫流程圖」、「繪製架構圖」、「建立心智圖」或產生 .excalidraw 檔案時使用。 | `skills/tools/excalidraw/` |
| `shadcn` | 當任務涉及 shadcn/ui 元件安裝、選型、表單、圖表或 theme 整合時使用。 | `skills/frontend/shadcn/` |
| `obsidian-markdown` | 當要建立或修改 Obsidian 筆記，且需要 wikilinks、callouts、embeds 或 properties 時使用。 | `skills/obsidian/markdown/` |
| `obsidian-bases` | 當要建立或修改 Obsidian `.base`、views、filters、formulas 或 summaries 時使用。 | `skills/obsidian/bases/` |
| `json-canvas` | 當要建立或修改 Obsidian `.canvas`、節點、連線、群組或視覺流程圖時使用。 | `skills/obsidian/canvas/` |
| `obsidian-cli` | 當要用 Obsidian CLI 搜尋、建立、更新或批次管理 vault 內容時使用。 | `skills/obsidian/cli/` |
| `brainstorming` | 當要進行任何創意工作（新功能、元件、行為修改）前，必須先探索需求與設計時使用。 | `skills/brainstorming/` |
| `pua` | 當任務連續失敗 2 次以上、開始卡循環、想放棄或想把工作推回給使用者時必須使用。 | `skills/pua/` |

## 維護原則
- 新增技能時，先確保 `name`、`description` 與 trigger 文案一致，再補進本索引。
- 索引只保留一行 trigger，不重複貼 `SKILL.md` 內容。
- 長篇說明、範例、schema 與腳本細節放進技能自己的 `references/`、`README.md` 或 `scripts/`。
