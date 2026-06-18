---
name: frontend-design
description: 當要建立具辨識度、可上線、避免 AI 套版感的前端介面時使用。這是核心設計實作技能，負責定義方向並在需要時讀取 typography、color、motion、responsive 等 reference。
---

## 何時使用
- 新做頁面、元件或設計導向的前端實作。

## 第一步：紮根主題（Ground it in the subject）
設計前先釘定三件事：
1. **主題**：產品或頁面的具體對象是什麼？
2. **受眾**：使用者是誰、他們的期待是什麼？
3. **頁面任務**：這頁只做一件事——是什麼？

從主題本身的材質、工具、產物與語彙抽取設計語言。讓 hero 呈現最能代表主題的元素，而非放泛用的漂亮圖（**hero 是論點，不是裝飾**）。

## 兩段式設計流程

**Pass 1 — 規劃 token system（先不要動手刻）**

建立一份精簡的設計計畫，涵蓋：
- **色彩**：4–6 個具名 hex 值
- **字體**：display（個性）/ body（易讀）/ utility（說明、數字）三個角色
- **Layout**：ASCII wireframe 勾勒主要版型
- **Signature element**：一個最有記憶點的設計錨點

**Pass 2 — 自我稽核，再開始 build**

對照 brief 檢查計畫是否落入 template default：
- 有沒有只因「常見」而選的字體或配色？
- Signature element 是否真的源自主題？
- 每個結構元素是否傳遞資訊，還是只是裝飾？

稽核通過後才開始實作；實作後再跑一次設計評論（`critique`）。

## 核心設計原則

- **集中大膽**：把視覺張力集中在一個 signature element，周圍保持安靜克制。不要分散注意力。
- **結構即資訊**：數字標記、分組、縮排只用在真正有結構關係的內容；裝飾性分隔不是資訊。
- **動態服務主題**：動效要有敘事目的，不散落使用。

## 載入策略
按需讀 `references/`：
- 排版：`typography.md`
- 配色與對比：`color-and-contrast.md`
- 空間與節奏：`spatial-design.md`
- 動態：`motion-design.md`
- 互動：`interaction-design.md`
- 響應式：`responsive-design.md`
- 文案：`ux-writing.md`
