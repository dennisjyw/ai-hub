# ReactBits 動效元件指南

## 安裝方式

```bash
# TypeScript + Tailwind 版本
npx jsrepo add https://reactbits.dev/ts/tailwind/<Category>/<ComponentName>
```

## 元件分類與克制使用

### 文字動效（TextAnimations）

| 元件 | 適用場景 | 克制程度 |
|------|---------|---------|
| SplitText | Hero 主標題逐字出現 | ✅ 克制 |
| BlurText | 副標題模糊漸入 | ✅ 克制 |
| GradientText | 品牌關鍵詞高亮 | ✅ 克制 |
| ShinyText | 高光掃過效果，適合 CTA | ✅ 克制 |
| CountUp | 數字統計展示 | ✅ 克制 |
| RotatingText | 循環切換關鍵詞 | ⚠️ 適度 |
| DecryptedText | 科技/解密效果 | ⚠️ 僅科技類 |
| ScrambleText | 亂碼擾動效果 | ⚠️ 僅個性品牌 |

### 交互动效（Animations）

| 元件 | 適用場景 | 克制程度 |
|------|---------|---------|
| FadeContent | 滾動進入時淡入 | ✅ 克制 |
| BlurFade | 模糊淡入，更柔和 | ✅ 克制 |
| ScrollReveal | 文字隨滾動逐行顯示 | ✅ 克制 |
| GlassIcons | 毛玻璃圖標組 | ✅ 克制 |
| Magnet | 滑鼠磁吸效果，用於 CTA | ⚠️ 適度 |
| TiltedCard | 滑鼠懸停卡片傾斜 | ⚠️ 適度 |
| FlipCard | 翻轉卡片 | ⚠️ 適度 |

### 背景動效（Backgrounds）

| 元件 | 適用場景 | 克制程度 |
|------|---------|---------|
| Particles | 細膩粒子背景 | ✅ 克制（density 調低） |
| GridMotion | 極簡網格流動 | ✅ 克制 |
| DotGrid | 點陣背景 | ✅ 克制 |
| Aurora | 極光漸變背景 | ⚠️ 適度（顏色別太亮） |
| Iridescence | 彩虹漸變背景 | ⚠️ 適度 |
| MeshGradient | 網格漸變 | ⚠️ 適度 |

### UI 元件（Components）

| 元件 | 適用場景 | 克制程度 |
|------|---------|---------|
| AnimatedList | 動態列表（消息/通知流） | ✅ 克制 |
| Dock | macOS 風格底部導航 | ✅ 克制 |
| Marquee | 無縫滾動 Logo 牆 | ✅ 克制 |
| Stepper | 步驟指引動畫 | ✅ 克制 |

## 搭配規則

**硬性限制**：
- 同一頁面，背景動效最多 1 個
- 同一頁面，文字動效最多 2 種（且不同區域）
- 不要給滾動文字段落加動效
- 不要在移動端使用 Magnet、TiltedCard（加 isMobile 判斷）

**風格搭配**：
- 淺色/企業風 → FadeContent + SplitText + Particles(低密度)
- 深色/科技風 → BlurText + Spotlight + Aurora
- 創意/個性 → RotatingText + TiltedCard + MeshGradient
- 簡約/極簡 → BlurFade + DotGrid

## 調參原則

| 參數 | 建議值 | 說明 |
|------|--------|------|
| delay | 60-120ms | 字間延遲 |
| duration | 0.4-0.8s | 動畫時長 |
| Particles quantity | 40-80 | 粒子數量 |
| Aurora 飽和度 | 降低 20-30% | 避免刺眼 |

## 無障礙支援

```javascript
const prefersReducedMotion = window.matchMedia(
  '(prefers-reduced-motion: reduce)'
).matches;

// 若為 true，跳過動效或使用極簡版
{!prefersReducedMotion && <Particles quantity={60} />}
```

## 快速參數參考

### SplitText
```jsx
<SplitText
  text="主標題"
  delay={80}
  duration={0.6}
  ease="power3.out"
/>
```

### FadeContent
```jsx
<FadeContent delay={100} duration={0.6}>
  <div>內容</div>
</FadeContent>
```

### Particles
```jsx
<Particles
  quantity={60}
  staticity={30}
  className="absolute inset-0"
/>
```
