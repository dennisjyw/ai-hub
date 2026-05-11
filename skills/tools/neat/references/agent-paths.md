# Agent 記憶與設定路徑速查

不同 Agent 平台的記憶系統和專案設定檔位置不一樣。執行第一步盤點時按你正在使用的平台查這張表。

## Claude Code

| 用途 | 路徑 |
|---|---|
| 跨會話記憶（全局） | `~/.claude/projects/<encoded-project-path>/memory/` |
| 記憶索引檔案 | `~/.claude/projects/<...>/memory/MEMORY.md` |
| 全局指令 | `~/.claude/CLAUDE.md` |
| 專案級指令 | 專案根目錄 `CLAUDE.md`（可層級巢狀） |
| 技能目錄 | `~/.claude/skills/<name>/SKILL.md` |

記憶檔案使用 YAML frontmatter：`name`、`description`、`type`（user / feedback / project / reference）。

## OpenAI Codex

| 用途 | 路徑 |
|---|---|
| 跨會話指令（全局） | `~/.codex/AGENTS.md` 或 `$CODEX_HOME/AGENTS.md` |
| 專案級指令 | 專案根目錄 `AGENTS.md`（可層級巢狀） |
| 專案級 override | `AGENTS.override.md`（若存在，覆蓋同目錄 AGENTS.md） |
| 技能目錄 | `~/.codex/skills/<name>/SKILL.md` 或專案內 `.codex/skills/<name>/` |

Codex 沒有獨立的「記憶檔案 + 索引」機制，所有跨會話資訊都直接寫在 `AGENTS.md` 裡。同步時把「專案事實」那部分內容統一放 AGENTS.md。

若專案裡有 `TEAM_GUIDE.md` 或 `.agents.md` 也要看——這是 Codex 的 fallback 檔名。

## 若當前 Agent 沒有獨立記憶系統

跳過「記憶」那一層，把功夫全花在：
- 專案根目錄 markdown（CLAUDE.md / AGENTS.md）
- README.md
- docs/

仍然是有效的同步——記憶是錦上添花，docs 才是專案知識的最低保障。
