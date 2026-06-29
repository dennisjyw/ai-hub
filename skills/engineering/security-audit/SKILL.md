---
name: security-audit
description: 當使用者要求對 codebase 做安全審計、抓漏洞、安全 review、滲透測試、pen-test、找可利用的漏洞時使用。涵蓋 web app、API、服務、CLI 工具、函式庫、daemon 等。重點是可被 exploit 的真實漏洞，不是理論風險或產業標準偏差。
---

# Security Audit

你的任務是找出 **可被 exploit 且具真實影響力的漏洞**。本檔是路由與方法論總覽；細節與各階段 prompt 模板放在 `references/`，只在對應階段需要時才讀。

## 平台術語對應

本 skill 為 agent-neutral，方法論中的角色對應如下：

- **Task tool** → Claude Code 的 `Agent` 工具（或其他子代理人機制）
- **`research` agent** → `subagent_type: Explore` 或同類只讀深掘 agent
- **`general` agent** → `subagent_type: general-purpose` 或同類可自主派生 sub-agent 的 agent
- **`subagent_type`** → 用目前平台等價的角色即可

保留指定角色、平行度、prompt 與獨立性邊界。

## 設定

啟動前先確立兩個路徑：

- **Target**：要審計的 codebase（從使用者請求或當前工作目錄推斷）
- **Output directory**：所有產出寫到這裡。
  - 未指定時主動詢問；或預設 `~/security-audit-skill/<repo-name>/run-<N>`，`<N>` 取下一個未使用的整數（先 `ls` 檢查），不存在就 `mkdir -p`。
  - 同 repo 的多次 run 各自獨立，每次跑不同 code path。

寫入 Output directory 的檔案：

| 檔案 | 內容 |
|------|------|
| `architecture.md` | Phase 1 產出，會被原封注入 Phase 2 的 agent prompt |
| `REPORT.md` | 人讀報告（Phase 4） |
| `FINDINGS-DETAIL.md` | MEDIUM 以上 finding 的詳細資料流（Phase 4） |
| `findings.json` | 結構化輸出（Phase 5） |

**Subagent 不寫檔**。Phase 2/3/6 的 subagent 透過 Task tool 把結果回傳給你，由你統一寫檔。

## 六階段流程

| 階段 | 名稱 | 細節 |
|------|------|------|
| 1 | Recon | `references/RECONNAISSANCE.md` |
| 2 | Hunt | `references/HUNTING.md` + `references/ATTACK-CLASSES.md` |
| 3 | Validate | `references/VALIDATION-AND-REPORTING.md`（Phase 3） |
| 4 | Report | 同上（Phase 4） |
| 5 | Structured output | 同上（Phase 5）+ `references/report-schema.json` + `references/validate-findings.cjs` |
| 6 | Independent verification | 同上（Phase 6） |

必須照順序走，不可跳。

### 既有 run 處理

啟動 Phase 2 之前先 `ls ~/security-audit-skill/<repo-name>/`，若已有 `findings.json`：

1. 跳過已知 finding（避免浪費 agent 重挖）
2. 鎖定缺口（前次偏 injection，這次加重 business logic 與 wildcard）
3. 解決前次 verdict 衝突的項目

在 `architecture.md` 加一段「prior runs summary」給 Phase 2 agent 看。

## 核心原則

### 只回報可被 exploit 的

每個 finding 必須有具體攻擊情境：誰是攻擊者、做什麼、得到什麼。「理論上可以」不是 finding，「送這個 request 拿到 X」才是。

### 動態決定 baseline

Phase 1 識別應用類型與可比較的對標產品。CMS 比 CMS、API gateway 比 API gateway；同樣 pattern 在對標被 exploit 過 = 這個 finding 強度上升，從未被 exploit = 要先理解為什麼。

### 縱深防禦缺口不是漏洞

如果 Layer A 已阻擋攻擊，缺 Layer B 是 hardening 建議，不是 finding。要列就另外放 hardening note，severity 不要灌水。

### Severity 是 likelihood × impact

- **CRITICAL**：未授權 RCE、完整 DB dump、無憑證 admin takeover
- **HIGH**：授權後 RCE、SQLi 資料外洩、stored XSS 全使用者觸發、auth bypass；或 RBAC/權限模型對某動作被**完全**擊敗
- **MEDIUM**：限定條件 XSS、有意義 state change 的 CSRF、敏感資料外洩；或有限後果的 business logic 繞過（需授權、影響限於自己資料、罕見條件）
- **LOW**：非敏感資料外洩、需持續努力的 DoS、hardening 缺口

HIGH vs MEDIUM 的關鍵：**是否擊敗系統明確設的安全邊界**。如果無法描述攻擊者實際造成的損害，severity 應該下修。

## 載入策略

| 何時讀什麼 | 檔案 |
|------------|------|
| Phase 1 開始 | `references/RECONNAISSANCE.md` |
| Phase 2 開始 | `references/HUNTING.md` |
| 選擇攻擊類別 | `references/ATTACK-CLASSES.md` |
| Phase 3-6 開始 | `references/VALIDATION-AND-REPORTING.md` |
| 寫 `findings.json` 前 | `references/report-schema.json` |
| 驗 schema | `node references/validate-findings.cjs <path>/findings.json` |

主檔不重複列反模式與細節，開新 run 時只先讀本檔，到對應階段再下拉 references/。

## 輸出要求

1. `REPORT.md` 必須包含：
   - 一段 executive summary（誠實評估安全 posture）
   - 識別出的 baseline 與本應用比較
   - Findings table（severity、title、one-line 描述）
   - 每個 finding：檔案路徑、具體攻擊情境、影響、建議修法
   - Hardening notes（縱深防禦建議，**不是** finding）
   - Positive patterns（codebase 做對的地方，建立 finding 可信度）
2. `FINDINGS-DETAIL.md` 只收 MEDIUM 以上：完整資料流 + 攻擊 request + 攻擊者得到什麼 + baseline 對標處理方式
3. `findings.json` 嚴格符合 schema（`additionalProperties: false`），通過 `validate-findings.cjs`

報告寧可短。三個真 MEDIUM 比三十個 LOW 有用。「沒找到」也是誠實答案，但要夠努力才得出。

## 反模式（速查）

完整版見 `references/SKILL.md` 與 `references/RECONNAISSANCE.md`，最常見的 5 個：

1. 把所有偏離 OWASP 的東西當 finding — OWASP 是 checklist 不是 bug list
2. 把 hardening 缺口評為 HIGH/CRITICAL
3. 忽略 deployment model（CDN 層 rate limit 是合法架構）
4. 寫「可能 / 理論上」就交 — 要有 exploit 證明
5. 太早放棄（「用了 parameterized query 就沒 SQLi」）— 查每一條 `sql.raw()`、動態 identifier、FTS 路徑

## 依賴

- 支援 tool use + 平行 sub-agent 的 coding agent（本環境用 Claude Code Agent tool）
- Node.js（執行 `validate-findings.cjs`）

## 來源

本 skill fork 自 [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)（MIT）。詳細方法論、attack class 完整 prompt、schema 規格與 validator 都在 `references/`，原文未翻譯，僅本路由層為繁中。
