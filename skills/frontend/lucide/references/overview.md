# Lucide 套件總覽

## 起源與定位

- 2019 年由 **Feather Icons** 社群分支出來,目標是擴充更多 icon、同時保留 Feather 的極簡風格。
- 採 **SVG + stroke** 設計,每個 icon 是 24×24 viewBox、stroke-width 預設 2。
- 截至目前（2025-2026）icon 數量已達 1,500+ 並持續成長。
- 是 **shadcn/ui 的預設 icon library**,也是 React / Vue / Svelte / Angular 生態中最常見的 icon 方案之一。

## 設計哲學

| 面向 | 取捨 |
|------|------|
| 視覺風格 | 極簡、幾何、stroke-based（不是 fill-based） |
| Grid | 24×24,icon 視覺邊界約 18-20px |
| Stroke | 2px、round linecap/linejoin,視覺一致 |
| 一致性 | 同一組 icon（arrow / chevron / user ...）的視覺權重與幾何比例需對齊 |
| 變體 | 不做 filled / outline 切換（不是 Material 雙風格哲學） |

## 套件家族

Lucide 提供多個官方套件,API 介面幾乎一致,只有 import 名稱不同：

| 套件名 | 用途 | 入口 |
|--------|------|------|
| `lucide-react` | React (Vite, Next.js, Remix, CRA) | 命名 import → React 元件 |
| `lucide-vue-next` | Vue 3 (Composition API) | 命名 import → Vue 元件 |
| `lucide-vue` | Vue 2 | 命名 import → Vue 元件 |
| `lucide-svelte` | Svelte / SvelteKit | 命名 import → Svelte 元件 |
| `lucide-angular` | Angular | 命名 import → Angular 元件 |
| `lucide` | Vanilla JS / 任何框架 | 命名 import → 純函式回傳 SVG 節點字串 |
| `@lucide/lab` | 實驗性 icon 與 draft | 命名 import → 與主套件一致 |

> 各套件皆由 monorepo 統一管理,更新節奏一致,版本號對齊。

## 與其他 icon 套件的差異（簡述）

| 套件 | 風格 | 授權 | 樹搖 | 選用情境 |
|------|------|------|------|----------|
| Lucide | stroke 2px 極簡 | ISC | 完整支援 | 預設首選 |
| Heroicons | 兩套（mini 24×24 solid / outline） | MIT | 完整支援 | Tailwind 生態,需要兩種風格切換 |
| Tabler Icons | stroke 2px,icon 數量多 | MIT | 完整支援 | 需要非常冷門的 icon |
| Material Symbols | filled / outline / rounded / sharp | Apache-2.0 | 變形 | Material Design 專案 |
| Font Awesome | 雙風格 + 多種重量 | CC BY 4.0（free）/ PRO 付費 | 部分 | 已有 FA 設計 / 需要品牌字型 |
| react-icons | 上游多家（FA / Material / Hero / ...） | 看各家 | 部分（依賴命名 import 是否 tree-shake） | 想用單一 API 切換多家來源 |

完整對照看 [comparison.md](comparison.md)。

## License

**ISC License**（等同於 MIT / BSD 寬鬆）：

- 商業使用 OK
- 修改 OK
- 散佈 OK
- 私人使用 OK
- 不需標註來源（但建議標）

詳見 <https://github.com/lucide-icons/lucide/blob/main/LICENSE>。

## 官方資源

- 官網 / Icon 搜尋：<https://lucide.dev>
- Icon 列表頁（每個 icon 有可複製的 import 範例）：<https://lucide.dev/icons>
- GitHub：<https://github.com/lucide-icons/lucide>
- Figma plugin：可在 Figma 直接搜尋並插入 icon
- VS Code / IntelliJ plugin：可在編輯器內搜尋
- `@lucide/lab` 實驗性 icon：<https://lucide.dev/lab>
