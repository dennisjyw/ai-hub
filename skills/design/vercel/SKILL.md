---
name: vercel-design
description: 當使用者要以 Vercel 設計語言製作 UI、設計系統、landing page、dashboard 或元件時使用。涵蓋色彩、字型、按鈕、卡片、表單、間距、圓角、陰影等完整 token 體系，支援 light/dark 雙主題。
---

# Vercel Design System

基於 Vercel 官方設計語言的完整設計規範。涵蓋色彩、排版、元件、間距與 elevation 等 token。

## 載入策略

- 完整設計預覽（Light）：讀 [references/vercel-design.md](references/vercel-design.md)
- 完整設計預覽（Dark）：讀 [references/vercel-design.dark.md](references/vercel-design.dark.md)

## 設計原則

- **極簡**：大量留白、無裝飾性元素、內容優先
- **高對比**：黑底白字或白底黑字，輔助色僅用於點綴
- **一致性**：統一的 spacing、radius、shadow 層級
- **雙主題**：同一套 token 結構，light/dark 只切換數值

## 色彩系統

### Primary

| Token | Light | Dark | 用途 |
|-------|-------|------|------|
| `--black` | `#171717` | `#ededed` | 主要文字、標題 |
| `--white` | `#ffffff` | `#0a0a0a` | 頁面背景 |
| `--true-black` | `#000000` | `#000000` | Console 文字 |

### Workflow Accents

| Token | 色值 | 用途 |
|-------|------|------|
| `--develop-blue` | `#0a72ef` | 開發流程 |
| `--preview-pink` | `#de1d8d` | Preview 部署 |
| `--ship-red` | `#ff5b4f` | 發布到 production |

### Console Colors

| Token | 色值 | 用途 |
|-------|------|------|
| `--console-blue` | `#0070f3` | Syntax 藍 |
| `--console-purple` | `#7928ca` | Syntax 紫 |
| `--console-pink` | `#eb367f` | Syntax 粉 |

### Neutral Scale

| Token | Light | Dark | 用途 |
|-------|-------|------|------|
| `--gray-50` | `#fafafa` | `#111111` | 微底色 |
| `--gray-100` | `#ebebeb` | `#2a2a2a` | 邊框、分隔線 |
| `--gray-400` | `#808080` | `#666666` | Placeholder |
| `--gray-500` | `#666666` | `#808080` | 輔助文字 |
| `--gray-600` | `#4d4d4d` | `#a0a0a0` | 次要文字 |

### Interactive

| Token | 色值 | 用途 |
|-------|------|------|
| `--link-blue` | `#0072f5` | 連結 |
| `--focus-blue` | `hsl(212,100%,48%)` | Focus ring |
| `--badge-bg` | `#ebf5ff` | Pill badge 底色 |
| `--badge-text` | `#0068d6` | Pill badge 文字 |

## 字型

| 字型 | 用途 |
|------|------|
| `Geist` | 主要 sans-serif |
| `Geist Mono` | 程式碼、mono label |

### 排版層級

| 名稱 | 大小 | 粗細 | 行高 | 字距 | 用途 |
|------|------|------|------|------|------|
| Display Hero | 48px | 600 | 1.00 | -2.4px | Hero 標題 |
| Section Heading | 40px | 600 | 1.20 | -2.4px | 區塊標題 |
| Sub-heading | 32px | 600 | 1.25 | -1.28px | 副標題 |
| Card Title | 24px | 600 | 1.33 | -0.96px | 卡片標題 |
| Card Title Light | 24px | 500 | 1.33 | -0.96px | 輕量卡片標題 |
| Body Large | 20px | 400 | 1.80 | normal | 大段內文 |
| Body Medium | 16px | 500 | 1.50 | — | 導覽、強調文字 |
| Body Semibold | 16px | 600 | 1.50 | -0.32px | Active 狀態 |
| Button / Link | 14px | 500 | 1.43 | — | 按鈕與連結 |
| Caption | 12px | 500 | 1.33 | — | 註解、小標籤 |
| Mono Body | 16px | 400 | 1.50 | — | 程式碼區塊 |
| Mono Label | 12px | 500 | 1.00 | uppercase | Mono 標籤 |
| Micro Badge | 7px | 700 | 1.00 | uppercase | 徽章 |

## 按鈕

### Primary Dark

背景 `--black`、文字 `--white`、padding `10px 20px`、radius `6px`、font 14px/500。hover 時 opacity 0.85。

```css
.btn-primary {
  background: var(--black);
  color: var(--white);
  padding: 10px 20px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 500;
  transition: opacity 0.15s;
}
.btn-primary:hover { opacity: 0.85; }
```

