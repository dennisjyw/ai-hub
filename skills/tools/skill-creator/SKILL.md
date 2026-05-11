---
name: skill-creator
description: 當使用者要建立新 skill、重寫既有 skill、優化觸發描述、做技能評估、比較新舊版本表現，或要求依照 skill 標準規範檢查整包技能時使用。這個技能負責意圖釐清、SKILL.md 設計、progressive disclosure、測試與迭代。
---

# Skill Creator

## 何時使用
- 建立新 skill。
- 改寫或瘦身既有 `SKILL.md`。
- 檢查 skill 是否好觸發、好閱讀、低 preload 成本。
- 想跑 eval、比較新舊 skill 表現。

## 核心標準
- `description` 要清楚寫出何時觸發與做什麼，且要偏積極觸發。
- 主 `SKILL.md` 只放路由、邊界、流程與輸出要求。
- 長篇教學、範例、schema、腳本說明放到 `references/`、`scripts/` 或其他附檔。
- 優先用 progressive disclosure，避免觸發後一次載入過多內容。

## 工作流程
1. 先釐清 skill 的任務、觸發句型、輸出格式與是否需要 eval。
2. 寫或改 `SKILL.md`，先縮主檔，再把細節下放。
3. 若要驗證，建立 eval prompts，必要時做新舊比較。
4. 依結果再調整描述、流程、邊界與 references。

## 載入策略
- 主流程與原則看本檔。
- schema 與 benchmark 細節再讀 `references/`。
- 腳本與 viewer 操作再讀 `scripts/` 與對應說明。

## 產出要求
- 至少說明：改了哪些 trigger、哪些內容被下放、token 成本如何降低。
- 若有跑 eval，需回報 qualitative 與 quantitative 差異。
