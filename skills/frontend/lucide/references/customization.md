# 客製化（Props & Styling）

## 完整 props 表（以 React 為例,其他框架介面一致）

| Prop | 類型 | 預設 | 說明 |
|------|------|------|------|
| `size` | number \| string | 24 | 寬高（px） |
| `color` | string | `currentColor` | stroke 顏色,接受任何 CSS color（含 `var(--token)`） |
| `strokeWidth` | number | 2 | stroke 粗細 |
| `absoluteStrokeWidth` | boolean | false | 設 true 時 stroke 不隨 size 縮放,視覺粗細保持一致 |
| `className` | string | — | CSS class |
| `style` | CSSProperties | — | inline style |
| `fill` | string | `none` | 一般不需改,Lucide 預設 stroke-only |
| `aria-label` | string | — | 螢幕閱讀器名稱 |
| `aria-hidden` | boolean \| string | false | 設 true 對輔助技術隱藏 |
| `role` | string | `img` | SVG role |
| 其他 | — | — | 標準 SVG / HTML 屬性皆透傳（`id`、`tabIndex` 等） |

## Size 策略

### 預設 24px

Lucide 預設 `size=24`。但 Tailwind / shadcn 場景常用較小：

| 用途 | 建議 size | Tailwind class |
|------|----------|----------------|
| 與小字 (text-xs/sm) 同行 | 12-14 | `size-3`、`size-3.5` |
| 與中字 (text-base) 同行 | 16 | `size-4` |
| 與大字 (text-lg/xl) 同行 | 20 | `size-5` |
| 獨立大 icon / Hero | 32-48+ | `size-8` / `size-12` |

### 不用 size prop 的好處

直接給 className,搭配 Tailwind 設計系統,設計稿改 token 時 icon 會跟著變：

```tsx
// 不推薦：寫死 size
<Search size={16} />

// 推薦：跟設計系統 token
<Search className="size-4" />
```

## Color 策略

### 用 currentColor 跟著文字色

```tsx
<button className="text-blue-500">
  <Search className="size-4" /> {/* stroke 自動變藍 */}
</button>
```

### 在 hover / state 改色

```tsx
<Search className="size-4 text-muted-foreground group-hover:text-foreground transition-colors" />
```

### 用 CSS variable

```tsx
<Search style={{ color: 'var(--brand-accent)' }} className="size-4" />
```

## Stroke 粗細（strokeWidth）

預設 2。視覺一致性重要,不是每個 icon 都該改：

| 場景 | strokeWidth | 範例 |
|------|-------------|------|
| 一般 UI | 2（預設） | 導航列、toolbar |
| 大尺寸 / Hero | 1.5 | 登入頁裝飾 icon |
| 細緻 / 編輯器 | 1.5-2 | 程式碼編輯器 toolbar |
| 極簡設計 | 1 | 純文字排版旁的 icon |

```tsx
<Search className="size-4" strokeWidth={1.5} />
```

### absoluteStrokeWidth

預設 false。設 true 時,stroke 不會被 size 等比放大,維持視覺粗細一致。

```tsx
// size=48,strokeWidth=2,absoluteStrokeWidth=false
// → 視覺 stroke 會被放大到 4px（24 → 48 放大 2 倍）
<Search size={48} strokeWidth={2} />

// size=48,strokeWidth=2,absoluteStrokeWidth=true
// → 視覺 stroke 維持 2px
<Search size={48} strokeWidth={2} absoluteStrokeWidth />
```

> 大多數情境不需動此 prop,Lucide 設計師已挑過 24×24 時的視覺權重。**只在 icon 跨尺寸使用且發現大尺寸時 stroke 太粗時才開**。

## 旋轉 / 翻轉

```tsx
// 旋轉
<ChevronRight className="size-4 rotate-90" />

// 水平翻轉
<ArrowRight className="size-4 scale-x-[-1]" />

// 條件式旋轉（shadcn / Radix）
<ChevronDown className="size-4 transition-transform data-[state=open]:rotate-180" />
```

## Animation

```tsx
<Loader2 className="size-4 animate-spin" />
<Pulse className="size-4 animate-pulse" />
```

> 進階動畫（路徑繪製、scroll-driven）走 [gsap skill](../gsap/SKILL.md)。

## 顏色模式

Lucide 預設 stroke 為 `currentColor`,fill 為 `none`。要實心 icon：

```tsx
// 1. 單一顏色實心（用 fill,不走 stroke）
<Heart className="size-4 fill-red-500 text-red-500" />

// 2. outline + fill 雙色
<User className="size-4 fill-blue-100 text-blue-700" />
```

> 若經常需要實心版,評估是否改用其他套件（Heroicons solid / Material filled）。Lucide 哲學是「不混兩種風格」。

## 客製化 stroke-linecap / linejoin

```tsx
<Search style={{ strokeLinecap: 'square', strokeLinejoin: 'miter' }} className="size-4" />
```

> 強烈不建議改：會破壞 Lucide 視覺一致性,跨 icon 統一性會跑掉。

## 不要做的客製化

- **不要改 viewBox**：會破壞 grid 對齊。
- **不要包 `<div style={{ width: 24, height: 24 }}>` 限制 icon**：用 size prop 或 size-* class。
- **不要把 icon 顏色寫死成 hex**：用 `currentColor` 配 `text-*`,才有 dark mode / state 切換的彈性。
- **不要 import 整包再渲染子集**：破壞 tree-shaking,見 [performance.md](performance.md)。
