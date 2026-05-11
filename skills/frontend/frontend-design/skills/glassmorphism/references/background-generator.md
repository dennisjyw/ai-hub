# 背景图生成器使用指南

## 概述

背景图生成器用于创建与玻璃质感UI风格匹配的简约背景图。生成的背景图具有以下特点：
- 深色基调，突出玻璃卡片的透明效果
- 柔和的光晕和渐变，增加视觉层次
- 简约的几何元素，不抢夺前景注意力
- 轻微的噪点纹理，增加质感

## 使用方法

### 命令行调用

```bash
node scripts/generate-background.js [选项]
```

### 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `--width` | number | 1920 | 图片宽度 |
| `--height` | number | 1080 | 图片高度 |
| `--scheme` | string | random | 配色方案名称 |
| `--style` | string | mixed | 背景风格类型 |
| `--output` | string | ./background.png | 输出路径 |

### 配色方案

#### deepOcean - 深海蓝紫
适合金融、科技类产品
- 主色调：深蓝紫渐变
- 强调色：珊瑚红、紫色、橙色

#### sunset - 日落橙粉
适合社交、生活类产品
- 主色调：深紫到黑色渐变
- 强调色：珊瑚红、黄色、粉色

#### forest - 森林绿
适合健康、自然类产品
- 主色调：深绿色渐变
- 强调色：翠绿、青绿

#### violet - 紫罗兰
适合创意、艺术类产品
- 主色调：深紫色渐变
- 强调色：淡紫、紫红、粉红

#### coolGray - 冷灰蓝
适合商务、专业类产品
- 主色调：深蓝灰渐变
- 强调色：天蓝、深蓝、青色

### 风格类型

#### gradient
纯渐变背景，最简约

#### waves
抽象波浪线条，增加动感

#### geometric
几何图形装饰，现代感强

#### glows
柔和光晕效果，梦幻感

#### mixed
随机混合以上风格

## 代码示例

### 基础用法

```javascript
const { generateBackground } = require('./scripts/generate-background');

// 生成随机背景
const result = generateBackground({
  outputPath: './assets/background.png'
});

console.log(`背景已生成: ${result.path}`);
console.log(`使用配色: ${result.scheme}`);
```

### 指定配色方案

```javascript
const result = generateBackground({
  schemeName: 'deepOcean',
  style: 'glows',
  outputPath: './assets/background.png'
});
```

### 自定义尺寸

```javascript
const result = generateBackground({
  width: 2560,
  height: 1440,
  outputPath: './assets/background-2k.png'
});
```

## 与玻璃组件的配合

生成的背景图应该与玻璃卡片组件配合使用：

```css
.app-background {
  background-image: url('/assets/background.png');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

/* 添加暗色遮罩增强玻璃效果 */
.app-background::before {
  content: '';
  position: fixed;
  inset: 0;
  background: linear-gradient(
    135deg,
    rgba(20, 20, 30, 0.4) 0%,
    rgba(30, 30, 45, 0.5) 100%
  );
  pointer-events: none;
}
```

## 最佳实践

1. **配色协调**：背景强调色应与UI主色调呼应
2. **对比度**：确保背景与玻璃卡片有足够对比
3. **复杂度**：背景不宜过于复杂，避免干扰前景
4. **性能**：生成后应压缩图片，控制文件大小
5. **响应式**：建议生成多种尺寸适配不同设备

## 输出格式

生成器返回以下信息：

```json
{
  "path": "./background.png",
  "scheme": {
    "primary": ["#1a1a2e", "#16213e", "#0f3460"],
    "accent": ["#e94560", "#533483", "#f39422"],
    "type": "gradient"
  },
  "style": "glows",
  "dimensions": {
    "width": 1920,
    "height": 1080
  }
}
```
