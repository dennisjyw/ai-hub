---
name: pm-dev
description: 通用產品開發主流程。當使用者要做新產品、工具、MVP 或功能開發，但平台還不夠明確時使用。這個技能只負責路由與上下文治理，詳細規則交給 discover、design、architect、plan、implement、log_decision 子技能。
---

# pm-dev

## 何時使用
- 使用者說「我想做一個產品／工具／App」但尚未明確指向 Web 或 iOS。
- 需要從模糊需求一路收斂到規格、架構、任務與實作。

## 路由規則
- 明確是 Web：改用 `pm-web`。
- 明確是 iOS：改用 `pm-ios`。
- 需求還模糊：從 `discover` 開始。
- 使用者已指定階段：只讀該子技能。

## 核心檔案
- `.spec/spec.md`：產品目標、使用者、流程、設計規格。
- `.spec/build.md`：技術架構、資料模型、里程碑、任務。
- `.spec/memory.md`：已確認決策、變更、假設與未解問題。

## 執行原則
- 主技能只做路由，不重複子技能內容。
- 一次只載入當前階段需要的技能，避免上下文膨脹。
- 高風險決策先確認；低風險整理與補件可直接做。

## 階段順序
`discover -> design -> architect -> plan -> implement -> log_decision`
