# 效能、Tree-shaking 與 Dynamic Import

## 預設情境：Tree-shaking 已足夠

Lucide 採用「每個 icon 獨立 export」設計,搭配 ES Modules,named import 會自動 tree-shake：

```tsx
// 最終 bundle 只包含 Search,不會拉整包
import { Search } from 'lucide-react';
```

**實際打入 bundle 的 icon 數 = 你 import 的數量。** 平均單 icon 約 0.5-1 KB gzip,30 個 icon 大概 15-30 KB,對多數專案不是問題。

## 驗證 tree-shaking 有運作

### Vite / esbuild

```bash
npm run build
npx vite-bundle-visualizer
# 或
npx rollup-plugin-visualizer
```

檢查產物：搜 `lucide-react`,只應看到你實際 import 的 icon 路徑,不是整個 index。

### Next.js

```bash
ANALYZE=true npm run build
```

（需先裝 `@next/bundle-analyzer` 並在 next.config.js 設定）

### Webpack

用 `webpack-bundle-analyzer`,檢查 `lucide-react` chunk 大小。

## 危險 pattern（會破壞 tree-shaking）

### 1. wildcard import

```tsx
// 整包 1500+ icon 全部拉進來
import * as Icons from 'lucide-react';

<icons.search />  // 或類似動態存取
```

### 2. 字串索引

```tsx
// 即使是 named import,動態組字串會讓 bundler 無法靜態分析
import { Search, User } from 'lucide-react';
const iconName = someVar; // 'Search' | 'User'
const Icon = Icons[iconName]; // 整包
```

> 只有當**所有可能的字串都明確列舉**時,bundler 才能 tree-shake。動態組字串（特別是來自 API、URL、localStorage）一律整包。

### 3. dynamic import 路徑不固定

```tsx
const Icon = await import(`lucide-react/dist/icons/${name}`);
```

> 除非用 build-time 的 icon registry（見下節 IconPicker 模式）,否則不建議。

## IconPicker / 大量 icon 預覽

如果產品需要 icon picker（讓使用者從數百 icon 挑選）:

### 解法 A：Dynamic import + 預先分檔

Lucide 內部每個 icon 是獨立檔案（`lucide-react/dist/icons/search.js` 等）。可寫 build script 預先掃描需要的 icon,產出小 chunk：

```js
// build-icons.js
import { icons } from 'lucide-react';
import fs from 'fs';

const iconNames = Object.keys(icons);
fs.writeFileSync(
  'src/generated/icon-names.json',
  JSON.stringify(iconNames)
);
```

執行期：

```tsx
import iconNames from './generated/icon-names.json';

const IconPicker = () => {
  const [icons, setIcons] = useState<Record<string, any>>({});
  useEffect(() => {
    Promise.all(
      iconNames.map(name =>
        import(`lucide-react/dist/icons/${kebab(name)}.js`)
          .then(mod => [name, mod.default] as const)
      )
    ).then(pairs => setIcons(Object.fromEntries(pairs)));
  }, []);
  // ...
};
```

> 這個 pattern 第一次載入會 fetch 一批小 chunk,適合 icon picker。

### 解法 B：Iconify（替代方案）

若「需要數千 icon 動態顯示」是常態,改用 [Iconify](https://iconify.design)：

```tsx
import { Icon } from '@iconify/react';
<Icon icon="lucide:search" />
```

Iconify 用 on-demand API + 快取,初次使用時 fetch,之後用 cache。對 icon picker 友善。**但**：多一個網路依賴,且 SSR 需處理。

### 解法 C：保留 Lucide 靜態 import,但只列舉常用 icon

大多數 app 真正用到的 icon < 50 個,icon picker 場景也不需要全 1500+：

```ts
// src/lib/common-icons.ts
export { Search, User, Settings, ChevronRight, /* ... 30 個 */ } from 'lucide-react';
```

icon picker 只在這 30 個之間挑,完全不犧牲 tree-shaking。

## SSR / Hydration 成本

Lucide 是純 SVG,SSR 會把 SVG inline 進 HTML,client hydrate 時對照節點。**沒有額外 JS 執行成本**（icon 元件本身已是 SVG DOM）。

```tsx
// SSR 產出
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor">
  <circle cx="11" cy="11" r="8" />
  <path d="m21 21-4.3-4.3" />
</svg>
```

對 bundle size 與 LCP / TBT 影響極低。

## 圖片 vs Icon

不是所有「小圖」都該用 icon 套件：

| 情境 | 用 icon 套件 | 用圖片 |
|------|------------|--------|
| UI 控制（按鈕、導航） | ✅ | — |
| 裝飾性 icon | ✅ | — |
| 品牌 logo | — | ✅（SVG / PNG） |
| 場景插畫 | — | ✅（SVG illustration） |
| 表情 / 貼圖 | — | ✅（圖檔） |
| 多色 / 漸層 icon | ⚠️（要客製） | ✅（圖檔） |

## 監控 bundle 變化

可在 CI 加 budget：

```js
// scripts/check-bundle-size.js
import fs from 'fs';
const stats = fs.statSync('dist/assets/index-*.js');
const maxKb = 200;
if (stats.size / 1024 > maxKb) {
  throw new Error(`Bundle 超過 ${maxKb} KB,請檢查 lucide 是否正確 tree-shake`);
}
```

或用 `bundlesize` 套件設定 PR check。

## 一句話總結

> 預設情境用 named import,Lucide 的 tree-shaking 已足夠。**只在真的做 icon picker 場景**才需要 dynamic import / Iconify 替代方案。
