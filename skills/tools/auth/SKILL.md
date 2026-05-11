---
name: auth
description: 當使用者提到「註冊」、「登入」、「用戶認證」、「帳號系統」、「密碼管理」、「用戶中心」或需要實作身份驗證功能時使用。基於 Supabase Auth 實作安全的密碼加密儲存和會話管理。
dependency:
  npm:
    - "@supabase/supabase-js@^2.39.0"
---

# 用戶認證系統

實作安全的用戶註冊、登入、登出和會話管理。

## 何時使用

- 「實作註冊登入功能」
- 「用戶認證系統」
- 「帳號管理」
- 「密碼加密」
- 「用戶中心」

## 能力範圍

- 郵箱/用戶名密碼認證
- 會話持久化
- 用戶資料管理
- 密碼加密儲存（Supabase Auth 自動處理）

## 工作流程

1. **資料庫初始化** - 執行 SQL 遷移建立 profiles 表和 RLS 策略
2. **實作認證元件** - 建立註冊表單、登入表單、用戶狀態管理
3. **整合至應用** - 設定 auth 狀態監聽、受保護路由、用戶資訊展示

## 核心原則

- **密碼安全**：由 Supabase Auth 自動加密儲存，嚴禁前端硬編碼或明文傳輸
- **用戶名註冊**：使用虛擬郵箱方案（`username@auth.local`），用戶無感知
- **自動確認**：新用戶註冊時自動確認郵箱，無需郵件驗證即可登入
- **會話管理**：必須儲存完整的 session 對象，不僅是 user 對象

## 參考資源

- [references/database-setup.md](references/database-setup.md) - 資料庫表結構、RLS 策略、觸發器完整 SQL
- [references/auth-patterns.md](references/auth-patterns.md) - React 認證元件模式、狀態管理、受保護路由實作
- [scripts/auth-utils.js](scripts/auth-utils.js) - 註冊、登入、登出、獲取用戶資訊等核心認證函數
