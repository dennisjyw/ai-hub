# 認證元件模式

## 核心狀態管理

### AuthProvider 模式
```jsx
import { useState, useEffect, createContext, useContext } from 'react';
import { supabase } from '../supabase/client';

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [session, setSession] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // 設定 auth 狀態監聽
    const { data: { subscription } } = supabase.auth.onAuthStateChange(
      (event, session) => {
        setSession(session);
        setUser(session?.user ?? null);
        setLoading(false);
      }
    );

    // 檢查現有會話
    supabase.auth.getSession().then(({ data: { session } }) => {
      setSession(session);
      setUser(session?.user ?? null);
      setLoading(false);
    });

    return () => subscription.unsubscribe();
  }, []);

  return (
    <AuthContext.Provider value={{ user, session, loading }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);
```

## 註冊元件模式

```jsx
import { useState } from 'react';
import { registerUser } from './auth-utils';

function RegisterForm() {
  const [identifier, setIdentifier] = useState('');
  const [password, setPassword] = useState('');
  const [isUsername, setIsUsername] = useState(false);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleRegister = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    const { error } = await registerUser(identifier, password, {
      isUsername,
      username: isUsername ? identifier : identifier.split('@')[0],
    });

    if (error) setError(error.message);
    setLoading(false);
  };

  return (
    <form onSubmit={handleRegister}>
      <input
        type={isUsername ? 'text' : 'email'}
        value={identifier}
        onChange={(e) => setIdentifier(e.target.value)}
        placeholder={isUsername ? '用戶名' : '郵箱'}
        required
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="密碼"
        required
      />
      {error && <div className="error">{error}</div>}
      <button type="submit" disabled={loading}>
        {loading ? '註冊中...' : '註冊'}
      </button>
    </form>
  );
}
```

## 登入元件模式

```jsx
import { useState } from 'react';
import { loginUser } from './auth-utils';

function LoginForm() {
  const [identifier, setIdentifier] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    const { error } = await loginUser(identifier, password);

    if (error) setError(error.message);
    setLoading(false);
  };
  // ...
}
```

## 受保護路由模式

```jsx
import { Navigate } from 'react-router-dom';
import { useAuth } from './AuthProvider';

function RouteGuard({ children }) {
  const { user, loading } = useAuth();

  if (loading) return <div>載入中...</div>;
  if (!user) return <Navigate to="/login" replace />;

  return children;
}
```

## 關鍵注意事項
- **禁止硬編碼密碼**: 所有密碼通過 Supabase Auth 處理
- **完整 session 儲存**: 同時維護 user 和 session 狀態
- **錯誤處理**: 所有認證操作必須處理錯誤並反饋給用戶
- **載入狀態**: 所有非同步操作顯示載入狀態，防止重複提交