### Ghost / Shadow

背景 `--white`、文字 `--black`、使用 `--shadow-ring-light` 邊框效果。hover 時升級為 `--shadow-ring`。

```css
.btn-ghost {
  background: var(--white);
  color: var(--black);
  padding: 10px 20px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 500;
  box-shadow: var(--shadow-ring-light);
  transition: box-shadow 0.15s;
}
.btn-ghost:hover { box-shadow: var(--shadow-ring); }
```

### Pill Badge

小標籤型按鈕，`--badge-bg` 底色、`--badge-text` 文字、padding `4px 10px`、radius `9999px`、font 12px/500。

### Workflow Pill

帶有 workflow 色彩的 pill：Develop Blue / Preview Pink / Ship Red，白字。

## 卡片

背景 `--white`、radius `8px`、padding `24px`。使用多層 shadow 系統：

| 層級 | Shadow | 說明 |
|------|--------|------|
| 預設 | `--shadow-card` | ring + 微浮起 |
| Hover | `--shadow-card-full` | ring + 浮起 + ambient + glow |

### 卡片結構

- **Badge**：Mono 12px/500 uppercase pill，置於頂部
- **標題**：20px/600，letter-spacing -0.8px
- **內容**：14px，`--gray-600` 色，行高 1.50

## 表單

### Input

無邊框設計，使用 shadow-ring 作為視覺邊界。padding `10px 12px`、radius `6px`、font 14px。

| 狀態 | Shadow |
|------|--------|
| Default | `--shadow-ring` |
| Focus | `0 0 0 2px var(--focus-blue)` |
| Error | `0 0 0 2px var(--ship-red)` |

### Label

14px/500，`--black` 色，margin-bottom `6px`。

### Textarea

同 Input 樣式，min-height `80px`，可垂直 resize。

## 間距系統

| Token | 值 | 常見用途 |
|-------|-----|---------|
| `2` | 2px | 極小間距 |
| `4` | 4px | 緊密間距 |
| `6` | 6px | 元素內部 |
| `8` | 8px | 小間距 |
| `12` | 12px | 中小間距 |
| `16` | 16px | 標準間距 |
| `32` | 32px | 區塊間距 |
| `40` | 40px | 大區塊間距 |

## 圓角

| 值 | 用途 |
|----|------|
| `2px` | Code span |
| `4px` | Small 元素 |
| `6px` | 按鈕、Input |
| `8px` | 卡片 |
| `12px` | 圖片 |
| `64px` | Tabs |
| `9999px` | Badge、Pill |

## Elevation（陰影層級）

| 層級 | 名稱 | CSS | 說明 |
|------|------|-----|------|
| 0 | Flat | `border: 1px solid var(--gray-100)` | 無陰影，純邊框 |
| 1 | Ring | `rgba(0,0,0,0.08) 0px 0px 0px 1px` | Shadow-as-border |
| 1b | Light Ring | `rgb(235,235,235) 0px 0px 0px 1px` | 較淺 ring |
| 2 | Card | Ring + `rgba(0,0,0,0.04) 0px 2px 2px 0px` + inner ring | 卡片預設 |
| 3 | Full Card | Card + `rgba(0,0,0,0.04) 0px 8px 8px -8px` + inner glow | Hover 狀態 |
| Focus | Focus Ring | `0 0 0 2px hsl(212,100%,48%)` | 無障礙焦點 ring |

## Dark Mode 差異

Dark mode 使用相同結構，僅切換數值：

| 屬性 | Light | Dark |
|------|-------|------|
| `--black` | `#171717` | `#ededed` |
| `--white` | `#ffffff` | `#0a0a0a` |
| `--gray-50` | `#fafafa` | `#111111` |
| `--gray-100` | `#ebebeb` | `#2a2a2a` |
| `--gray-400` | `#808080` | `#666666` |
| `--gray-500` | `#666666` | `#808080` |
| `--gray-600` | `#4d4d4d` | `#a0a0a0` |
| `--shadow-ring` | `rgba(0,0,0,0.08)` | `rgba(255,255,255,0.1)` |
| `--shadow-ring-light` | `rgb(235,235,235)` | `rgba(255,255,255,0.08)` |
| `--shadow-card` | 黑色基調 | 白色基調 + 深色 ambient |
| Nav bg | `rgba(255,255,255,0.85)` | `rgba(10,10,10,0.88)` |
| Divider | `var(--gray-100)` | `#2a2a2a` |
| Nav CTA | 黑底白字 | 白底黑字 |

