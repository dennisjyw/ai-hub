---
name: tailwind
description: 當使用者要建立 Tailwind CSS 設計系統、遷移至 v4、實作設計令牌（design tokens）、建立元件庫，或需要精緻化現有 Tailwind UI 時使用。涵蓋 v3/v4 版本。
---

# Tailwind CSS

建立、遷移與打磨 Tailwind CSS 設計系統。

## 何時使用

- 建立新的 Tailwind v4 設計系統（CSS-first 配置）
- 從 v3 遷移至 v4
- 實作設計令牌（design tokens）與主題系統
- 建立元件庫與標準化 UI 模式
- 精緻化現有 Tailwind UI（微調間距、配色、層級）

## 核心能力

| 能力 | 適用版本 | 觸發關鍵詞 |
|------|---------|-----------|
| 設計系統建立 | v4 | 「建立設計系統」、「component library」 |
| 版本遷移 | v3→v4 | 「升級 Tailwind」、「migrate to v4」 |
| 視覺打磨 | v3/v4 | 「調整樣式」、「UI 太粗糙」、「精緻化」 |

## 子技能

- **[skills/polish.md](skills/polish.md)** - UI 視覺打磨（間距、配色、層級微調）

## v4 關鍵變更

| v3 模式 | v4 模式 |
|---------|---------|
| `tailwind.config.ts` | `@theme` in CSS |
| `@tailwind base/components/utilities` | `@import "tailwindcss"` |
| `darkMode: "class"` | `@custom-variant dark` |
| `theme.extend.colors` | `@theme { --color-*: value }` |

## 工作流程

### 設計系統建立（v4）

1. 建立 CSS-first 配置（`@import "tailwindcss"`）
2. 定義 `@theme` 設計令牌（colors、spacing、radius、animations）
3. 使用 CVA（Class Variance Authority）建立元件變體
4. 實作深色模式（`@custom-variant dark`）
5. 建立基礎元件（Button、Card、Input、Dialog）

### 視覺打磨

參見 [skills/polish.md](skills/polish.md)。

## 產出要求

- 設計系統：說明令牌層級（brand → semantic → component）
- 遷移：提供檢查清單與 breaking changes 說明
- 打磨：說明每個調整解決的視覺問題

## References

- `references/v4-migration.md` - v3 到 v4 完整遷移指南
- `references/design-tokens.md` - 設計令牌最佳實踐
- `references/component-patterns.md` - 元件模式（CVA、Compound Components）
