---
name: n8n-agent
description: 當使用者要把自然語言需求轉成 n8n workflow、AI Agent 流程、可匯入的 JSON、節點串接邏輯或 Mermaid 流程圖時使用。只要任務核心是 n8n 自動化設計，而不是一般程式開發，就應優先觸發此技能。
---

# n8n Agent

## 何時使用
- 使用者提到 `n8n`、workflow、automation、AI Agent、節點串接、匯入 JSON。
- 需求是「設計流程」或「產出可導入 n8n 的檔案」。

## 不要使用
- 純後端 API 開發。
- 與 n8n 無關的一般自動化腳本。

## 載入策略
- 先讀 [references/prompt.md](references/prompt.md) 取得完整流程與節點規範。
- 只在需要補背景時再讀 [references/說明文件.md](references/說明文件.md)。

## 執行流程
1. 先把需求拆成觸發條件、輸入來源、核心節點、輸出結果。
2. 確認是否需要真人審批、排程、Webhook、外部 API、記憶體或向量檢索。
3. 先畫出流程圖，再產出 n8n JSON，避免直接拼節點。
4. 交付時同時給：流程摘要、風險點、可匯入 JSON、必要設定說明。

## 產出要求
- 預設提供可讀摘要與可匯入的 workflow JSON。
- 若流程較複雜，再補 Mermaid 流程圖與節點說明。
- 明確標出需要使用者自行填入的憑證、環境變數與 Webhook URL。
