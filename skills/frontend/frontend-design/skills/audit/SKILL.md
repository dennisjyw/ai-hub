---
name: audit
description: 當要系統性稽核 UI 的無障礙、效能、響應式、主題一致性與實作品質時使用。此技能以找問題與排序優先級為主，不直接假設要大改設計。支援 Vercel Web Interface Guidelines 審查。
---

# Audit

系統性稽核 UI 品質，找出問題並排序優先級。

## 何時使用

- 設計或前端品質稽核
- 可訪問性 (a11y) 檢查
- 響應式設計審查
- 主題一致性檢查

## 稽核維度

1. **無障礙 (Accessibility)** - ARIA 標籤、鍵盤導航、色彩對比
2. **效能 (Performance)** - 載入時間、渲染性能、資源優化
3. **響應式 (Responsive)** - 斷點適配、觸控目標、可讀性
4. **主題一致性 (Consistency)** - 設計令牌、元件複用、視覺層級

## Vercel Web Interface Guidelines

如需參考最新的 Web 介面設計規範：

```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

使用 WebFetch 動態獲取最新規則進行審查。

## 產出要求

- 依嚴重度列問題（Critical > High > Medium > Low）
- 每項至少包含：觀察、風險、修法
- 若無重大問題，也要列剩餘風險與驗證缺口

