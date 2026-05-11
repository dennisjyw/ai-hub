# Interaction Design

## 八種互動狀態

每個互動元素都需要設計這些狀態：

| State | When | Visual Treatment |
|-------|------|------------------|
| **Default** | 靜止時 | 基礎樣式 |
| **Hover** | 指標移入（非觸控） | 細微抬升、顏色變化 |
| **Focus** | 鍵盤 / 程式 focus | 可見 focus ring（見下） |
| **Active** | 正在按下 | 壓下感、更深色 |
| **Disabled** | 不可互動 | 降低透明度、無 pointer |
| **Loading** | 處理中 | Spinner、skeleton |
| **Error** | 無效狀態 | 紅色邊框、icon、訊息 |
| **Success** | 已完成 | 綠色勾勾、確認訊息 |

**最常漏掉的地方**：只設計 hover、卻不設計 focus，或反過來。這兩者不同。鍵盤使用者永遠看不到 hover。

## Focus Rings：正確處理

**不要在沒有替代方案的情況下使用 `outline: none`。** 這是無障礙違規。請改用 `:focus-visible`，只對鍵盤使用者顯示 focus：

```css
/* Hide focus ring for mouse/touch */
button:focus {
  outline: none;
}

/* Show focus ring for keyboard */
button:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
}
```

**Focus ring 設計原則**：
- 高對比（與鄰近顏色至少 3:1）
- 厚度 2-3px
- 與元素有 offset（不要畫在元素內側）
- 所有互動元素都一致

## Form Design：那些不明顯但重要的事

**Placeholders 不是 labels**，因為一輸入就消失。永遠使用可見的 `<label>`。**請在 blur 時驗證**，不要每打一個字就驗證（密碼強度是例外）。錯誤訊息應該放在欄位**下方**，並用 `aria-describedby` 連結。

## Loading States

**Optimistic updates**：先立即顯示成功，再在失敗時 rollback。這適合低風險行為（按讚、追蹤），不適合付款或破壞性操作。**Skeleton screens > spinners**，因為它們能預示內容形狀，主觀上也比 generic spinner 更快。

## Modals：用 inert 的做法

Modal 的 focus trapping 以前需要複雜 JavaScript。現在請使用 `inert` attribute：

```html
<!-- When modal is open -->
<main inert>
  <!-- Content behind modal can't be focused or clicked -->
</main>
<dialog open>
  <h2>Modal Title</h2>
  <!-- Focus stays inside modal -->
</dialog>
```

或使用原生 `<dialog>` element：

```javascript
const dialog = document.querySelector('dialog');
dialog.showModal();  // Opens with focus trap, closes on Escape
```

## The Popover API

對 tooltips、dropdowns 與非 modal overlays，請使用原生 popovers：

```html
<button popovertarget="menu">Open menu</button>
<div id="menu" popover>
  <button>Option 1</button>
  <button>Option 2</button>
</div>
```

**Benefits**：點外部自動關閉（light-dismiss）、正確堆疊、不再有 z-index 戰爭，且預設就具備可及性。

## Destructive Actions：Undo > Confirm

**Undo 比 confirmation dialogs 更好**，因為使用者通常會無腦點過確認視窗。應先從 UI 中移除，顯示 undo toast，等 toast 過期後再真正刪除。只有在真正不可逆、代價極高，或批次操作時，才使用確認。

## Keyboard Navigation Patterns

### Roving Tabindex

對元件群組（tabs、menu items、radio groups），只讓一個項目可 tab 進入；箭頭鍵則在群組內移動：

```html
<div role="tablist">
  <button role="tab" tabindex="0">Tab 1</button>
  <button role="tab" tabindex="-1">Tab 2</button>
  <button role="tab" tabindex="-1">Tab 3</button>
</div>
```

箭頭鍵負責在項目間切換 `tabindex="0"`，而 Tab 則跳到下一個元件區塊。

### Skip Links

為鍵盤使用者提供 skip links（`<a href="#main-content">Skip to main content</a>`），讓他們可以跳過導覽。預設藏在螢幕外，focus 時再顯示。

## Gesture Discoverability

Swipe-to-delete 與類似手勢本質上是不可見的。請提示其存在：

- **Partially reveal**：讓 delete button 從邊緣露一點出來
- **Onboarding**：首次使用時給 coach marks
- **Alternative**：永遠提供一個可見 fallback（例如含有 "Delete" 的選單）

不要把手勢當成唯一操作方式。

---

**Avoid**：在沒有替代方案下移除 focus indicators。把 placeholder text 當 labels。Touch targets 小於 44x44px。使用泛泛的錯誤訊息。建立沒有 ARIA / keyboard support 的自訂控制元件。
