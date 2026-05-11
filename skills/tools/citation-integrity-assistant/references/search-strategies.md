# 搜尋策略

## 學術期刊論文

```python
# 基本搜尋
"[作者] [年份] [標題關鍵字]" site:scholar.google.com OR doi.org OR jstor.org

# 若有 DOI，直接 fetch DOI 連結確認

# 中文文獻加入
site:airitilibrary.com OR handle.ncl.edu.tw OR cnki.net
```

## 智庫 / 政策報告

```python
# 主要智庫
"[作者] [標題關鍵字]" site:rand.org OR iiss.org OR brookings.edu OR csis.org

# 台灣智庫
site:indsr.org.tw

# 官方文件
搜尋發布機關官網
```

## 灰色文獻

```python
# 會議論文、工作文件
"[作者] [標題]" conference OR working paper OR SSRN

# SSRN
site:ssrn.com OR papers.ssrn.com
```

## 理論溯源搜尋

```python
# 找原始來源
"[theory name]" original source OR "first proposed" OR "introduced by"

# 安全研究領域
site:rand.org OR jstor.org OR tandfonline.com
```

## 搜尋技巧

1. **精確匹配**：使用引號包圍確切詞組
2. **布林邏輯**：AND / OR / NOT 組合
3. **站內搜尋**：`site:` 限定特定網站
4. **時間範圍**：限定發表年份
5. **DOI 驗證**：直接 fetch DOI 連結