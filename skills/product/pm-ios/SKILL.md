---
name: pm-ios
description: 當需求明確是 iPhone、iPad、iOS app、Apple HIG、SwiftUI、UIKit 或 iOS 優先的 React Native／Expo 專案時使用。這個技能負責把需求導向 iOS 專用流程與參考資料，避免與通用 `pm-dev` 或 `pm-web` 混用。
---

# pm-ios

## 何時使用
- iOS app 規劃與開發。
- 需要 Apple HIG、iPhone 體驗、App Store 上架考量。

## 路由規則
- 若只是一般產品探索但平台未定，退回 `pm-dev`。
- 若主要是瀏覽器體驗或網站，改用 `pm-web`。
- iOS 任務一律優先沿用 `pm-dev` 的階段式流程，再套 iOS 參考。

## 載入策略
- 主技能只判斷是否為 iOS 場景。
- 需要平台細節時再讀 `references/` 內對應資料。
