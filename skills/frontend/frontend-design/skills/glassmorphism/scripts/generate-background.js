const fs = require('fs');
const path = require('path');

/**
 * 生成简约风格背景图 - 使用SVG方式
 * 支持多种风格：渐变、几何图形、抽象波浪、柔和光晕
 */

// 预设配色方案 - 适合玻璃质感UI的背景
const colorSchemes = {
  // 深海蓝紫 - 适合金融/科技类
  deepOcean: {
    primary: ['#1a1a2e', '#16213e', '#0f3460'],
    accent: ['#e94560', '#533483', '#f39422'],
    type: 'gradient'
  },
  // 日落橙粉 - 适合社交/生活类
  sunset: {
    primary: ['#2d1b4e', '#1a1a2e', '#0f0f23'],
    accent: ['#ff6b6b', '#feca57', '#ff9ff3'],
    type: 'gradient'
  },
  // 森林绿 - 适合健康/自然类
  forest: {
    primary: ['#1a2f1a', '#0f1f0f', '#1a3a1a'],
    accent: ['#2ecc71', '#27ae60', '#1dd1a1'],
    type: 'gradient'
  },
  // 紫罗兰 - 适合创意/艺术类
  violet: {
    primary: ['#2d1b4e', '#1a0f2e', '#0f0518'],
    accent: ['#a29bfe', '#6c5ce7', '#fd79a8'],
    type: 'gradient'
  },
  // 冷灰蓝 - 适合商务/专业类
  coolGray: {
    primary: ['#1a1a2e', '#16213e', '#1f4068'],
    accent: ['#74b9ff', '#0984e3', '#00cec9'],
    type: 'gradient'
  }
};

/**
 * 生成SVG背景
 */
function generateSVGBackground(width, height, scheme, style) {
  const colors = scheme.primary;
  const accents = scheme.accent;
  
  let svgContent = '';
  
  // 基础渐变背景
  const gradientId = 'bgGradient';
  svgContent += `
    <defs>
      <linearGradient id="${gradientId}" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:${colors[0]}" />
        <stop offset="50%" style="stop-color:${colors[1]}" />
        <stop offset="100%" style="stop-color:${colors[2]}" />
      </linearGradient>
      
      <!-- 噪点滤镜 -->
      <filter id="noise">
        <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="4" stitchTiles="stitch" />
        <feColorMatrix type="saturate" values="0" />
        <feComponentTransfer>
          <feFuncA type="linear" slope="0.05" />
        </feComponentTransfer>
      </filter>
      
      <!-- 模糊滤镜 -->
      <filter id="blur" x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur in="SourceGraphic" stdDeviation="60" />
      </filter>
            <filter id="blurHeavy" x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur in="SourceGraphic" stdDeviation="100" />
      </filter>
    </defs>
    
    <!-- 背景矩形 -->
    <rect width="100%" height="100%" fill="url(#${gradientId})" />
  `;
  
  // 根据风格添加元素
  if (style === 'glows' || style === 'mixed') {
    // 添加柔和光晕
    const numGlows = 4;
    for (let i = 0; i < numGlows; i++) {
      const cx = 20 + Math.random() * 60;
      const cy = 20 + Math.random() * 60;
      const r = 15 + Math.random() * 20;
      const color = accents[i % accents.length];
      
      svgContent += `
        <circle cx="${cx}%" cy="${cy}%" r="${r}%" fill="${color}" opacity="0.15" filter="url(#blurHeavy)" />
      `;
    }
  }
  
  if (style === 'waves' || style === 'mixed') {
    // 添加波浪线条
    const waveColor = accents[0];
    for (let i = 0; i < 3; i++) {
      const y = 30 + i * 20;
      const opacity = 0.08 - i * 0.02;
      svgContent += `
        <path d="M0,${y}% Q25%,${y - 10}% 50%,${y}% T100%,${y}%" 
              stroke="${waveColor}" stroke-width="2" fill="none" opacity="${opacity}" filter="url(#blur)" />
      `;
    }
  }
  
  if (style === 'geometric' || style === 'mixed') {
    // 添加几何图形
    const numShapes = 5;
    for (let i = 0; i < numShapes; i++) {
      const x = 10 + Math.random() * 80;
      const y = 10 + Math.random() * 80;
      const size = 5 + Math.random() * 10;
      const color = accents[i % accents.length];
      const opacity = 0.1;
      
      svgContent += `
        <circle cx="${x}%" cy="${y}%" r="${size}%" fill="${color}" opacity="${opacity}" filter="url(#blur)" />
      `;
    }
  }
  
  // 添加噪点层
  svgContent += `
    <rect width="100%" height="100%" filter="url(#noise)" opacity="0.4" style="mix-blend-mode: overlay;" />
  `;
  
  const svg = `<?xml version="1.0" encoding="UTF-8"?>
<svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" xmlns="http://www.w3.org/2000/svg">
  ${svgContent}
</svg>`;
  
  return svg;
}

/**
 * 主生成函数
 */
function generateBackground(options = {}) {
  const {
    width = 1920,
    height = 1080,
    schemeName = null,
    outputPath = './background.svg',
    style = 'mixed'
  } = options;
  
  // 选择配色方案
  const schemeKeys = Object.keys(colorSchemes);
  const selectedScheme = schemeName && colorSchemes[schemeName] 
    ? colorSchemes[schemeName]
    : colorSchemes[schemeKeys[Math.floor(Math.random() * schemeKeys.length)]];
  
  // 确定实际风格
  const actualStyle = style === 'mixed' 
    ? ['glows', 'waves', 'geometric'][Math.floor(Math.random() * 3)]
    : style;
  
  // 生成SVG
  const svg = generateSVGBackground(width, height, selectedScheme, actualStyle);
  
  // 确保输出目录存在
  const outputDir = path.dirname(outputPath);
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }
  
  // 保存SVG文件
  fs.writeFileSync(outputPath, svg);
  
  return {
    path: outputPath,
    scheme: selectedScheme,
    style: actualStyle,
    dimensions: { width, height }
  };
}

// 命令行接口
if (require.main === module) {
  const args = process.argv.slice(2);
  const options = {};
  
  for (let i = 0; i < args.length; i += 2) {
    const key = args[i].replace('--', '');
    const value = args[i + 1];
    
    switch (key) {
      case 'width':
        options.width = parseInt(value);
        break;
      case 'height':
        options.height = parseInt(value);
        break;
      case 'scheme':
        options.schemeName = value;
        break;
      case 'output':
        options.outputPath = value;
        break;
      case 'style':
        options.style = value;
        break;
    }
  }
  
  const result = generateBackground(options);
  console.log(JSON.stringify(result, null, 2));
}

module.exports = { generateBackground, colorSchemes };
