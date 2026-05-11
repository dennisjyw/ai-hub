# 玻璃质感组件示例

## 玻璃卡片组件

```jsx
// GlassCard.jsx
function GlassCard({ children, className = '' }) {
  return (
    <div className={`glass-card ${className}`}>
      {children}
    </div>
  );
}

// CSS
.glass-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
  padding: 24px;
  position: relative;
  overflow: hidden;
}

.glass-card::before {
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

## 圆环进度组件

```jsx
// CircularProgress.jsx
function CircularProgress({ value, max = 100, size = 120 }) {
  const percentage = (value / max) * 100;
  const strokeDashoffset = 283 - (283 * percentage) / 100;
  
  return (
    <div className="circular-progress" style={{ width: size, height: size }}>
      <svg viewBox="0 0 100 100">
        <circle className="track" cx="50" cy="50" r="45" />
        <circle 
          className="progress" 
          cx="50" 
          cy="50" 
          r="45"
          style={{ strokeDashoffset }}
        />
      </svg>
      <span className="value">{value}%</span>
    </div>
  );
}

// CSS
.circular-progress {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.circular-progress svg {
  transform: rotate(-90deg);
}

.circular-progress circle {
  fill: none;
  stroke-width: 8;
  stroke-linecap: round;
}

.track {
  stroke: rgba(255, 255, 255, 0.1);
}

.progress {
  stroke: linear-gradient(90deg, #667eea, #764ba2);
  stroke-dasharray: 283;
  transition: stroke-dashoffset 0.5s ease;
}

.value {
  position: absolute;
  font-size: 20px;
  font-weight: 600;
  color: white;
}
```

## Apple风格导航栏

```jsx
// GlassNav.jsx
function GlassNav({ items }) {
  return (
    <nav className="glass-nav">
      {items.map((item, index) => (
        <a key={index} href={item.href} className="nav-item">
          {item.label}
        </a>
      ))}
    </nav>
  );
}

// CSS
.glass-nav {
  display: flex;
  gap: 8px;
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(24px);
  border-radius: 32px;
  padding: 12px 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.nav-item {
  padding: 10px 20px;
  border-radius: 20px;
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
}

.nav-item:hover {
  background: rgba(255, 255, 255, 0.15);
  color: white;
}

.nav-item.active {
  background: rgba(255, 255, 255, 0.25);
  color: white;
}
```

## 数据卡片组件

```jsx
// DataCard.jsx
function DataCard({ title, value, trend, color }) {
  return (
    <div className="data-card">
      <div className="data-header">
        <span className="data-title">{title}</span>
        <span className={`data-trend ${trend >= 0 ? 'up' : 'down'}`}>
          {trend > 0 ? '+' : ''}{trend}%
        </span>
      </div>
      <div className="data-value" style={{ color }}>{value}</div>
    </div>
  );
}

// CSS
.data-card {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(12px);
  border-radius: 16px;
  padding: 20px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.data-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.data-title {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.6);
}

.data-trend {
  font-size: 12px;
  padding: 4px 8px;
  border-radius: 12px;
}

.data-trend.up {
  background: rgba(52, 211, 153, 0.2);
  color: #34d399;
}

.data-trend.down {
  background: rgba(248, 113, 113, 0.2);
  color: #f87171;
}

.data-value {
  font-size: 32px;
  font-weight: 700;
}
```

## 背景设置

```css
/* 渐变背景 + 暗色遮罩 */
.app-background {
  min-height: 100vh;
  background: 
    linear-gradient(135deg, rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.6)),
    url('/background.jpg') center/cover;
  background-attachment: fixed;
}
```
