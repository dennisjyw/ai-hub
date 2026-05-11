# Excalidraw JSON Schema 參考

## 頂層結構

```typescript
interface ExcalidrawFile {
  type: "excalidraw";
  version: number;           // 永遠是 2
  source: string;            // "https://excalidraw.com"
  elements: ExcalidrawElement[];
  appState: AppState;
  files: Record<string, any>;
}

interface AppState {
  viewBackgroundColor: string; // Hex 顏色
  gridSize: number;            // 通常是 20
}
```

## 基礎元素屬性

```typescript
interface BaseElement {
  id: string;
  type: ElementType;
  x: number;
  y: number;
  width: number;
  height: number;
  strokeColor: string;
  backgroundColor: string;
  fillStyle: "solid" | "hachure" | "cross-hatch";
  strokeWidth: number;
  strokeStyle: "solid" | "dashed" | "dotted";
  roughness: number;
  opacity: number;
  groupIds: string[];
  seed: number;
  version: number;
  versionNonce: number;
  isDeleted: false;
  updated: number;  // Timestamp
}
```

## 元素類型

### Rectangle
```typescript
{
  type: "rectangle";
  roundness: { type: 3 };  // 圓角
  text?: string;
  fontSize?: number;
  fontFamily?: number;     // 1=Virgil, 2=Helvetica, 3=Cascadia
  textAlign?: "left" | "center" | "right";
  verticalAlign?: "top" | "middle" | "bottom";
}
```

### Arrow
```typescript
{
  type: "arrow";
  points: [number, number][];  // 相對座標陣列
  roundness: { type: 2 };      // 2 = 曲線箭頭
  startBinding: null;
  endBinding: null;
}
```

### Text
```typescript
{
  type: "text";
  text: string;
  fontSize: number;
  fontFamily: number;
  textAlign: "left" | "center" | "right";
  verticalAlign: "top" | "middle" | "bottom";
  roundness: null;
}
```

## 常用顏色

| 用途 | Hex |
|------|-----|
| 預設線條 | `#1e1e1e` |
| 淺藍（主要） | `#a5d8ff` |
| 淺綠（流程） | `#b2f2bb` |
| 黃色（重要） | `#ffd43b` |
| 淺紅（警示） | `#ffc9c9` |

## ID 生成

```javascript
const id = Date.now().toString(36) + Math.random().toString(36).substr(2);
```

## 座標系統

- 原點 `(0, 0)` 在左上角
- X 向右增加
- Y 向下增加
- 單位為像素

## 推薦間距

| 場景 | 間距 |
|------|------|
| 水平元素間距 | 200-300px |
| 垂直行間距 | 100-150px |
| 邊緣留白 | 50px |
