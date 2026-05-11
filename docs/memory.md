# Memory 系統規範

> **重要**：本文件僅為路標，完整規範請參考 Claude 根目錄。

---

## 主要規範文件

請先讀取：**`~/.claude/memory/MEMORY.md`**

該索引檔包含：
- Memory 系統結構
- 使用方式（自動/手動模式）
- 檔案命名規則
- 專案索引

---

## 模板檔案

專案 memory 模板：
**`~/.claude/memory/project-memory.md`**

---

## 快速參考

### Memory 路徑
```
~/.claude/memory/
├── MEMORY.md              # 索引檔案（讀取這個）
├── project-memory.md      # 模板檔案
└── projects/              # 各專案的 memory 檔案
    ├── campus-ai-frontend.md
    ├── lab-website.md
    └── mindgap-website.md
```

### Memory 類型
- **user**: 使用者的角色、目標、責任和知識
- **feedback**: 對工作方式的指導（避免什麼、繼續做什麼）
- **project**: 進行中的工作、目標、計畫或事件
- **reference**: 外部系統資源的指標

---

## 工作流程

1. **Session 開始**：讀取 `MEMORY.md` 索引 → 讀取當前專案 memory（如果存在）
2. **Session 結束**：更新相關 memory 檔案
3. **定期整理**：在 Claude 中檢視、更新 memory

---

> 這是 Claude Code 官方建議的記憶系統位置，方便存取。