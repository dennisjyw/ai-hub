# ai-hub

`ai-hub` 是一個跨裝置、跨大語言模型共用的工作規則與技能中樞。它把不同 AI 工具需要讀取的入口檔、共享規則、技能索引與記憶系統路標集中在同一個專案中，讓 Codex、Claude Code 或其他支援專案指令的代理人可以用一致的方式理解使用者偏好、工作流程與可用能力。

## 這個專案解決什麼

當同一個人會在不同裝置、不同模型或不同代理工具之間切換時，最容易漂移的是：

- 每個模型該先讀哪些規則。
- 對話語言、工程習慣與驗證標準是否一致。
- Skill 應該怎麼被發現、觸發與按需載入。
- 長期記憶與專案脈絡的入口在哪裡。

本專案的目標是提供一組短入口與共享規則，讓模型不要每次都從零開始，也避免把大量細節塞進單一 prompt。

## 核心檔案

| 檔案或目錄 | 用途 |
| --- | --- |
| `AGENTS.md` | 給 Codex 或支援 `AGENTS.md` 的代理人讀取的專案入口。 |
| `CLAUDE.md` | 給 Claude Code 讀取的專案入口。內容與 `AGENTS.md` 對齊，確保不同工具載入同一套規則。 |
| `AGENTS_DOCS.md` | 共享核心規則，包含角色、載入順序、工作方式、檔案安全、驗證標準、技術偏好、回應格式與記憶規範。 |
| `skills/README.md` | Skill 索引，只描述可用技能與最小觸發條件，不預先展開所有技能內容。 |
| `skills/**/SKILL.md` | 各技能的實際操作說明。只有任務明確符合 trigger 時才讀取。 |
| `docs/memory.md` | Memory 系統的本地路標，指向主要記憶索引與模板位置。 |
| `AGENTS.local.md`、`CLAUDE.local.md` | 本機私有覆寫入口，適合放不應同步或只適用單一裝置的補充規則。 |

## 建議載入順序

模型或代理人進入本專案時，建議依序讀取：

1. `AGENTS.md` 或 `CLAUDE.md`
2. `AGENTS_DOCS.md`
3. `skills/README.md`
4. 視任務需要，再讀對應的 `skills/**/SKILL.md`
5. 若任務涉及記憶、歷史決策或跨專案一致性，再依 `docs/memory.md` 讀取記憶索引

這個順序的重點是「短入口、共享規則、按需展開」。不要在每次 session 一開始就讀完整個 `skills/` 目錄。

## Skill 設計原則

`skills/README.md` 是技能系統的總索引。它只保存三件事：

- Skill 名稱。
- 何時該使用這個 skill。
- Skill 所在路徑。

技能細節應留在各自的 `SKILL.md`、`references/`、`scripts/` 或 `README.md` 中。這樣可以讓模型先用低成本建立方向，只有真的需要某項能力時才載入完整上下文。

新增或維護 skill 時，請優先確認：

- `skills/README.md` 的 trigger 是否短而準。
- `SKILL.md` 是否能獨立指導模型完成任務。
- 大量範例、schema、長規範是否已下放到 references 或 scripts。
- 是否避免和既有技能重疊太多。

## Agents 與 Claude 入口

`AGENTS.md` 和 `CLAUDE.md` 刻意保持簡短，主要負責告訴模型：

- 先讀 `AGENTS_DOCS.md`。
- 再讀 `skills/README.md`。
- 使用繁體中文（台灣）互動。
- Memory 系統的路標在 `docs/memory.md`。

如果要調整跨工具共用的行為，優先修改 `AGENTS_DOCS.md`，不要分別在 `AGENTS.md` 和 `CLAUDE.md` 寫兩份不同規則。這能降低不同模型讀到不一致指令的風險。

## Memory 系統

本專案只保存 memory 的路標，不直接承載完整長期記憶。請參考：

- `docs/memory.md`
- `AGENTS_DOCS.md` 的記憶與文件規範

目前記憶系統的設計重點是：

- Session 開始或需要歷史脈絡時，先讀記憶索引。
- 記憶只作為輔助脈絡；可能過期的事實要查證現況。
- 更新長期規則、技能或索引時，維持「短入口、細節下放、按需載入」。

## 維護原則

- 入口檔保持短，不把大量工作流程塞進 `AGENTS.md` 或 `CLAUDE.md`。
- 共享規則集中在 `AGENTS_DOCS.md`，避免多處漂移。
- Skill 索引只放觸發條件，細節放回技能目錄。
- 本機私有規則放在 `.local.md` 檔案，不應混進共享規則。
- 修改文件後，至少回讀確認連結、檔名、trigger 與載入順序仍一致。

## 快速開始

如果你是新的模型或代理人，先讀：

```text
AGENTS.md 或 CLAUDE.md
AGENTS_DOCS.md
skills/README.md
```

如果你是人類維護者，最常修改的是：

```text
AGENTS_DOCS.md      # 調整共用工作規則
skills/README.md   # 新增或調整 skill trigger
skills/**/SKILL.md # 修改特定技能的實作指引
docs/memory.md     # 更新記憶系統路標
```
