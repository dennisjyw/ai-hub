---
name: clone-website
description: 當使用者要 clone、重建、臨摹、reverse-engineer 某個網站或頁面，而且要求高視覺擬真度時使用。這個技能負責先做瀏覽器勘查、抽規格、再實作；不是只靠截圖猜版面。
argument-hint: "<url1> [<url2> ...]"
user-invocable: true
---

# Clone Website

## 何時使用
- 使用者說要 clone、copy、rebuild、pixel-perfect 重做網站。
- 需求核心是「還原現有網站視覺與互動」。

## 先決條件
- 必須有可用的 browser automation 工具。
- 專案需能正常 build。
- URL 必須可實際打開與檢視。

## 工作原則
- 先抽規格，再實作；不要憑記憶直接切版。
- 先做 foundation，再拆 section。
- 外觀與互動都要抽，不只看靜態畫面。
- 多個網址可平行，但每個站點的研究產物必須分開保存。

## 最小流程
1. 驗證網址、工具與專案可用性。
2. 擷取桌機／手機截圖、字體、色彩、資產、全域互動。
3. 建立頁面拓樸與行為紀錄。
4. 先完成全域 foundation：fonts、tokens、globals、資產下載。
5. 逐 section 產規格並實作，必要時再平行拆工。
6. 最後驗證 `tsc` 與 `build`。

## 必存研究產物
- `docs/design-references/`：主要截圖。
- `docs/research/BEHAVIORS.md`：互動與狀態。
- `docs/research/PAGE_TOPOLOGY.md`：區塊拓樸。
- `docs/research/components/`：各元件規格。

## 交付要求
- 說明哪些部分是精準還原、哪些部分以 mock data 代替。
- 若原站互動模型複雜，明確標出 click / scroll / hover / time-driven 差異。
