# React API（lucide-react）

## 基本 import

```tsx
import { Search, ChevronRight, User, Settings, X } from 'lucide-react';

<Search />
<ChevronRight />
<User />
```

> **一定要用命名 import。** 不要用 `import * as Icons from 'lucide-react'` 再 `Icons.Search`——會失去 tree-shaking,bundle 整包拉進來。

## 基本 props

| Prop | 類型 | 預設 | 說明 |
|------|------|------|------|
| `size` | number \| string | 24 | 寬高（px） |
| `color` | string | `currentColor` | stroke 顏色,接受任何 CSS color |
| `strokeWidth` | number | 2 | stroke 粗細 |
| `className` | string | — | 套上 Tailwind / CSS 類別 |
| `style` | CSSProperties | — | inline style |
| `absoluteStrokeWidth` | boolean | false | 設 true 時 stroke 不隨 size 縮放,維持視覺粗細一致 |
| `onClick` | MouseEventHandler | — | 點擊事件 |
| `aria-label` / `aria-hidden` | string \| boolean | false | 無障礙 |
| 其他 | — | — | 所有 SVG 原生 props（`role`, `tabIndex` 等）皆透傳 |

```tsx
<Search size={16} className="text-muted-foreground" />
<ChevronRight size={20} color="#888" />
<Heart size={32} strokeWidth={1.5} />
```

## 用 Tailwind 控制樣式（推薦）

```tsx
<Search className="size-4" />
<Search className="size-5 text-blue-500" />
<Search className="size-6 text-foreground" />
```

Lucide 的 SVG 已經是 `fill="none"` `stroke="currentColor"`,所以：

- **`text-*` 控制顏色**（不用 `color` prop）
- **`size-*` 控制大小**（不用 `size` prop）
- **`stroke-*` 顏色**也跟著 `currentColor`

> shadcn 專案：放在 `Button` / `DropdownMenuItem` 等元件內時,**不另加** `size-4` / `mr-2`,改用 `data-icon="inline-start"` 等屬性（見 [shadcn icon 規則](../shadcn/rules/icons.md)）。

## 動態 / 條件式 icon

```tsx
import { ChevronRight, ChevronDown } from 'lucide-react';

function ExpandIcon({ open }: { open: boolean }) {
  return open ? <ChevronDown /> : <ChevronRight />;
}
```

## 渲染為按鈕 / 可互動元素

```tsx
<button onClick={onClose} aria-label="關閉">
  <X className="size-4" />
</button>
```

> 務必給 `<button>` 加 `aria-label` 或可見文字,icon 本身不該是唯一的 accessible name。

## 動畫 / 旋轉

```tsx
import { Loader2 } from 'lucide-react';

<Loader2 className="size-4 animate-spin" />
<ChevronDown className="size-4 transition-transform data-[state=open]:rotate-180" />
```

> 旋轉 / tween 等進階動畫見 [gsap skill](../gsap/SKILL.md)。

## 組合 icon（compound icon）

Lucide 沒有官方 compound icon 元件,但可以包裝：

```tsx
import { Github, Linkedin } from 'lucide-react';

const SocialIcon = {
  github: Github,
  linkedin: Linkedin,
} as const;

<SocialIcon.github className="size-5" />
```

或在 shadcn 場景下用 registry 模式,見 [shadcn skill](../shadcn/SKILL.md)。

## IconPicker（大量 icon 預覽）

若要在 UI 內讓使用者選 icon（數百個 icon 可挑選）：

```tsx
import { icons } from 'lucide-react';
const allIconNames = Object.keys(icons);
```

> 這個 pattern 會失去 tree-shaking（整包拉進來）。詳見 [performance.md](performance.md) 的 dynamic import 模式。

## 不可用情境

- 不支援 React 17 之前的 `createReactClass` 風格（已是歷史問題）。
- 在 React Native 環境請改用 `react-native-vector-icons` 或 SVG 直接 render,因為 `lucide-react` 依賴 SVG 元素（RN 需用 `react-native-svg`）。
