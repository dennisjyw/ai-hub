---
name: glassmorphism
description: 當使用者提到「玻璃質感」、「毛玻璃」、「通透 UI」、「iOS 風格」、「玻璃擬態設計」時使用。創建具有毛玻璃效果、景深光影的現代 UI。
dependency:
  npm:
    - canvas@^2.11.2
---

# 玻璃擬態 UI (Glassmorphism)

創建具有通透玻璃質感的前端 UI 設計。

## 何時使用

- 「玻璃質感」、「毛玻璃效果」
- 「通透 UI」、「iOS 風格界面」
- 「現代卡片設計」

## 設計規範

### 視覺風格
- **毛玻璃效果**：使用 `backdrop-filter: blur()` 實現 iOS 原生模糊
- **景深光影**：背景圖 + 暗色遮罩 + 光源方向明確的陰影
- **玻璃反光**：疊加高光模擬玻璃表面反光效果
- **空間感**：通過多層陰影和透明度製造正式的空間層次

### 字體規範
- 字體輕盈，採用系統預設無襯線字體
- 留白精簡但資訊完整
- 遵循 Apple 設計規範

### 卡片設計
- 單層陰影，不加描邊
- 色塊用透明度區分主次
- 圓角設計，符合 Apple 風格

### 數據展示
- 圓環進度條
- 卡片式資訊塊
- 色塊對比展示

## 工作流程

1. **讀取設計規範** - 參考 references/design-system.md
2. **生成背景圖** - 如需自定義背景，調用 scripts/generate-background.js
3. **實作元件** - 按照規範實作玻璃卡片、圓環進度、導航欄

## 參考資源

- [references/design-system.md](references/design-system.md) - 完整設計系統規範
- [references/component-examples.md](references/component-examples.md) - 核心元件代碼範例
- [references/background-generator.md](references/background-generator.md) - 背景圖生成器使用說明
- [scripts/generate-background.js](scripts/generate-background.js) - 背景圖生成腳本

## 注意事項

- **實作優先級**：backdrop-filter > box-shadow > background-gradient
- **性能注意**：毛玻璃效果在低端設備上可能影響性能，建議提供降級方案
- **瀏覽器兼容**：確保在 Safari、Chrome、Firefox 上均有良好表現
