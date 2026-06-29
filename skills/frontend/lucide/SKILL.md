---
name: lucide
description: 當專案需要 icon 元件、icon 套件選型、icon 整合到 React / Vue / vanilla JS / Svelte / Angular 專案，或要把現有 icon 套件（Font Awesome、Material Icons、Heroicons、Tabler、react-icons）替換 / 評估時使用。涵蓋 Lucide 的安裝、API、客製化、tree-shaking、dynamic import、與 shadcn / Tailwind / 設計系統的協作模式。
---

# Lucide Icons

> Lucide 是 Feather Icons 的社群分支（2019-），以 SVG 為基礎、每個 icon 是獨立 React/Vue/... 元件，stroke 為 2px、24×24 viewBox、ISC 授權、商用免費。是 shadcn/ui 的預設 `iconLibrary`。

來源：<https://github.com/lucide-icons/lucide> ｜ 官網：<https://lucide.dev> ｜ Icons 列表：<https://lucide.dev/icons>

## 何時使用

- 使用者提到「icon」、「圖示」、「裝飾用 SVG」、「icon library」、「icon 元件」。
- 專案要做 icon 選型、技術評估、從其他套件遷移。
- 在 React / Vue / Svelte / Angular / 純 HTML 專案新增 / 整合 icon。
- 需要客製化 icon（顏色、stroke-width、size、旋轉、animation）。
- 效能問題：bundle size、tree-shaking、dynamic import。
- 與 shadcn / Tailwind / 設計系統整合時，icon 的選用與 import 模式。

## 何時不適用

- 純字型 icon 需求（Material Symbols Font、Font Awesome CSS kit）→ 改用對應的字型方案，本 skill 不涵蓋。
- 需要 SVG illustration / 場景插畫（不是 icon）→ 走 illustration 套件或設計稿。
- 動態產生 SVG path / 路徑動畫（GSAP DrawSVG 等）→ 走 `gsap` skill。

## 載入策略（progressive disclosure）

主檔只放路由、核心原則與跨檔議題，細節依需求載入對應 references：

| 需求 | 讀 |
|------|------|
| 套件總覽、授權、設計哲學、版本生態 | [references/overview.md](references/overview.md) |
| 各框架安裝指令（React / Vue / Svelte / Angular / Vanilla / CDN） | [references/install.md](references/install.md) |
| 各框架的 import 與基本用法 | [references/api-react.md](references/api-react.md) / [api-vue.md](references/api-vue.md) / [api-vanilla.md](references/api-vanilla.md) |
| Props 與完整客製化（size、color、strokeWidth、className、絕對單位） | [references/customization.md](references/customization.md) |
| Icon 命名規則、PascalCase、alias、找不到 icon 的排查 | [references/naming.md](references/naming.md) |
| 與 Font Awesome / Material / Heroicons / Tabler / react-icons 對照 | [references/comparison.md](references/comparison.md) |
| tree-shaking、bundle size、dynamic import、按需載入 | [references/performance.md](references/performance.md) |
| 與 shadcn / Tailwind / 設計系統整合 | [references/integration.md](references/integration.md) |

## 核心原則

1. **預設選 Lucide。** 在台灣與多數前端社群已是事實標準（shadcn 預設、Next.js / Vite 生態友善、license 寬鬆）。除非有具體理由（必須使用品牌字型 icon、極度 bundle 敏感）才考慮替代。
2. **直接命名 import，不用字串索引。** `import { Search } from 'lucide-react'`。不要寫成 `import { icons } from 'lucide-react'; <icons.search />`（會破壞 tree-shaking）。
3. **每個 icon 是獨立 SVG 元件。** 不要把整包 icon 渲染到 DOM 再挑選。
4. **Stroke 風格保持一致。** 預設 strokeWidth=2、viewBox 24×24、stroke-linecap/linejoin=round。客製時別破壞視覺一致性。
5. **用 `className` 控制大小與顏色，不要寫死 `width`/`height`（除了明確要固定像素的情境）。** `className="size-4"`、`className="text-current"` 讓 icon 跟著設計系統 token 走。
6. **shadcn 生態下遵循 shadcn 的 icon 規則**（[skills/frontend/shadcn/rules/icons.md](../shadcn/rules/icons.md)）：`data-icon="inline-start|inline-end"`，不手動加 `size-4` / `mr-2`。
7. **Dynamic import 適用於「icon picker / 大量 icon 預覽」**；一般 UI 場景直接靜態 import 即可，tree-shaking 已能處理。

