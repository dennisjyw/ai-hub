# AGENTS.md
> [!IMPORTANT]
> **先閱讀共用設定**
> 閱讀 [AGENTS_DOCS.md](file:///Users/denniswang/ai-hub/AGENTS_DOCS.md) 以取得核心規則與設定。
> 閱讀 [skills/README.md](file:///Users/denniswang/ai-hub/skills/README.md) 以查看可用技能。

## 專案記憶（MEMORY.md）

每個專案根目錄下有一份 `MEMORY.md`，是跨工具（Claude Code、Codex 等）的共享專案脈絡檔。

- Session 開始時，若存在 `MEMORY.md`，優先讀取以取得最新進度與脈絡。
- 任務完成或對話結束前，將完成事項、新決策、已知問題與下一步更新回 `MEMORY.md`。
- 格式與維護規則見 [AGENTS_DOCS.md](AGENTS_DOCS.md) 第 10 節。

## 全域記憶系統

全域 Claude 記憶庫位於 `~/.claude/memory/`，用於跨專案的使用者偏好、回饋與長期脈絡。詳見 [AGENTS_DOCS.md](AGENTS_DOCS.md) `專案記憶（MEMORY.md）`。
