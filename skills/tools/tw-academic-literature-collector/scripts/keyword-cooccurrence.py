# 關鍵字共現分析程式碼

## Python TF-IDF + 網絡分析實作

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx

def extract_keywords_and_cooccurrence(literature_data):
    """
    從文獻標題和摘要中萃取關鍵字並建立共現矩陣

    Args:
        literature_data: 文獻清單，每筆包含 title 和 abstract

    Returns:
        dict: 包含 keywords, cooccurrence matrix, network, communities
    """
    # 合併標題和摘要
    texts = [f"{lit['title']} {lit['abstract']}" for lit in literature_data]

    # TF-IDF 關鍵字萃取
    vectorizer = TfidfVectorizer(
        max_features=30,
        stop_words=chinese_stopwords,
        ngram_range=(1, 2)  # 支援單字和雙字詞
    )

    tfidf_matrix = vectorizer.fit_transform(texts)
    keywords = vectorizer.get_feature_names_out()

    # 計算關鍵字共現
    cooccurrence = (tfidf_matrix.T * tfidf_matrix).toarray()

    # 建立網絡圖資料
    G = nx.Graph()
    for i, kw1 in enumerate(keywords):
        for j, kw2 in enumerate(keywords):
            if i < j and cooccurrence[i][j] > 0.1:  # 閾值過濾
                G.add_edge(kw1, kw2, weight=cooccurrence[i][j])

    # 社群偵測 (識別主題群組)
    communities = nx.community.louvain_communities(G)

    return {
        'keywords': keywords,
        'cooccurrence': cooccurrence,
        'network': G,
        'communities': communities
    }

# 繁體中文停用詞列表
chinese_stopwords = [
    '的', '是', '在', '和', '與', '等', '及', '或', '但', '而',
    '了', '著', '者', '也', '將', '可', '能', '對', '於', '為',
    '有', '無', '此', '彼', '其', '之', '以', '為', '因', '果'
]
```

## Louvain 社群偵測演算法

識別主題群組的步驟：
1. 建立 TF-IDF 矩陣
2. 計算關鍵字共現矩陣
3. 使用 `nx.community.louvain_communities(G)` 進行社群偵測
4. 每組用不同顏色標示

## 關鍵字萃取參數

| 參數 | 值 | 說明 |
|------|-----|------|
| max_features | 30 | 提取前30個高頻關鍵字 |
| ngram_range | (1,2) | 支援單字和雙字詞 |
| 閾值 | 0.1 | 共現權重過濾門檻 |

## 網絡視覺化屬性

| 屬性 | 計算方式 |
|------|---------|
| 節點大小 | 關鍵字出現頻率 |
| 辮粗細 | 共現頻率 |
| 節點顏色 | 社群群組 (不同主題用不同色) |