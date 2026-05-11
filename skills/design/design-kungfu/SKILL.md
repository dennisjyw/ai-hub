---
name: design-kungfu
description: 當使用者說「幫我設計一個...」、「給我推薦設計風格」、「這個產品用什麼設計風格好」、「設計建議」時使用。從 127+ 設計風格中智能匹配最佳方案，提供完整設計系統。
---

# Design Kungfu - 設計風格智能推薦

智能分析 Web 應用需求，從 127+ 設計風格中匹配最佳方案。

## 何時使用

- 「幫我設計一個...」
- 「給我推薦設計風格」
- 「這個產品用什麼設計風格好」
- 「設計建議」

## 核心能力

1. **需求分析** - 理解產品類型、目標用戶、品牌調性
2. **智能匹配** - 從 127+ 設計風格中找到最適合的選項
3. **多維推薦** - 提供多個設計方案，每個都有評分和理由
4. **設計系統** - 提供完整的設計規範和開發指南
5. **框架友好** - 預設推薦 shadcn/ui + Tailwind CSS

## 風格資料庫

127 個內建風格，涵蓋：
- 極簡/清爽系列（Minimalist Flat、Soft UI、Corporate Clean）
- 新粗野主義（Neo-Brutalist、Neo-Brutalist Playful）
- 形態系列（Glassmorphism、Neumorphism、Claymorphism）
- 現代/科技（Dark Mode、Cyberpunk、Modern Gradient）
- 佈局模式（Bento Grid、Dashboard、Split Screen）

## 工作流程

1. **需求分析** - 詢問產品類型、目標用戶、品牌調性、設備、特殊要求
2. **風格匹配** - 基於維度評分系統匹配風格
3. **推薦展示** - 展示 Top 5 推薦，包含評分和理由
4. **風格詳情** - 從 `styles/` 目錄讀取選中風格的設計系統
5. **開發指導** - 提供基於 shadcn/ui 的實作建議

## 評分維度

| 維度 | 權重 |
|------|------|
| 產品類型匹配 | 30% |
| 品牌調性匹配 | 25% |
| 目標受眾匹配 | 20% |
| 設備適配 | 15% |
| 技術約束 | 10% |

## 風格映射

| 產品類型 | 首選風格 | 備選風格 |
|----------|----------|----------|
| SaaS | Minimalist Flat, Glassmorphism | Soft UI, Corporate Clean |
| 電商 | Corporate Clean, Minimalist | Apple Style, Soft UI |
| Fintech | Corporate Clean, Minimalist | Glassmorphism, Dark Mode |
| 醫療 | Soft UI, Minimalist | Corporate Clean, Apple Style |
| 教育科技 | Soft UI, Bento Grid | Neo-Brutalist Playful |
| 開發者工具 | Dark Mode, Minimalist | Neo-Brutalist, Cyberpunk |
| AI/ML 平台 | Glassmorphism, Dark Mode | Cyberpunk, Aurora |

## 資源索引

- `styles/` - 127 個風格的設計系統文檔
- `database.js` - 產品類型映射數據
- `data/` - 設計數據和配置
- `scripts/` - 輔助腳本

## 使用方法

```bash
# 查看可用風格
ls styles/

# 讀取特定風格
cat styles/minimalist-flat.md
cat styles/glassmorphism.md
```

## 注意事項

- 所有風格文件通過 `styles/` 目錄相對路徑訪問
- 風格選擇後，精確使用 Tokens，不要近似或替換
- 遵循元件配方，使用參數化模板
- 確保設計在響應式、可訪問性方面符合標準
