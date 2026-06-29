# Vue API（lucide-vue-next）

> Vue 3 用 `lucide-vue-next`,Vue 2 用 `lucide-vue`。本檔以 Vue 3 為主。

## 安裝

```bash
npm install lucide-vue-next
```

## 基本用法

```vue
<script setup>
import { Search, ChevronRight, User, Settings, X } from 'lucide-vue-next';
</script>

<template>
  <Search />
  <ChevronRight />
  <User class="size-4" />
  <Settings :size="20" color="#888" />
  <X :size="16" :stroke-width="1.5" />
</template>
```

## Props

| Prop | 類型 | 預設 | 說明 |
|------|------|------|------|
| `size` | number \| string | 24 | 寬高（px） |
| `color` | string | `currentColor` | stroke 顏色 |
| `stroke-width` | number | 2 | stroke 粗細（Vue 慣例用 kebab-case） |
| `class` | string | — | CSS class（Vue 慣例） |
| `style` | string \| object | — | inline style |
| `absolute-stroke-width` | boolean | false | stroke 不隨 size 縮放 |
| 事件 | — | — | 標準 DOM 事件皆透傳 |

## 用 Tailwind 控制（推薦）

```vue
<Search class="size-4 text-muted-foreground" />
<ChevronRight class="size-5 text-blue-500" />
```

## 動態切換

```vue
<script setup>
import { ref } from 'vue';
import { ChevronRight, ChevronDown } from 'lucide-vue-next';
const open = ref(false);
</script>

<template>
  <component :is="open ? ChevronDown : ChevronRight" class="size-4" />
</template>
```

## Nuxt SSR

- `lucide-vue-next` 在 Nuxt 3 預設 SSR 沒問題（SVG 會 inline 進 HTML）。
- 不需額外設定 `build.transpile`。

## 不可用情境

- 與 shadcn 整合：shadcn/ui 沒有 Vue 版本。如要在 Vue 專案做類似設計系統,改用 Reka UI / Radix Vue + 自己的 icon 規則。
