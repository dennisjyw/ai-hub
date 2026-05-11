---
name: pm-web
description: 當需求明確是網站、Web app、後台、瀏覽器介面或前後端 Web 功能時使用。這個技能負責把需求導向 Web 專用流程與參考資料，避免與通用 `pm-dev` 或 `pm-ios` 混用。
---

# pm-web

## 何時使用
- 網站、Web app、Dashboard、Admin、前後端 Web 功能。
- 需要以瀏覽器體驗、SEO、表單、登入、後台等情境來規劃。

## 路由規則
- 平台未明時回到 `pm-dev`。
- 明確是 iOS app 時改用 `pm-ios`。
- Web 任務沿用 `pm-dev` 階段流程，再按需讀 Web 參考資料。

## 載入策略
- 主技能只做 Web 場景判斷與路由。
- 需要平台細節時再讀 `references/` 內的對應檔案。
