# 與 shadcn / Tailwind / 設計系統整合

## shadcn/ui

shadcn 預設 `iconLibrary: "lucide"`,並透過 `components.json` 設定：

```json
{
  "iconLibrary": "lucide"
}
```

### 規則（節錄自 shadcn skill）

完整規則見 [shadcn/rules/icons.md](../shadcn/rules/icons.md)。重點：

1. **icon 在 Button 等元件內,用 `data-icon`**：

   ```tsx
   // 錯誤
   <Button>
     <Search className="mr-2 size-4" />
     Search
   </Button>

   // 正確
   <Button>
     <Search data-icon="inline-start" />
     Search
   </Button>
   ```

2. **不手動加 sizing class**：

   ```tsx
   // 錯誤
   <DropdownMenuItem>
     <Settings className="mr-2 size-4" />
     Settings
   </DropdownMenuItem>

   // 正確（由 DropdownMenuItem 透過 CSS 處理間距與尺寸）
   <DropdownMenuItem>
     <Settings />
     Settings
   </DropdownMenuItem>
   ```

3. **icon 物件傳遞,不用字串**：

   ```tsx
   <Button onClick={...} icon={CheckIcon}>Done</Button>
   ```

### 切換 iconLibrary

若專案要從 lucide 換成 tabler / phosphor,在 `components.json` 改：

```json
{
  "iconLibrary": "tabler"
}
```

shadcn 的元件內部會改用 `@tabler/icons-react`。本 skill 仍可當作「icon 概念」參考,但 import 寫法會變。

## Tailwind CSS

### 用 utility class 控制 size

```tsx
<Search className="size-3" />  // 12px
<Search className="size-4" />  // 16px
<Search className="size-5" />  // 20px
<Search className="size-6" />  // 24px
```

> Tailwind 預設 `size-*` 是 w+h 一起設,等於 Lucide 期待的方形 SVG。

### 用 text-* 控制顏色

```tsx
<Search className="text-foreground" />
<Search className="text-muted-foreground" />
<Search className="text-blue-500 dark:text-blue-400" />
```

> Lucide 預設 `stroke="currentColor"`,所以文字色直接影響 icon 顏色。

### Design Token 整合（Tailwind v4）

```css
/* app.css */
@theme {
  --color-icon-default: var(--color-foreground);
  --color-icon-muted: var(--color-muted-foreground);
  --color-icon-accent: var(--color-primary);
}
```

```tsx
<Search className="size-4 text-icon-default" />
<Search className="size-4 text-icon-accent" />
```

Tailwind v3 同樣可在 `tailwind.config.ts` 定義 token。

## 設計系統：建立 icon 等級

設計稿常見的 icon size 系統：

| 等級 | size | 用途 | 範例 |
|------|------|------|------|
| `xs` | 12px | 表格內、tag 旁 | `<Search className="size-3" />` |
| `sm` | 16px | 按鈕、toolbar、input 旁 | `<Search className="size-4" />` |
| `md` | 20px | 導航、tab | `<Search className="size-5" />` |
| `lg` | 24px | 卡片標題、區塊 | `<Search className="size-6" />` |
| `xl` | 32px+ | Hero、empty state | `<Search className="size-8" />` |

> 同一畫面 icon size 變化不應超過 3 級,否則視覺會亂。

## Wrapper 元件：包裝成團隊慣用 API

```tsx
// src/components/Icon.tsx
import { icons, type LucideIcon } from 'lucide-react';
import { cn } from '@/lib/utils';

type IconName = keyof typeof icons;

interface IconProps {
  name: IconName;
  size?: 'xs' | 'sm' | 'md' | 'lg' | 'xl';
  className?: string;
}

const sizeMap = {
  xs: 'size-3',
  sm: 'size-4',
  md: 'size-5',
  lg: 'size-6',
  xl: 'size-8',
} as const;

export function Icon({ name, size = 'sm', className }: IconProps) {
  const LucideIcon = icons[name] as LucideIcon;
  return <LucideIcon className={cn(sizeMap[size], className)} />;
}
```

```tsx
<Icon name="Search" />
<Icon name="ChevronRight" size="md" className="text-muted-foreground" />
```

> **注意**：這個 wrapper 用了動態索引（`icons[name]`）,會破壞 tree-shaking。改法：把所有可能用到的 icon 預先 import：

```tsx
import { Search, ChevronRight, /* ... 列舉 */, type LucideIcon } from 'lucide-react';

const iconMap = { Search, ChevronRight, /* ... */ } as const;
type IconName = keyof typeof iconMap;

export function Icon({ name, size = 'sm', className }: { name: IconName; size?: ...; className?: string }) {
  const LucideIcon = iconMap[name];
  return <LucideIcon className={cn(sizeMap[size], className)} />;
}
```

這樣 team 用 `Icon` 元件時,bundler 仍能 tree-shake。

## 與 dark mode 整合

Lucide 預設 stroke 跟 `currentColor`,所以只要 `text-*` 用 design token,dark mode 自動切換：

```tsx
<Search className="size-4 text-foreground dark:text-foreground" />
// 或直接靠 design token
<Search className="size-4 text-foreground" />
```

Tailwind v4 的 `@theme` token 在 dark mode 通常有對應變體（`dark:` 或 media query）。

## Icon + text 對齊

icon 與相鄰文字的 baseline 對齊是常見痛點：

```tsx
// 用 flex 對齊
<div className="flex items-center gap-2">
  <Search className="size-4" />
  <span>搜尋</span>
</div>
```

> Lucide 24×24 設計,文字 default 行高（line-height: 1.5）配 size-4 / size-5 icon 視覺最齊。

## 在 shadcn 之外的設計系統

- **Mantine**：內建 `IconSearch` 等用 Tabler,不是 Lucide。要用 Lucide 直接 import 即可。
- **Chakra UI**：有 `@chakra-ui/icons` 用舊版,建議改用 Lucide + `Icon` wrapper。
- **Ant Design**：內建 icon 用自家 SVG。混用 Lucide 需手動 import。
- **MUI**：用 `@mui/icons-material`（Material）。若堅持 Lucide,直接 import 不衝突。

## 一句話總結

> shadcn 預設 Lucide + 嚴格 icon 規則（`data-icon`、不手動 size class）,Tailwind 用 `text-*` / `size-*` 控制樣式,icon 跟 design token 走,設計稿改 token 時 icon 自動跟著變。
