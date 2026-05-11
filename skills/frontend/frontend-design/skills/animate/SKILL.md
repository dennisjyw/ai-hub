---
name: animate
description: 當介面需要加入有目的的動畫、微互動、進場效果或狀態轉換，以提升理解、回饋或愉悅感時使用。不要為了動而動。支援 ReactBits 元件庫整合。
---

# Animate

為介面加入克制的動效，提升體驗而不干擾。

## 何時使用

- 需要改善互動回饋、狀態轉換、內容進場節奏
- 使用者說「加動效」、「讓頁面動起來」、「太靜了」
- 整合 ReactBits 元件庫的動畫元件

## 核心原則

- 動效是配角，內容是主角
- 讓頁面更自然、有層次，不讓使用者分心
- 尊重 `prefers-reduced-motion`

## 執行流程

1. **分析頁面結構** - 識別 Hero 標題、CTA 按鈕、卡片列表等關鍵元素
2. **選取動效類型** - 根據場景選擇文字動效、交互动效或背景動效
3. **克制配置** - 同一頁面背景動效最多 1 個，文字動效最多 2 種
4. **實作整合** - 使用 ReactBits 元件或自定義 CSS 動畫

## 動效優先級

| 元素類型 | 動效優先級 |
|---------|-----------|
| Hero 標題 / 主標語 | ⭐⭐⭐ 高 |
| CTA 按鈕 | ⭐⭐⭐ 高 |
| 卡片列表 / Feature Grid | ⭐⭐ 中 |
| 頁面背景 | ⭐⭐ 中 |
| 導航欄 | ⭐ 低（謹慎） |
| 正文段落 | ⭐ 低（通常不加） |

## 推薦元件庫

### ReactBits（推薦）

安裝方式：
```bash
npx jsrepo add https://reactbits.dev/ts/tailwind/<Category>/<ComponentName>
```

**文字動效**：SplitText、BlurText、GradientText、ShinyText
**交互动效**：FadeContent、BlurFade、ScrollReveal、Magnet
**背景動效**：Particles（低密度）、GridMotion、DotGrid

詳見 [references/reactbits-guide.md](references/reactbits-guide.md) 完整元件清單與搭配規則。

## 產出要求

- 說明選用的動效類型與解決的體驗問題
- 提供安裝命令與整合代碼
- 包含 `prefers-reduced-motion` 降級方案
- 標註調參建議（delay、duration、quantity）

## 參考資源

- [references/reactbits-guide.md](references/reactbits-guide.md) - ReactBits 元件詳細指南
- [references/animation-patterns.md](references/animation-patterns.md) - CSS 動畫模式與範例
