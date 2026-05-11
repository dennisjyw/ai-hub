# Tailwind v3 到 v4 遷移指南

## 主要變更

| v3 Pattern | v4 Pattern |
|------------|------------|
| `tailwind.config.ts` | `@theme` in CSS |
| `@tailwind base/components/utilities` | `@import "tailwindcss"` |
| `darkMode: "class"` | `@custom-variant dark` |
| `theme.extend.colors` | `@theme { --color-*: value }` |
| `require("tailwindcss-animate")` | CSS `@keyframes` in `@theme` |

## 遷移檢查清單

- [ ] 刪除 `tailwind.config.ts`，改用 CSS `@theme`
- [ ] 更新 `@tailwind` 指令為 `@import "tailwindcss"`
- [ ] 將顏色定義移至 `@theme { --color-*: value }`
- [ ] 使用 `@custom-variant dark` 替代 `darkMode: "class"`
- [ ] 將 `@keyframes` 移至 `@theme` 區塊內
- [ ] 使用 `size-*` 替代 `h-* w-*`
- [ ] 移除 `forwardRef`（React 19 直接傳遞 ref）

## 常見問題

### 顏色變數引用

```css
/* v3 */
@apply bg-blue-500;

/* v4 */
@apply bg-primary; /* 使用 semantic tokens */
```

### 自定義 Utilities

```css
/* v4 使用 @utility */
@utility line-t {
  @apply relative before:absolute before:top-0 before:-left-[100vw] before:h-px before:w-[200vw] before:bg-gray-950/5;
}
```
