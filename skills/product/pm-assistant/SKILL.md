---
name: pm-assistant
description: 當使用者提到需求分析、PRD、用戶故事、產品規劃、競品分析、功能設計、OKR、路線圖時使用。提供產品經理全流程智能化支援。
dependency:
  npm:
    - marked@^9.0.0
---

# 產品經理智能助手

產品管理全流程智能化支援，從需求收集到產品上線。

## 何時使用

- 需求分析與用戶故事拆解
- PRD 文件生成
- 競品分析與市場定位
- 產品規劃與路線圖設計
- OKR 目標拆解

## 核心能力

| 能力 | 說明 |
|------|------|
| 需求分析 | Kano 模型、MoSCoW 法則、可行性分析 |
| 用戶故事 | INVEST 原則、驗收標準、故事點估算 |
| PRD 生成 | 產品背景、功能說明、交互流程、數據指標 |
| 競品分析 | 功能對比、SWOT、差異化策略 |
| 產品規劃 | 版本迭代、路線圖、資源排期 |

## 工作流程

1. **需求輸入** - 提供產品需求描述
2. **分析處理** - 調用分析腳本進行處理
3. **文件輸出** - 生成標準化產品文件

## 腳本工具

| 腳本 | 用途 | 優先級 |
|------|------|--------|
| `scripts/llm-analyze.js` | LLM 增強分析 | ⭐ 推薦 |
| `scripts/analyze.js` | 本地規則引擎分析 | 備選 |
| `scripts/collect.js` | 互動式需求收集 | 系統化收集時 |

## 模板資源

- `templates/prd-template.md` - PRD 文件標準模板
- `templates/user-story-template.md` - 用戶故事模板
- `templates/competitive-analysis-template.md` - 競品分析模板
- `templates/roadmap-template.md` - 產品路線圖模板

## 參考資源

- [references/requirement-framework.md](references/requirement-framework.md) - 需求分析方法論
- [references/priority-model.md](references/priority-model.md) - 優先級評估模型
- [references/ai-workflow-guide.md](references/ai-workflow-guide.md) - AI 產品經理工作流

## 環境變數

```bash
LLM_API_KEY="your-api-key"
LLM_PROVIDER="openai"  # 可選: openai, anthropic, deepseek, qwen
```
