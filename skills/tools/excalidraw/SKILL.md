---
name: excalidraw
description: 當使用者要求「建立圖表」、「畫流程圖」、「視覺化流程」、「繪製系統架構圖」、「建立心智圖」或產生 .excalidraw 檔案時使用。支援流程圖、關係圖、心智圖、架構圖、時序圖、類別圖、ER 圖等多種圖表類型。
---

# Excalidraw 圖表生成

從自然語言描述生成 Excalidraw 格式的圖表。

## 何時使用

- 「建立一個圖表顯示...」
- 「畫個流程圖」
- 「視覺化這個流程」
- 「繪製系統架構」
- 「建立心智圖」
- 「產生 .excalidraw 檔案」

## 支援圖表類型

| 圖表類型 | 適用場景 | 關鍵詞 |
|---------|---------|--------|
| 流程圖 | 順序流程、工作流程 | workflow, process, steps |
| 關係圖 | 實體關係、系統元件 | relationship, dependencies |
| 心智圖 | 概念層級、腦力激盪 | mind map, concepts |
| 架構圖 | 系統設計、模組互動 | architecture, system |
| 時序圖 | 物件互動、訊息流 | sequence, timeline |
| 類別圖 | 物件導向設計 | class, OOP |
| ER 圖 | 資料庫實體關係 | database, entity |

## 工作流程

1. **理解需求** - 分析圖表類型、關鍵元素、關係
2. **選擇圖表類型** - 根據使用者意圖選擇最適合的類型
3. **提取結構資訊** - 整理步驟、實體、關係等結構化資料
4. **生成 Excalidraw JSON** - 建立符合格式的 .excalidraw 檔案
5. **輸出與說明** - 提供檔案與開啟方式說明

## 設計規範

### 色彩配置

| 用途 | 顏色 |
|------|------|
| 主要元素 | `#a5d8ff` (淺藍) |
| 次要元素 | `#b2f2bb` (淺綠) |
| 重要/中心 | `#ffd43b` (黃色) |
| 警示/警告 | `#ffc9c9` (淺紅) |

### 間距規範

- 水平間距：200-300px
- 垂直間距：100-150px
- 字體大小：16-24px

### 重要提醒

- 所有文字元素必須使用 `fontFamily: 5` (Excalifont)
- 單一圖表元素數量建議 < 20
- 複雜場景拆分为多個圖表

## 參考資源

- [references/diagram-types.md](references/diagram-types.md) - 各類圖表詳細規範與結構要求
- [references/json-schema.md](references/json-schema.md) - Excalidraw JSON 完整格式說明
- [references/layout-guide.md](references/layout-guide.md) - 佈局最佳實踐與配色方案
- [templates/flowchart.json](templates/flowchart.json) - 流程圖模板
- [templates/mindmap.json](templates/mindmap.json) - 心智圖模板
