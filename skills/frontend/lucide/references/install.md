# 安裝指令

依框架對應的 npm package。所有套件版本號對齊,可同步升級。

## React（Vite / Next.js / Remix / CRA）

```bash
npm install lucide-react
# 或 pnpm add lucide-react
# 或 yarn add lucide-react
# 或 bun add lucide-react
```

```tsx
import { Search, ChevronRight } from 'lucide-react';

<Search className="size-4" />
<ChevronRight className="text-muted-foreground" />
```

## Vue 3

```bash
npm install lucide-vue-next
```

```vue
<script setup>
import { Search, ChevronRight } from 'lucide-vue-next';
</script>

<template>
  <Search class="size-4" />
  <ChevronRight class="text-muted-foreground" />
</template>
```

## Vue 2

```bash
npm install lucide-vue
```

## Svelte / SvelteKit

```bash
npm install lucide-svelte
```

```svelte
<script>
  import { Search, ChevronRight } from 'lucide-svelte';
</script>

<Search class="size-4" />
<ChevronRight class="text-muted-foreground" />
```

## Angular

```bash
npm install lucide-angular
```

在 standalone component：

```ts
import { LucideAngularModule, Search, ChevronRight } from 'lucide-angular';

@NgModule({
  imports: [LucideAngularModule.pick({ Search, ChevronRight })],
})
export class AppModule {}
```

```html
<i-lucide name="search" class="size-4"></i-lucide>
<i-lucide name="chevron-right"></i-lucide>
```

## Vanilla JS（任何框架或純 HTML）

```bash
npm install lucide
```

```js
import { createIcons, Search, ChevronRight } from 'lucide';

createIcons({ icons: { Search, ChevronRight } });
```

或以 data 屬性驅動：

```html
<i data-lucide="search"></i>
<i data-lucide="chevron-right"></i>
```

```js
import { createIcons, icons } from 'lucide';
createIcons({ icons });
```

> Vanilla 模式會把 `<i data-lucide="search">` 替換成實際 SVG。可用 `nameAttr` / `attrs` / `classes` 等選項自訂。詳見 vanilla API。

## CDN（不建置,直接用於 HTML 練習 / Demo）

```html
<script src="https://unpkg.com/lucide@latest"></script>
<i data-lucide="search"></i>
<script>
  lucide.createIcons();
</script>
```

> 線上 demo / 靜態頁適用。生產環境建議走 npm 套件以利 tree-shaking。

## 實驗性 / Draft icon

```bash
npm install @lucide/lab
```

與主套件相同 API,但 icon 仍在草案階段、未來可能改名或移除。**生產環境避免使用**。

## 升級策略

- **小版號**（0.x.y → 0.x.z）：icon 微調、bug 修正,通常無 breaking change。
- **次版號**（0.x → 0.y）：可能新增 / 棄用 icon,需跑 `npx lucide-codemod`（若官方有提供）或手動對照。
- **大版號**（x.0）：breaking 機率較高,需詳閱 changelog。

```bash
# 查看最新版本
npm view lucide-react version

# 升級
npm install lucide-react@latest
```

## TypeScript

所有官方套件皆隨附完整 `.d.ts`,icon 名稱、props 都有型別。不需額外裝 `@types/*`。

## SSR 注意事項

- **Next.js App Router / Nuxt / SvelteKit**：icon 元件是純 client component,SSR 會 inline 渲染 SVG,無 hydration 問題。
- **Astro**：若使用 `client:load` / `client:visible`,icon 會在 client 端 hydrate；用 `client:idle` 較省。
- **純 SSR（無 client JS）**：lucide 會把 SVG inline 進 HTML,完全 server-side 渲染,沒問題。
