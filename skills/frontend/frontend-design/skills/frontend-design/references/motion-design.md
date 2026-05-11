# Motion Design

## 時長：100/300/500 Rule

Timing 往往比 easing 更重要。以下時長在大多數 UI 中都很合理：

| Duration | Use Case | Examples |
|----------|----------|----------|
| **100-150ms** | 即時回饋 | Button press、toggle、color change |
| **200-300ms** | 狀態切換 | Menu open、tooltip、hover states |
| **300-500ms** | 版面變化 | Accordion、modal、drawer |
| **500-800ms** | 進場動畫 | Page load、hero reveals |

**離場動畫比進場更快**，建議使用約 75% 的進場時長。

## Easing：選對曲線

**不要用 `ease`。** 那是一個折衷值，通常不是最好的選擇。請改用：

| Curve | Use For | CSS |
|-------|---------|-----|
| **ease-out** | 元素進場 | `cubic-bezier(0.16, 1, 0.3, 1)` |
| **ease-in** | 元素離場 | `cubic-bezier(0.7, 0, 0.84, 0)` |
| **ease-in-out** | 狀態來回切換 | `cubic-bezier(0.65, 0, 0.35, 1)` |

**對 micro-interactions，請使用 exponential curves**，它們之所以自然，是因為更接近真實物理（摩擦、減速）：

```css
/* Quart out - smooth, refined (recommended default) */
--ease-out-quart: cubic-bezier(0.25, 1, 0.5, 1);

/* Quint out - slightly more dramatic */
--ease-out-quint: cubic-bezier(0.22, 1, 0.36, 1);

/* Expo out - snappy, confident */
--ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
```

**避開 bounce 與 elastic curves。** 它們在 2015 年很流行，但現在看起來俗氣而業餘。真實物體停止時不會彈跳，而是平滑減速。Overshoot 效果會把注意力拉到動畫本身，而不是內容。

## 唯二應該被動畫化的屬性

只用 **transform** 與 **opacity**，其他屬性都會觸發 layout recalculation。若要做高度動畫（如 accordion），請用 `grid-template-rows: 0fr → 1fr`，而不是直接動畫 `height`。

## Staggered Animations

使用 CSS custom properties 讓 stagger 更乾淨：`animation-delay: calc(var(--i, 0) * 50ms)`，每個項目加上 `style="--i: 0"`。**請控制總 stagger 時間**，例如 10 個項目 × 50ms = 總共 500ms。若項目很多，請縮短每項延遲或限制 stagger 數量。

## Reduced Motion

這不是可選項。40 歲以上成人中，約有 35% 受 vestibular disorders 影響。

```css
/* Define animations normally */
.card {
  animation: slide-up 500ms ease-out;
}

/* Provide alternative for reduced motion */
@media (prefers-reduced-motion: reduce) {
  .card {
    animation: fade-in 200ms ease-out;  /* Crossfade instead of motion */
  }
}

/* Or disable entirely */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

**該保留什麼**：像 progress bars、loading spinners（可放慢）與 focus indicators 這種功能性動畫仍應保留，只是不要有空間移動。

## Perceived Performance

**沒有人真的在意網站有多快，只在意它感覺多快。** 感知層面的處理，有時和實際效能同樣有效。

**80ms 門檻**：我們的大腦會緩衝約 80ms 的感官輸入，以同步感知。低於 80ms 的事物會感覺像瞬間同時發生。這是 micro-interactions 的理想目標。

**Active vs passive time**：被動等待（盯著 spinner）會感覺更久；主動參與會感覺更短。你可以這樣做：

- **Preemptive start**：在載入時立刻開始 transition（例如 iOS App zoom、skeleton UI），讓使用者感覺事情正在進行
- **Early completion**：逐步顯示內容，不要等所有東西都載完，例如影片 buffering、progressive images、streaming HTML
- **Optimistic UI**：先更新介面，失敗再優雅處理。Instagram 的 like 在離線時也會立刻反應，之後再同步。這適合低風險操作，不適合付款或破壞性動作

**Easing 會影響感知時長**：Ease-in（越接近結尾越快）會讓任務感覺更短，因為 peak-end effect 讓人更重視結尾時刻。Ease-out 適合進場，但若想讓任務感覺更快結束，可在收尾使用 ease-in。

**注意**：太快的回應也可能降低感知價值。對於搜尋、分析等複雜操作，使用者可能不信任瞬間結果。有時很短的延遲反而能傳達「系統真的在做事」。

## Performance

不要預先到處加 `will-change`，只在動畫即將發生時才加（如 `:hover`、`.animating`）。對 scroll-triggered animations，使用 Intersection Observer，而不是 scroll events；動畫一次後就 unobserve。建立 motion tokens 來維持一致性（durations、easings、common transitions）。

---

**Avoid**：什麼都動畫化（動畫疲勞是真實的）。對 UI 回饋使用超過 500ms。忽略 `prefers-reduced-motion`。用動畫掩飾慢速載入。
