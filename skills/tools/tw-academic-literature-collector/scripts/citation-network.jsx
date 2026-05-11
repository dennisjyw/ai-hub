# 引用網絡圖程式碼

## D3.js 力導向布局實作

```jsx
import React, { useEffect, useRef, useState } from 'react';
import * as d3 from 'd3';

const CitationNetwork = ({ literatureData }) => {
  const svgRef = useRef();
  const [selectedNode, setSelectedNode] = useState(null);

  useEffect(() => {
    if (!literatureData) return;

    // 文獻資料結構
    const nodes = literatureData.map(lit => ({
      id: lit.id,
      author: lit.author,
      year: lit.year,
      citations: lit.citations,
      grade: lit.grade
    }));

    const links = literatureData.links || [];

    // D3.js 力導向布局
    const simulation = d3.forceSimulation(nodes)
      .force("link", d3.forceLink(links).id(d => d.id).distance(100))
      .force("charge", d3.forceManyBody().strength(-300))
      .force("center", d3.forceCenter(400, 300));

    // SVG 繪製邏輯
    const svg = d3.select(svgRef.current);

    // 繪製連結
    const link = svg.selectAll("line")
      .data(links)
      .enter().append("line")
      .attr("stroke", "#999")
      .attr("stroke-width", d => Math.sqrt(d.strength));

    // 繪製節點
    const node = svg.selectAll("circle")
      .data(nodes)
      .enter().append("circle")
      .attr("r", d => 5 + Math.log(d.citations + 1) * 3)
      .attr("fill", d => getColorByYear(d.year))
      .call(drag(simulation))
      .on("click", (event, d) => setSelectedNode(d));

    // 更新位置
    simulation.on("tick", () => {
      link
        .attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);

      node
        .attr("cx", d => d.x)
        .attr("cy", d => d.y);
    });
  }, [literatureData]);

  const getColorByYear = (year) => {
    const colorScale = d3.scaleLinear()
      .domain([2015, 2020, 2025])
      .range(["#003f5c", "#58508d", "#bc5090"]);
    return colorScale(year);
  };

  const drag = (simulation) => {
    function dragstarted(event) {
      if (!event.active) simulation.alphaTarget(0.3).restart();
      event.subject.fx = event.subject.x;
      event.subject.fy = event.subject.y;
    }

    function dragged(event) {
      event.subject.fx = event.x;
      event.subject.fy = event.y;
    }

    function dragended(event) {
      if (!event.active) simulation.alphaTarget(0);
      event.subject.fx = null;
      event.subject.fy = null;
    }

    return d3.drag()
      .on("start", dragstarted)
      .on("drag", dragged)
      .on("end", dragended);
  };

  return (
    <div>
      <h2>文獻引用網絡圖</h2>
      <svg ref={svgRef} width={800} height={600} />
      {selectedNode && (
        <div className="info-panel">
          <h3>{selectedNode.author} ({selectedNode.year})</h3>
          <p>引用次數: {selectedNode.citations}</p>
          <p>文獻分級: {selectedNode.grade}</p>
        </div>
      )}
    </div>
  );
};

export default CitationNetwork;
```

## 網絡節點設計規則

| 屬性 | 規則 |
|------|------|
| 節點大小 | 依引用次數縮放：`5 + log(citations + 1) * 3` |
| 節點顏色 | 依年份漸層：深藍(2015-2018) → 紫(2019-2021) → 粉(2022-2025) |
| 節點標籤 | 第一作者姓氏 + 年份 |
| 辮粗細 | 共同引用次數 |
| 箭頭方向 | A引用B: A→B |

## 互動功能

- 滑鼠懸停：顯示完整引文資訊
- 點擊節點：高亮該文獻的所有引用/被引用關係
- 拖曳節點：調整網絡布局
- 縮放/平移：探索大型網絡
- 篩選器：按年份範圍、引用次數閾值、文獻分級篩選