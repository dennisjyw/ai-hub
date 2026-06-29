# 與其他 icon 套件對照

> 預設首選 Lucide。這個檔列出**什麼情境才考慮替代方案**,以及如何評估。

## 主流 icon 套件對照表

| 套件 | 風格 | Icon 數 | 授權 | 樹搖 | React 元件 | SSR | 動態載入 | 一句話定位 |
|------|------|--------|------|------|-----------|-----|----------|-----------|
| **Lucide** | stroke 2px 極簡 | 1,500+ | ISC | 完整 | `lucide-react` | OK | 需手動 dynamic | shadcn 預設,事實標準 |
| Heroicons | outline 24 + solid 24 | 300+ | MIT | 完整 | `@heroicons/react` | OK | OK | Tailwind 官方,兩套風格 |
| Tabler | stroke 2px | 4,500+ | MIT | 完整 | `@tabler/icons-react` | OK | OK | 冷門 icon 多,風格類 Lucide |
| Material Symbols | 4 種風格（outline/filled/rounded/sharp） | 3,000+ | Apache-2.0 | 完整 | `@mui/icons-material` 或 `material-symbols` | OK | OK | Material Design 專案 |
| Phosphor | 6 種權重 | 9,000+ | MIT | 完整 | `@phosphor-icons/react` | OK | OK | 想要不同視覺權重 |
| Iconoir | stroke 1.5px 法系 | 1,500+ | MIT | 完整 | `iconoir-react` | OK | OK | 與 Lucide 相似,法國設計 |
| Font Awesome | solid / regular / light / thin / duotone | 30,000+ | CC BY 4.0 (free) / PRO 付費 | 需命名 import | `react-icons` 包裹 | OK | 需設定 | 品牌字型、icon 數量王者 |
| react-icons | FA + Material + Hero + ... 統一 API | 看各家 | 看各家 | **各家不一** | 多套件合併 | OK | 需注意 | 想用單一 API 切換多家 |

## 何時考慮替代 Lucide

### 改用 Heroicons

- 已經在 Tailwind 生態,且**需要 outline / solid 兩套風格**。
- 設計稿明確標示 heroicons icon。
- 對 Lucide 1,500+ icon 數量不滿意（其實 Heroicons 較少,選擇反而精煉）。

### 改用 Tabler Icons

- 找不到 Lucide icon（Tabler 4,500+,冷門 icon 覆蓋率高）。
- 風格相近,語法類似,遷移成本低。

### 改用 Material Symbols

- 專案是 Material Design（MUI / Material Web / Angular Material）。
- 設計稿明確要 Material 風格。
- 需要 outline / filled / rounded / sharp 四種變體。

### 改用 Phosphor

- 想要 **6 種權重**（thin / light / regular / bold / fill / duotone）精細切換。
- 視覺需要更多變化,不想整套統一 stroke。

### 改用 Font Awesome

- 已有 FA 設計稿 / 品牌規範。
- 需要極大量 icon（FA 是商業字型 icon 之王）。
- 公司已買 FA Pro 授權。

### 改用 react-icons

- 想要單一 import 切換多家來源（`react-icons/fa`、`react-icons/md` 等）。
- **缺點：tree-shaking 行為因套件而異**,需逐套件驗證。

## Lucide vs Heroicons 細節對照

| 面向 | Lucide | Heroicons |
|------|--------|-----------|
| 視覺風格 | stroke 2px,極簡 | outline 1.5px + solid |
| 同一 icon 多版本 | 偶有（`Trash` vs `Trash2`） | 完整兩套（outline/solid） |
| Tailwind 整合 | `text-*` 直接吃 token | 同 |
| 客製化 | 完整 props | 完整 props |
| shadcn 預設 | 是 | 否（可改） |
| 維護 | 社群驅動,活躍 | Tailwind Labs 官方 |

**簡單選擇法**：
- 在 shadcn 專案 → Lucide
- 在純 Tailwind（非 shadcn）→ Heroicons 也很順
- 想要兩套風格切換 → Heroicons

## 從其他套件遷移到 Lucide

### 從 Font Awesome

| FA 類別 | Lucide 對應 |
|---------|------------|
| `fa-solid fa-search` | `Search` |
| `fa-regular fa-user` | `User` |
| `fa-brands fa-github` | `Github` |
| `fa-spinner` | `Loader2` |
| `fa-chevron-right` | `ChevronRight` |

完整對照表可用 [FA → Lucide codemod 工具](https://github.com/lucide-icons/lucide/tree/main/scripts)（查官方文件確認）。

### 從 Material Icons

| Material | Lucide |
|----------|--------|
| `search` | `Search` |
| `add_circle` | `CirclePlus` |
| `arrow_back` | `ArrowLeft` |
| `favorite` | `Heart` |
| `home` | `House` |

### 從 react-icons（FA / HI / MD 等）

```tsx
// 舊
import { FaSearch } from 'react-icons/fa';
<FaSearch />

// 新
import { Search } from 'lucide-react';
<Search />
```

通常 1:1 可換,需要時參考 [naming.md](naming.md) 對照。

## Bundle size 對照（粗略）

| 套件 | 平均單 icon gzip | 整包 gzip |
|------|-----------------|----------|
| Lucide | ~0.5-1 KB | ~150 KB（1500+ icon） |
| Heroicons | ~0.5 KB | ~30 KB（300 icon） |
| Tabler | ~0.4 KB | ~250 KB（4500 icon） |
| Font Awesome free | 看字型 / SVG | ~80 KB（subset） |

> Lucide 整包雖然 ~150 KB,但**有 tree-shaking,實際打入 bundle 的只有用到的 icon**。最終 app 通常只多 5-20 KB。

## 評估新專案時的決策流程

```
新專案需要 icon
├── 已在 shadcn 專案 → 100% 用 Lucide
├── 在 Tailwind / 純 React 專案
│   ├── 需要 solid + outline 切換 → Heroicons
│   └── 預設情境 → Lucide
├── 在 Material Design 專案 → Material Symbols
├── 設計稿指定 FA / Material / Heroicons → 沿用設計稿
├── icon 數量需求極大（>3000）→ Tabler / FA Pro
└── 不確定 → 用 Lucide,日後遷移成本不高
```
