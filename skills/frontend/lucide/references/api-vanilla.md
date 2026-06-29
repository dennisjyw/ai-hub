# Vanilla JS API（lucide）

> 適用於純 HTML 頁面、靜態網站、或不想引入框架的場景。

## 安裝

```bash
npm install lucide
```

## 兩種使用模式

### 模式 A：createIcons() 把 `<i data-lucide="...">` 替換為 SVG

```html
<!doctype html>
<html>
<head>
  <script type="module">
    import { createIcons, icons } from 'lucide';
    // 把所有 <i data-lucide="..."> 替換為實際 SVG
    createIcons({ icons });
  </script>
</head>
<body>
  <i data-lucide="search"></i>
  <i data-lucide="chevron-right"></i>
  <i data-lucide="user" class="size-4"></i>
</body>
</html>
```

> 第一次呼叫 `createIcons()` 處理當前 DOM。新增的 icon 元素需再呼叫一次,或用 MutationObserver 自動觀察（見下方 `nameAttr` / 進階選項）。

### 模式 B：動態呼叫 createElement 取得 SVG 節點字串

```js
import { createElement, Search, ChevronRight } from 'lucide';

const svg = createElement(Search);
document.getElementById('search-container').innerHTML = svg;
```

## createIcons 選項

```js
createIcons({
  icons: { Search, ChevronRight },     // 註冊可用 icon
  nameAttr: 'data-lucide',              // 偵測的屬性名
  attrs: {},                            // 套到每個 SVG 的預設屬性
  // classList 不需設定,直接吃原本元素上的 class
});
```

> 如果用 `icons: { Search, ChevronRight }` 註冊子集,可以限制實際可被替換的 icon（節省記憶體）。

## 自動觀察 DOM（單頁應用 / 動態新增）

需手動加 MutationObserver 或在新增 icon 後再呼叫 createIcons()：

```js
import { createIcons, icons } from 'lucide';

function renderIcons() {
  createIcons({ icons });
}
renderIcons();

// 動態新增 icon 後
document.body.insertAdjacentHTML('beforeend', '<i data-lucide="x"></i>');
renderIcons();
```

## CDN（不建置）

```html
<script src="https://unpkg.com/lucide@latest"></script>

<i data-lucide="search"></i>
<i data-lucide="chevron-right" class="size-4"></i>

<script>
  lucide.createIcons();
</script>
```

> 線上 demo 與簡單靜態頁適用。生產建議走 npm。

## TypeScript

`createIcons` 與 `createElement` 都有型別。Icon 本身是 `IconNode`（`[string, Record<string, string>][]`）格式。

## 不可用情境

- 想用於 React Native：請改用 `react-native-svg`。
- 需要 SSR + 大量 icon：用框架版本（`lucide-react` / `lucide-vue-next` 等）inline 進 HTML。
