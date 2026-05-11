# 資料庫設置

## 核心表結構

### profiles 表
```sql
CREATE TABLE public.profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  username TEXT UNIQUE,
  avatar_url TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

### RLS 策略
```sql
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;

-- 用戶可以查看自己的資料
CREATE POLICY "用戶可以查看自己的資料" ON public.profiles
  FOR SELECT USING (auth.uid() = id);

-- 用戶可以更新自己的資料
CREATE POLICY "用戶可以更新自己的資料" ON public.profiles
  FOR UPDATE USING (auth.uid() = id);

-- 用戶可以插入自己的資料（用於觸發器）
CREATE POLICY "用戶可以插入自己的資料" ON public.profiles
  FOR INSERT WITH CHECK (auth.uid() = id);
```

### 自動建立 Profile 觸發器（含自動確認郵箱）
```sql
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS trigger
LANGUAGE plpgsql
SECURITY DEFINER SET search_path = public, auth
AS $$
BEGIN
  -- 自動確認用戶郵箱
  UPDATE auth.users SET email_confirmed_at = NOW() WHERE id = new.id;
  
  -- 建立用戶資料
  INSERT INTO public.profiles (id, username, avatar_url)
  VALUES (
    new.id,
    COALESCE(new.raw_user_meta_data ->> 'username', split_part(new.email, '@', 1)),
    new.raw_user_meta_data ->> 'avatar_url'
  );
  RETURN new;
END;
$$;

CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();
```

## 執行步驟
1. 使用 CloudApplyMigration 工具執行上述 SQL
2. 驗證 profiles 表建立成功
3. 測試觸發器：註冊新用戶後檢查 profiles 表是否自動建立記錄

## 注意事項
- **禁止修改 auth schema**: 所有操作在 public schema 中進行
- **SECURITY DEFINER**: 觸發器函數必須使用 security definer
- **RLS 必須啟用**: 所有用戶相關表都必須啟用行級安全
- **級聯刪除**: profiles 表使用 ON DELETE CASCADE
- **自動確認**: 觸發器會自動設定 email_confirmed_at，用戶註冊後即可立即登入
