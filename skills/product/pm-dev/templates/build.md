# 技術與任務規劃

> **文件定位**：整合技術設計、實作規範、任務拆解，取代 SDD + 部分 WBS + implementation plan
> **目標**：讓 AI 知道「應該怎麼做」與「做到什麼才算完成」
> **更新時機**：architect / plan skill 執行後

---

## 技術棧

### 前端
- **框架**：[例如：React / Vue / Next.js]
- **語言**：[例如：TypeScript]
- **UI 庫**：[例如：Tailwind CSS / shadcn/ui]
- **狀態管理**：[例如：Zustand / Redux / Context]

### 後端（選填）
- **框架**：[例如：Node.js / Python]
- **資料庫**：[例如：PostgreSQL / MongoDB]
- **ORM**：[例如：Prisma / Drizzle]

### 工具與服務
- **建構工具**：[例如：Vite / Webpack]
- **部署**：[例如：Vercel / AWS]
- **其他**：[其他工具]

---

## 架構原則

### 核心原則
1. [原則 1]：[說明]
2. [原則 2]：[說明]

### 設計模式
- [模式 1]：[應用在哪裡]
- [模式 2]：[應用在哪裡]

---

## 專案結構 / Repo Structure

```
project/
├── src/
│   ├── components/       # 共用元件
│   │   ├── ui/          # 基礎 UI 元件
│   │   └── common/      # 業務元件
│   ├── pages/           # 頁面元件
│   ├── hooks/           # 自定義 hooks
│   ├── stores/          # 狀態管理
│   ├── utils/           # 工具函數
│   ├── services/        # API 服務
│   └── types/           # TypeScript 類型
├── public/              # 靜態資源
├── tests/               # 測試檔案
└── docs/                # 文件
```

---

## 資料模型

### [實體名稱 1]
```typescript
interface Entity1 {
  id: string;
  field1: string;
  field2: number;
  createdAt: Date;
  updatedAt: Date;
}
```

**關係：**
- [關係 1]：[描述]

---

## API / 資料流草規格

### [API 名稱 1]
**方法：** GET / POST / PUT / DELETE
**路徑：** `/api/...`

**請求參數：**
| 參數 | 類型 | 必填 | 說明 |
|------|------|------|------|
| param1 | string | 是 | 說明 |
| param2 | number | 否 | 說明 |

**回應：**
```json
{
  "data": { ... },
  "status": "success"
}
```

---

## 狀態管理策略

### 全域狀態
- [狀態 1]：[管理方式]
- [狀態 2]：[管理方式]

### 本地狀態
- [原則 1]
- [原則 2]

---

## Coding Rules

### 命名規範
- **元件**：PascalCase（例如：UserProfile）
- **函數/變數**：camelCase（例如：getUserData）
- **常數**：UPPER_SNAKE_CASE（例如：API_BASE_URL）
- **檔案**：kebab-case（例如：user-profile.tsx）

---

## Milestones

### Milestone 1: [名稱]
**目標：** [這個 milestone 要完成什麼]
**預計完成：** [日期]
**成功標準：**
- [ ] [標準 1]
- [ ] [標準 2]

---

## Task Backlog

### 進行中
- [ ] **[TASK-001]** [任務名稱] - [狀態]

### 待開始
- [ ] **[TASK-002]** [任務名稱]
- [ ] **[TASK-003]** [任務名稱]

### 已完成
- [x] **[TASK-000]** [任務名稱] - 完成日期：[日期]

---

## Task 詳細規格

### TASK-001: [任務名稱]
**所屬 Milestone：** [Milestone 名稱]

**描述：**
[具體要做什麼]

**Acceptance Criteria：**
- [ ] [可驗證的完成條件 1]
- [ ] [可驗證的完成條件 2]
- [ ] [可驗證的完成條件 3]

**估計：** [時間]
**依賴：** [依賴的 task]
**狀態：** [待開始/進行中/已完成]

---

## Definition of Done

### Task 完成標準
- [ ] 功能實作完成
- [ ] 通過測試（單元測試/整合測試）
- [ ] 程式碼審查通過（如適用）
- [ ] 文件已更新

### Milestone 完成標準
- [ ] 所有 task 已完成
- [ ] 整合測試通過
- [ ] 驗收標準達成
- [ ] 相關文件已更新

---

## 更新記錄

| 日期 | 更新內容 | 更新者 |
|------|----------|--------|
| YYYY-MM-DD | 初始版本 | AI |
