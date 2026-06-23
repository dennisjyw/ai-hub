---
name: gsap
description: 當專案使用或準備使用 GSAP 動畫庫，且任務涉及動畫、時間軸、滾動動畫、插件、React 整合、效能優化或框架整合時使用。這個技能負責導向正確的子技能，不應把所有文件塞進主技能。
---

# GSAP (GreenSock Animation Platform)

## 何時使用
- 使用者提到 GSAP、GreenSock、動畫庫、timeline、ScrollTrigger、tween。
- 需要 JavaScript 動畫（React、Vue、Svelte 或原生 JS）。
- 需要滾動驅動動畫、SVG 動畫、拖拽互動或複雜動畫序列。
- Webflow 互動/動畫問題（Webflow 底層使用 GSAP）。

## 載入策略
- **核心 API**（to/from/fromTo/easing/stagger）：讀 [gsap-core.md](gsap-core.md)
- **時間軸排序**（sequence/nesting/labels/playback）：讀 [gsap-timeline.md](gsap-timeline.md)
- **滾動動畫**（ScrollTrigger/scrub/pin/batch）：讀 [gsap-scrolltrigger.md](gsap-scrolltrigger.md)
- **插件**（Flip/Draggable/SplitText/MorphSVG/DrawSVG 等）：讀 [gsap-plugins.md](gsap-plugins.md)
- **工具函數**（clamp/mapRange/interpolate/random/snap/toArray）：讀 [gsap-utils.md](gsap-utils.md)
- **React 整合**（useGSAP/context/cleanup/SSR）：讀 [gsap-react.md](gsap-react.md)
- **效能優化**（transforms/will-change/batching）：讀 [gsap-performance.md](gsap-performance.md)
- **Vue/Svelte/其他框架**（lifecycle/cleanup）：讀 [gsap-frameworks.md](gsap-frameworks.md)

## 執行流程
1. 確認專案是否已安裝 GSAP（`npm install gsap`）。
2. 根據任務需求載入對應的子技能。
3. 遵循官方最佳實踐與 Do Not 規則。
4. 交付時包含安裝步驟、變更檔案與動畫參數說明。

## 授權
MIT License — 所有 GSAP 插件（包含原 Club GSAP 付費插件）均免費使用，包括商業用途。
