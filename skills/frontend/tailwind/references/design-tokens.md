# Tailwind v4 設計令牌

## Token 層級架構

```
Brand Tokens (抽象)
    └── Semantic Tokens (用途)
        └── Component Tokens (具體)

Example:
    oklch(45% 0.2 260) → --color-primary → bg-primary
```

## CSS-First 配置

```css
/* app.css - Tailwind v4 */
@import "tailwindcss";

@theme {
  /* Semantic color tokens using OKLCH */
  --color-background: oklch(100% 0 0);
  --color-foreground: oklch(14.5% 0.025 264);
  --color-primary: oklch(14.5% 0.025 264);
  --color-primary-foreground: oklch(98% 0.01 264);
  --color-secondary: oklch(96% 0.01 264);
  --color-muted: oklch(96% 0.01 264);
  --color-accent: oklch(96% 0.01 264);
  --color-destructive: oklch(53% 0.22 27);
  --color-border: oklch(91% 0.01 264);
  --color-ring: oklch(14.5% 0.025 264);

  /* Radius tokens */
  --radius-sm: 0.25rem;
  --radius-md: 0.375rem;
  --radius-lg: 0.5rem;
  --radius-xl: 0.75rem;

  /* Animation tokens */
  --animate-fade-in: fade-in 0.2s ease-out;
  --animate-fade-out: fade-out 0.2s ease-in;

  @keyframes fade-in {
    from { opacity: 0; }
    to { opacity: 1; }
  }
}

/* Dark mode */
@custom-variant dark (&:where(.dark, .dark *));

.dark {
  --color-background: oklch(14.5% 0.025 264);
  --color-foreground: oklch(98% 0.01 264);
  --color-primary: oklch(98% 0.01 264);
}
```

## 最佳實踐

- 使用 OKLCH 顏色空間獲得更好的感知均勻性
- 使用 `color-mix()` 建立透明度變體
- 使用 `@theme inline` 引用其他 CSS 變數
- 使用 `@theme static` 強制輸出所有 CSS 變數

## 深色模式

```css
@custom-variant dark (&:where(.dark, .dark *));

.dark {
  --color-background: oklch(14.5% 0.025 264);
  --color-foreground: oklch(98% 0.01 264);
}
```