## 元件清單

| 元件 | 說明 |
|------|------|
| Nav | sticky、blur 背景、brand + links + CTA |
| Hero | 居中大標題 + 副標 + 雙按鈕 |
| Section | 帶 mono label 編號 + 標題 + 內容 |
| Card | badge + title + description，shadow hover |
| Input | shadow-ring 邊框，focus/error 狀態 |
| Badge | pill 造型，mono 字型 |

## 執行流程

**先設計，後開發。** 每個新專案都必須先建立 DESIGN.md，確立設計系統後再寫程式碼。

### Step 1：生成 DESIGN.md

在專案根目錄建立 `DESIGN.md`，作為整個專案的設計 source of truth。以 Vercel 設計語言為預設，light/dark 雙主題同時準備。

使用下方模板（見 [DESIGN.md 模板](#designmd-模板)），根據專案需求調整：
- 色彩：預設使用 Vercel light/dark tokens，可依品牌需求覆蓋
- 字型：預設 Geist / Geist Mono，可替換為專案指定字型
- 間距、圓角、陰影：直接沿用 Vercel 體系
- 元件：列出專案會用到的元件清單

### Step 2：將 DESIGN.md 轉為程式碼

根據 DESIGN.md 的內容，生成對應的技術設定：

**Tailwind CSS（推薦）：**
```js
// tailwind.config.js — 從 DESIGN.md 讀取 token
module.exports = {
  theme: {
    extend: {
      colors: {
        background: 'var(--white)',
        foreground: 'var(--black)',
        muted: 'var(--gray-600)',
        border: 'var(--gray-100)',
        link: 'var(--link-blue)',
        accent: { develop: 'var(--develop-blue)', preview: 'var(--preview-pink)', ship: 'var(--ship-red)' },
      },
      fontFamily: {
        sans: ['Geist', 'system-ui', 'sans-serif'],
        mono: ['Geist Mono', 'ui-monospace', 'monospace'],
      },
      borderRadius: { sm: '4px', DEFAULT: '6px', md: '8px', lg: '12px', pill: '9999px' },
    },
  },
}
```

**CSS 變數：**
```css
/* globals.css — 直接從 DESIGN.md 複製 */
:root {
  --black: #171717;
  --white: #ffffff;
  --gray-50: #fafafa;
  --gray-100: #ebebeb;
  --gray-400: #808080;
  --gray-500: #666666;
  --gray-600: #4d4d4d;
  --link-blue: #0072f5;
  --focus-blue: hsl(212,100%,48%);
  --ship-red: #ff5b4f;
  --preview-pink: #de1d8d;
  --develop-blue: #0a72ef;
  --font-sans: 'Geist', system-ui, -apple-system, Arial, sans-serif;
  --font-mono: 'Geist Mono', ui-monospace, SFMono-Regular, monospace;
}

@media (prefers-color-scheme: dark) {
  :root {
    --black: #ededed;
    --white: #0a0a0a;
    --gray-50: #111111;
    --gray-100: #2a2a2a;
    --gray-400: #666666;
    --gray-500: #808080;
    --gray-600: #a0a0a0;
    --shadow-ring: rgba(255,255,255,0.1) 0px 0px 0px 1px;
    --shadow-ring-light: rgba(255,255,255,0.08) 0px 0px 0px 1px;
    --shadow-card: rgba(255,255,255,0.1) 0px 0px 0px 1px, rgba(0,0,0,0.2) 0px 2px 2px 0px;
    --shadow-card-full: rgba(255,255,255,0.12) 0px 0px 0px 1px, rgba(0,0,0,0.3) 0px 2px 2px 0px, rgba(0,0,0,0.2) 0px 8px 8px -8px;
  }
}
```

### Step 3：開發

有了 DESIGN.md 和對應的 CSS/Tailwind 設定後，才開始開發元件。開發過程中若需要調整設計，先更新 DESIGN.md，再同步到程式碼。

### 規則

- ❌ 不可跳過 DESIGN.md 直接寫 UI
- ❌ 不可使用 DESIGN.md 未定義的顏色或間距
- ✅ 所有設計決策記錄在 DESIGN.md
- ✅ 修改設計時先改 DESIGN.md 再改程式碼

## DESIGN.md 模板

以下為預設模板，直接複製到專案根目錄的 `DESIGN.md`。根據專案需求修改標記為 `<!-- CUSTOMIZE -->` 的區塊。

```markdown
# Design System

> Source of truth for all design decisions. Modify this file first, then sync to code.

## Fonts

| Token | Value | Usage |
|-------|-------|-------|
| `--font-sans` | `'Geist', system-ui, -apple-system, Arial, sans-serif` | Body, headings |
| `--font-mono` | `'Geist Mono', ui-monospace, SFMono-Regular, monospace` | Code, labels |

## Typography

| Name | Size | Weight | Line-height | Letter-spacing | Usage |
|------|------|--------|-------------|----------------|-------|
| Display Hero | 48px | 600 | 1.00 | -2.4px | Hero title |
| Section Heading | 40px | 600 | 1.20 | -2.4px | Section title |
| Sub-heading | 32px | 600 | 1.25 | -1.28px | Subtitle |
| Card Title | 24px | 600 | 1.33 | -0.96px | Card heading |
| Body Large | 20px | 400 | 1.80 | normal | Long text |
| Body Medium | 16px | 500 | 1.50 | — | Nav, emphasis |
| Body Semibold | 16px | 600 | 1.50 | -0.32px | Active state |
| Button / Link | 14px | 500 | 1.43 | — | Buttons, links |
| Caption | 12px | 500 | 1.33 | — | Metadata |
| Mono Label | 12px | 500 | 1.00 | uppercase | Mono labels |

## Colors — Light

| Token | Hex | Usage |
|-------|-----|-------|
| `--black` | `#171717` | Primary text, headings |
| `--white` | `#ffffff` | Page background |
| `--gray-50` | `#fafafa` | Subtle surface |
| `--gray-100` | `#ebebeb` | Borders, dividers |
| `--gray-400` | `#808080` | Placeholders |
| `--gray-500` | `#666666` | Tertiary text |
| `--gray-600` | `#4d4d4d` | Secondary text |
| `--link-blue` | `#0072f5` | Links |
| `--focus-blue` | `hsl(212,100%,48%)` | Focus ring |
| `--develop-blue` | `#0a72ef` | Dev workflow |
| `--preview-pink` | `#de1d8d` | Preview |
| `--ship-red` | `#ff5b4f` | Ship / error |
| `--badge-bg` | `#ebf5ff` | Badge surface |
| `--badge-text` | `#0068d6` | Badge text |

## Colors — Dark

| Token | Hex | Usage |
|-------|-----|-------|
| `--black` | `#ededed` | Primary text |
| `--white` | `#0a0a0a` | Page background |
| `--gray-50` | `#111111` | Subtle surface |
| `--gray-100` | `#2a2a2a` | Borders, dividers |
| `--gray-400` | `#666666` | Placeholders |
| `--gray-500` | `#808080` | Tertiary text |
| `--gray-600` | `#a0a0a0` | Secondary text |

## Shadows

| Level | Light | Dark |
|-------|-------|------|
| Ring | `rgba(0,0,0,0.08) 0px 0px 0px 1px` | `rgba(255,255,255,0.1) 0px 0px 0px 1px` |
| Ring Light | `rgb(235,235,235) 0px 0px 0px 1px` | `rgba(255,255,255,0.08) 0px 0px 0px 1px` |
| Card | Ring + `rgba(0,0,0,0.04) 0px 2px 2px` | Ring + `rgba(0,0,0,0.2) 0px 2px 2px` |
| Card Full | Card + `0px 8px 8px -8px` ambient | Card + `0px 8px 8px -8px` ambient |
| Focus | `0 0 0 2px hsl(212,100%,48%)` | same |

## Spacing

| Token | Value |
|-------|-------|
| `2` | 2px |
| `4` | 4px |
| `6` | 6px |
| `8` | 8px |
| `12` | 12px |
| `16` | 16px |
| `32` | 32px |
| `40` | 40px |

## Border Radius

| Value | Usage |
|-------|-------|
| `2px` | Code spans |
| `4px` | Small elements |
| `6px` | Buttons, inputs |
| `8px` | Cards |
| `12px` | Images |
| `64px` | Tabs |
| `9999px` | Badges, pills |

## Components

<!-- CUSTOMIZE: list the components your project needs -->

| Component | Status | Notes |
|-----------|--------|-------|
| Nav | ⬜ | Sticky, blur bg, brand + links + CTA |
| Hero | ⬜ | Centered title + subtitle + dual buttons |
| Card | ⬜ | Badge + title + description, shadow hover |
| Input | ⬜ | Shadow-ring border, focus/error states |
| Badge | ⬜ | Pill, mono font |

## Decisions

<!-- CUSTOMIZE: record design decisions as you go -->

| Date | Decision | Rationale |
|------|----------|-----------|
| — | Default to Vercel light/dark tokens | Clean, high-contrast, production-ready |
```