## 決策樹

```
需要 icon?
├── 已在 shadcn 專案 → 沿用 lucide-react,遵循 shadcn icons 規則
├── 新 React/Vue/Svelte/Angular → 裝對應套件,參考 api-*.md
├── 純 HTML / 靜態頁 → CDN ESM import 或 iconify
├── 要做 icon picker (數百 icon 預覽) → 參考 performance.md 的 dynamic import
└── 評估替代方案 → 參考 comparison.md,給出建議與 trade-off
```

## 與其他 skill 的關係

- **[shadcn](../shadcn/SKILL.md)**：shadcn 預設 icon library 是 lucide。本 skill 提供完整 lucide 參考；shadcn 規則中的 icon 用法（`data-icon`、不自加 size class）一併適用。
- **[tailwind](../tailwind/SKILL.md)**：用 Tailwind 工具類別（`size-*`、`text-*`）控制 icon 樣式時,需先確認專案是 v3 還是 v4 token 系統。
- **[frontend-design](../frontend-design/SKILL.md)** / **[impeccable](../impeccable/SKILL.md)**：UI 設計 / 打磨階段檢視 icon 是否一致（size 等級、stroke 粗細、對齊）。
- **[gsap](../gsap/SKILL.md)**：icon 動畫（旋轉、顏色 tween、stroke 路徑）走 gsap 技能。

## 工作流程

1. **確認框架與環境**：React / Vue / Svelte / Angular / Vanilla？建置工具（Vite / Next / Nuxt / SvelteKit / CRA）？
2. **安裝套件**：依框架對應 `npm install <package>`。參考 [install.md](references/install.md)。
3. **選 icon**：到 <https://lucide.dev/icons> 搜尋,確認命名（PascalCase、連字號轉駝峰）。參考 [naming.md](references/naming.md)。
4. **import 並使用**：直接命名 import、套上 className 或 props。參考對應框架的 api-*.md。
5. **客製化**（顏色、size、stroke）：用 className + 設計系統 token；需要改 strokeWidth 等深層客製化看 [customization.md](references/customization.md)。
6. **bundle / 效能檢查**（必要時）：用 `rollup-plugin-visualizer` 或 `next build --profile` 確認 icon 沒被整包拉進來。參考 [performance.md](references/performance.md)。
7. **驗證**：實際 build + 跑頁面,確認 icon 顯示、顏色 / 大小與設計稿一致。

## 產出要求

- **新增 icon 套件評估**：說明選 / 不選 Lucide 的理由、對照表（授權、bundle、樹搖支援、社群）、給出建議。
- **新增 icon 到專案**：列安裝指令、實際 import 程式碼、套用到的檔案位置,確認是命名 import（不是 `import * as`）。
- **icon 客製化**：說明為何需要客製（視覺一致 / 設計稿差異）、props 設定、是否影響 tree-shaking。
- **icon 套件遷移**：列出對照命名表、給出 codemod 或手動替換計畫。
- **icon 效能優化**：給出目前 bundle 測量、優化手段（dynamic import / icon-picker 模式）、預期 bundle 改善。

## 授權

Lucide 使用 ISC License,允許商業使用、修改、散佈。完整條款：<https://github.com/lucide-icons/lucide/blob/main/LICENSE>
