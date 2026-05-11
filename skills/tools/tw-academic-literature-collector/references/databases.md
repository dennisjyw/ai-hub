# 資料庫搜尋策略

## 可直接搜尋的資料庫

### Google Scholar
- 使用 `web_search` 工具直接搜尋繁體中文學術文獻
- 搜尋語法範例：
  ```python
  # 繁體中文學術文獻搜尋
  search_query = f'"{keyword_tw}" 台灣 繁體 site:scholar.google.com'
  
  # 特定年份範圍
  search_query = f'"{keyword}" 2020..2025 site:scholar.google.com'
  
  # 特定期刊
  search_query = f'"{keyword}" source:"期刊名稱" site:scholar.google.com'
  ```

## 需要登入/付費訪問的資料庫

提供搜尋指引，由使用者自行執行：

### 全國碩博士論文網
- 網址：https://ndltd.ncl.edu.tw/
- 搜尋指引格式：
  ```
  建議搜尋式: [生成的關鍵字]
  篩選條件:
    - 學位別: □博士 ☑碩士
    - 學院: 社會科學學院
    - 年份: 2015-2025
  ```

### 華藝線上圖書館 Airiti Library
- 網址：https://www.airitilibrary.com/
- 搜尋指引格式：
  ```
  文獻類型: ☑期刊論文 ☑研討會論文
  篩選條件:
    - 學科分類: 社會科學
    - 語言: 繁體中文
  ```

### 臺灣人文及社會科學引文索引資料庫 TCI-HSS
- 網址：https://tci.ncl.edu.tw/
- 核心期刊優先：☑TSSCI ☑THCI

## 多語言搜尋策略

根據社會科學研究特性，生成：
- 繁體中文關鍵字組合（主要）
- 簡體中文關鍵字（補充搜尋）
- 英文關鍵字（國際文獻）
- 布林邏輯搜尋式（AND, OR, NOT）

範例：
```
主題: 人工智慧教育應用
繁中關鍵字: "人工智慧" AND "教育應用" OR "AI教學"
簡中關鍵字: "人工智能" AND "教育应用"
英文關鍵字: "artificial intelligence" AND "education" OR "AI in teaching"
```

## 支援領域

- 教育學 (Education)
- 社會學 (Sociology)
- 心理學 (Psychology)
- 政治學 (Political Science)
- 傳播學 (Communication)
- 公共行政 (Public Administration)
- 社會工作 (Social Work)