# Color & Contrast

## 色彩空間：使用 OKLCH

**不要再用 HSL。** 改用 OKLCH（或 LCH）。它在感知上是均勻的，也就是說相同的明度變化，看起來真的會一樣；不像 HSL 中，黃色 50% lightness 看起來很亮，但藍色 50% 卻很暗。

```css
/* OKLCH: lightness (0-100%), chroma (0-0.4+), hue (0-360) */
--color-primary: oklch(60% 0.15 250);      /* Blue */
--color-primary-light: oklch(85% 0.08 250); /* Same hue, lighter */
--color-primary-dark: oklch(35% 0.12 250);  /* Same hue, darker */
```

**關鍵洞見**：越接近白或黑時，越要降低 chroma（飽和度）。在極亮或極暗處維持高 chroma 會顯得刺眼。85% lightness 的淺藍，chroma 大約該是 0.08，而不是基礎色的 0.15。

## 建立可運作的色盤

### 帶色中性色陷阱

**純灰已經過時。** 請在所有 neutrals 中加入一點點品牌色調：

```css
/* Dead grays */
--gray-100: oklch(95% 0 0);     /* No personality */
--gray-900: oklch(15% 0 0);

/* Warm-tinted grays (add brand warmth) */
--gray-100: oklch(95% 0.01 60);  /* Hint of warmth */
--gray-900: oklch(15% 0.01 60);

/* Cool-tinted grays (tech, professional) */
--gray-100: oklch(95% 0.01 250); /* Hint of blue */
--gray-900: oklch(15% 0.01 250);
```

Chroma 只有 0.01，卻仍可被感知。它能讓品牌色與整體 UI 之間建立潛意識的一致性。

### Palette Structure

完整的系統需要：

| Role | Purpose | Example |
|------|---------|---------|
| **Primary** | 品牌、CTAs、關鍵動作 | 1 種顏色，3-5 階 |
| **Neutral** | 文字、背景、邊框 | 9-11 階色階 |
| **Semantic** | Success、error、warning、info | 4 種顏色，各 2-3 階 |
| **Surface** | Cards、modals、overlays | 2-3 個高度層級 |

**除非真的需要，否則略過 secondary/tertiary。** 多數 App 用一種 accent color 就足夠。加太多顏色只會增加決策疲勞與視覺噪音。

### 60-30-10 Rule（正確應用）

這條規則指的是**視覺權重**，不是像素數量：

- **60%**：中性背景、留白、基礎 surfaces
- **30%**：次要顏色，例如文字、邊框、非 active 狀態
- **10%**：Accent，例如 CTAs、highlight、focus states

常見錯誤是因為它是「品牌色」，就把 accent 到處用。Accent 之所以有效，正是因為它少。過度使用會摧毀它的力量。

## 對比與無障礙

### WCAG 要求

| Content Type | AA Minimum | AAA Target |
|--------------|------------|------------|
| Body text | 4.5:1 | 7:1 |
| Large text (18px+ or 14px bold) | 3:1 | 4.5:1 |
| UI components, icons | 3:1 | 4.5:1 |
| Non-essential decorations | None | None |

**容易忽略的一點**：Placeholder text 也需要 4.5:1。你常看到那種淺灰 placeholder，通常都不合格。

### 危險的配色組合

這些組合常常對比不夠，或會影響可讀性：

- 白底淺灰字（最常見的無障礙失敗）
- **彩色背景上的灰字**，灰字在彩色上會顯得發灰、無力。請用背景色的深色階，或用透明度
- 綠底紅字（或反過來），8% 男性無法區分這類組合
- 紅底藍字（會產生視覺震動）
- 白底黃字（幾乎一定失敗）
- 圖片上的細淺色文字（對比不可預測）

### 永遠不要使用純灰或純黑

純灰（`oklch(50% 0 0)`）與純黑（`#000`）在自然界中幾乎不存在，真實陰影與表面總帶有色偏。就算只有 0.005-0.01 的 chroma，也足夠讓畫面看起來更自然，而不會明顯染色。（可參考上方帶色中性色範例）

### Testing

不要只相信你的眼睛。請用工具：

- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- Browser DevTools → Rendering → Emulate vision deficiencies
- [Polypane](https://polypane.app/) 做即時測試

## Theming：Light 與 Dark Mode

### Dark Mode 不是 Light Mode 的反相

不能直接把顏色倒過來。Dark mode 需要不同設計判斷：

| Light Mode | Dark Mode |
|------------|-----------|
| 用陰影建立深度 | 用更亮的 surface 建立深度（不要靠陰影） |
| 深色文字配淺背景 | 淺色文字配深背景（字重也要稍微變輕） |
| 高彩度 accent | Accent 稍微去飽和 |
| 白色背景 | 不要純黑，請用深灰（oklch 12-18%） |

```css
/* Dark mode depth via surface color, not shadow */
:root[data-theme="dark"] {
  --surface-1: oklch(15% 0.01 250);
  --surface-2: oklch(20% 0.01 250);  /* "Higher" = lighter */
  --surface-3: oklch(25% 0.01 250);

  /* Reduce text weight slightly */
  --body-weight: 350;  /* Instead of 400 */
}
```

### Token Hierarchy

使用兩層 token：primitive tokens（`--blue-500`）與 semantic tokens（`--color-primary: var(--blue-500)`）。進入 dark mode 時，只重定義 semantic layer，primitive 保持不變。

## Alpha 是一種設計警訊

大量依賴透明度（rgba、hsla）通常代表你的 palette 不完整。Alpha 會帶來不可預測的對比、額外效能成本與不一致。請為每種情境定義明確的 overlay colors。例外只有 focus rings 與某些必須看透底層的互動狀態。

---

**Avoid**：只靠顏色傳達資訊。建立沒有清楚角色分工的色盤。在大面積區域使用純黑（#000）。跳過色盲測試（8% 男性受影響）。
