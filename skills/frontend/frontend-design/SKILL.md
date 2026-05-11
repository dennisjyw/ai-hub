---
name: frontend-design
description: 當使用者要做前端介面設計、頁面改版、UI 精修、設計 review、互動優化或要用 `/audit`、`/polish`、`/optimize` 等設計子技能時使用。這是前端設計的主路由技能，負責挑選合適的子技能，不應把所有設計理論一次載入。
license: Apache-2.0
---

# Frontend Workflow

## 何時使用
- Web 介面設計、改版、視覺優化、體驗提升。
- 使用者提到 `/audit`、`/critique`、`/polish`、`/harden`、`/animate` 等前端設計指令。

## 主技能責任
- 判斷目前需求是「建立、審查、精修、強化、萃取」哪一類。
- 只路由到必要子技能，不把 17 個子技能全部塞進上下文。
- 維持共同設計底線：避免制式 AI 風格、重視階層、可讀性、響應式與品牌感。

## 常用路由
- 新做頁面或元件：`frontend-design`
- 設計審查：`audit`、`critique`
- 發版前精修：`polish`
- 韌性與邊界案例：`harden`
- 動態效果：`animate`
- 一致性整理：`normalize`

## 執行原則
- 一次只載入主技能加上 1 到 2 個子技能。
- 先定義視覺方向，再決定色彩、排版、動態與細節。
- 若需求是局部調整，直接進對應子技能，不重跑完整流程。
