# 通透质感UI设计系统

## 设计概述
玻璃拟态（Glassmorphism）是一种现代UI设计风格，通过半透明、模糊和光影效果创造层次感和空间感。

## 核心CSS变量

```css
:root {
  /* 玻璃基础色 */
  --glass-bg: rgba(255, 255, 255, 0.1);
  --glass-bg-dark: rgba(0, 0, 0, 0.2);
  
  /* 模糊强度 */
  --blur-light: blur(8px);
  --blur-medium: blur(16px);
  --blur-heavy: blur(24px);
  
  /* 边框 */
  --border-glass: 1px solid rgba(255, 255, 255, 0.2);
  --border-subtle: 1px solid rgba(255, 255, 255, 0.1);
  
  /* 阴影层次 */
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.1);
  --shadow-md: 0 8px 32px rgba(0, 0, 0, 0.15);
  --shadow-lg: 0 16px 48px rgba(0, 0, 0, 0.2);
  
  /* 圆角 */
  --radius-sm: 8px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --radius-xl: 32px;
  
  /* 字体 */
  --font-system: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', sans-serif;
}
```

## 玻璃卡片基础样式

```css
.glass-card {
  background: var(--glass-bg);
  backdrop-filter: var(--blur-medium);
  -webkit-backdrop-filter: var(--blur-medium);
  border: var(--border-glass);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-md);
}
```

## 玻璃反光效果

```css
.glass-shine::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.4),
    transparent
  );
}
```

## 导航栏样式

```css
.glass-nav {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: var(--blur-heavy);
  border-radius: var(--radius-xl);
  padding: 12px 24px;
  box-shadow: var(--shadow-sm);
}
```

## 动效参数

```css
/* 悬停过渡 */
--transition-fast: 0.2s ease;
--transition-normal: 0.3s ease;
--transition-slow: 0.5s ease;

/* 弹性动画 */
--bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);
--smooth: cubic-bezier(0.4, 0, 0.2, 1);
```

## 色块透明度层级

| 层级 | 透明度 | 用途 |
|------|--------|------|
| 主内容 | 100% | 标题、重要数据 |
| 次要内容 | 70% | 描述文字 |
| 辅助信息 | 50% | 时间、标签 |
| 背景装饰 | 10-20% | 玻璃基底 |

## 响应式断点

```css
--breakpoint-sm: 640px;
--breakpoint-md: 768px;
--breakpoint-lg: 1024px;
--breakpoint-xl: 1280px;
```
