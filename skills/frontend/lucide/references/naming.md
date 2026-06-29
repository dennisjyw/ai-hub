# Icon 命名規則

## 基本規則

Lucide icon **PascalCase**,**無連字號**、**無底線**、**無前綴**（不像 Font Awesome 的 `fa-`、Material 的 `mat-`）。

| 視覺 | Icon 名稱 |
|------|----------|
| 搜尋放大鏡 | `Search` |
| 右上箭頭 | `ArrowUpRight` |
| 向下箭頭 | `ArrowDown` |
| 漢堡選單 | `Menu` |
| 關閉 X | `X` |
| 上一頁 | `ChevronLeft` |
| 設定齒輪 | `Settings` |
| 垃圾桶 | `Trash2`（不是 `Trash`） |

## 命名拆解

| 構成 | 範例 |
|------|------|
| 動作 | `Search`、`Trash`、`Edit`、`Copy`、`Download` |
| 方向 | `ArrowUp`、`ChevronLeft`、`MoveRight` |
| 物件 | `User`、`Mail`、`File`、`Folder` |
| 動作 + 方向 | `ArrowUpRight`、`MoveDownLeft` |
| 動作 + 物件 | `UserPlus`、`FilePlus`、`FileDown` |
| 物件 + 變體 | `Trash2`、`UserRound`、`MailOpen` |
| 狀態 | `Check`、`X`、`AlertCircle`、`Info` |
| 品牌 | `Github`、`Twitter`、`Slack`、`Figma`（社群提交） |

## 找不到 icon 的排查

### 1. 換關鍵字

官網 <https://lucide.dev/icons> 搜尋支援模糊比對：

- 想要「向上」找不到 → 試 `arrow-up`、`chevron-up`、`move-up`、`corner-up-left`
- 想要「關閉」找不到 → 試 `close`、`x`、`x-circle`、`circle-x`
- 想要「載入中」找不到 → 試 `loader`、`loading`、`rotate`、`refresh`

### 2. 查 alias

每個 icon 在 <https://lucide.dev/icons> 的頁面會列出 `Aliases`（舊名、別名）。例如 `Trash2` 早期叫 `Trash`。

### 3. 多個相近 icon

Lucide 同一概念常有 2-3 個變體,差異在細節幾何：

| 概念 | 變體 |
|------|------|
| Arrow | `ArrowRight`、`ArrowUpRight`、`MoveRight`、`ChevronRight`、`CornerDownRight` |
| User | `User`、`UserRound`、`UserCircle`、`UserSquare` |
| File | `File`、`FileText`、`FilePlus`、`FileX` |
| Bell | `Bell`、`BellRing`、`BellOff` |
| Heart | `Heart`、`HeartCrack`、`HeartHandshake`、`HeartOff`、`HeartPulse` |

挑選時以**視覺一致性**為優先——同一頁面的 icon 風格應統一（stroke 粗細、幾何比例、視覺權重）。

### 4. 真的沒有

- 翻 [Tabler Icons](https://tabler.io/icons)（icon 數更多,風格類似）。
- 從 Heroicons / Material 單獨抓 SVG。
- 用 [Lucide Lab](https://lucide.dev/lab) 的 draft icon（注意：實驗性,可能變動）。

## 不存在的 icon 名

常見誤猜,以下**不存在**或已更名：

| 誤猜 | 正確 |
|------|------|
| `SearchIcon` | `Search`（Lucide 不加 `Icon` 後綴） |
| `Close` | `X` |
| `Trash` | `Trash2` |
| `Spinner` | `Loader`、`Loader2`、`LoaderCircle` |
| `Hamburger` | `Menu` |
| `Cog` | `Settings` |
| `Bolt` | `Zap` |

## 建立 alias map（團隊 / 專案內統一）

若團隊有慣用命名（例如 `close` 而非 `x`）,可建立中央對照：

```ts
// src/lib/icons.ts
export {
  X as Close,
  Settings as Cog,
  Trash2 as Trash,
} from 'lucide-react';
```

或更精緻的 wrapper：

```ts
import { X as LucideX, Settings as LucideSettings } from 'lucide-react';

export const Close = LucideX;
export const Cog = LucideSettings;
```

> 注意：這個 pattern 讓團隊用熟悉的命名,但**寫了 alias 之後,新成員閱讀時需了解對照**,文件 / 註解要補上。

## 查詢輔助指令

```bash
# 用 npm registry 看所有 exports（簡略版）
npx -y lucide-list

# 或裝 lucide-helper CLI（社群工具）
```

> 目前沒有官方 CLI 列出所有 icon,最方便還是到 <https://lucide.dev/icons> 搜。
