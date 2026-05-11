---
name: react-best-practices
description: 當編寫、審查或重構 React/Next.js 代碼時使用。提供來自 Vercel Engineering 的性能優化指南，涵蓋 58 條規則，分為 8 個優先級類別。
license: MIT
---

# React 最佳實踐

React 與 Next.js 性能優化指南，來自 Vercel Engineering。

## 何時使用

- 編寫新的 React 元件或 Next.js 頁面
- 實作資料取得（客戶端或伺服器端）
- 審查代碼性能問題
- 重構現有 React/Next.js 代碼
- 優化 bundle 大小或載入時間

## 規則類別（按優先級）

| 優先級 | 類別 | 影響 | 前綴 |
|--------|------|------|------|
| 1 | 消除 Waterfalls | 關鍵 | `async-` |
| 2 | Bundle 大小優化 | 關鍵 | `bundle-` |
| 3 | 伺服器端性能 | 高 | `server-` |
| 4 | 客戶端資料取得 | 中高 | `client-` |
| 5 | 重新渲染優化 | 中 | `rerender-` |
| 6 | 渲染性能 | 中 | `rendering-` |
| 7 | JavaScript 性能 | 低中 | `js-` |
| 8 | 進階模式 | 低 | `advanced-` |

## 快速參考

### 關鍵規則

- `async-parallel` - 使用 Promise.all() 進行獨立操作
- `bundle-dynamic-imports` - 使用 next/dynamic 延遲載入
- `server-cache-react` - 使用 React.cache() 進行請求級去重
- `rerender-memo` - 將昂貴工作提取到 memoized 元件

## 使用方式

參見 `rules/` 目錄中的個別規則文件，每個文件包含：
- 規則說明與重要性
- 錯誤代碼範例
- 正確代碼範例
- 額外上下文與參考

## 參考資源

- [references/AGENTS.md](references/AGENTS.md) - 完整指南（所有規則展開）
- [rules/](rules/) - 個別規則詳細說明

## 規則總數

共 58 條規則，涵蓋：
- 5 條 async 規則
- 5 條 bundle 規則
- 8 條 server 規則
- 4 條 client 規則
- 10 條 rerender 規則
- 9 條 rendering 規則
- 12 條 js 規則
- 5 條 advanced 規則
