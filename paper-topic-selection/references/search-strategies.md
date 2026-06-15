# 检索策略模板

## 通用检索式构建方法

### 框架：PICO/PEO 适配

| 要素 | 英文 | 中文 | 说明 |
|------|------|------|------|
| P | Population | 研究对象 | 谁/什么 |
| I/E | Intervention/Exposure | 干预/暴露 | 做了什么 |
| C | Comparison | 对照 | 和什么比 |
| O | Outcome | 结果 | 得出什么 |

### 检索式组合策略

```
# 基础检索式
("核心概念1" OR "同义词1") AND ("核心概念2" OR "同义词2") AND ("时间限定")

# 扩大检索
- 减少 AND 连接的概念
- 增加同义词用 OR 连接
- 使用截断符 * (如 comput* 匹配 computer, computing)

# 精确检索
- 增加限定字段（标题/摘要）
- 增加时间范围
- 限定文献类型（综述/实证研究）
```

---

## 各平台检索要点

### Google Scholar（无需登录，优先使用）
```
site:scholar.google.com "关键词" 文件类型:pdf
优势：覆盖面广，可查引用链
局限：质量参差不齐，需筛选
```

### Semantic Scholar（无需登录）
```
https://www.semanticscholar.org/search?q=关键词
优势：AI辅助摘要，影响力评分
局限：偏计算机/生物医学
```

### arXiv（无需登录）
```
https://arxiv.org/search/?query=关键词&searchtype=all
优势：最新预印本，计算机科学首选
局限：未经同行评审
```

### PubMed（无需登录）
```
("关键词"[Title/Abstract]) AND ("2020/01/01"[Date - Publication] : "2025/12/31"[Date - Publication])
优势：生物医学权威，MeSH词表精准
局限：仅限生物医学
```

### Web of Science（可能需要登录）
```
TI=(关键词1) AND TI=(关键词2) AND PY=(2020-2025)
优势：引文分析强大，JCR分区
局限：需要机构订阅
```

### CNKI / 万方 / 维普（中文数据库，可能需要登录）
- CNKI: 主题=关键词 AND 年 Between (2020, 2025)
- 注意：核心期刊（CSSCI/CSCD）优先

### Scopus（可能需要登录）
```
TITLE-ABS-KEY(关键词1 AND 关键词2) AND PUBYEAR > 2019
优势：覆盖面最广的国际数据库
局限：需要机构订阅
```

---

## 检索顺序建议

1. **第一轮**：Google Scholar + Semantic Scholar（快速摸底）
2. **第二轮**：学科专业数据库（PubMed / arXiv / WoS / Scopus）
3. **第三轮**：引文滚雪球（从综述文章的参考文献回溯）
4. **第四轮**：中文数据库补充（如研究问题有中国情境）

---

## 检索记录表模板

| 编号 | 平台 | 检索式 | 语言 | 结果数 | 有效数 | 备注 |
|------|------|--------|------|--------|--------|------|
| | | | | | | |

---

## 灰色文献检索

除了期刊论文，还应检索：
- **学位论文**：ProQuest / CNKI 博士论文库（了解已有研究范围）
- **预印本**：arXiv / bioRxiv / medRxiv（获取最新进展）
- **技术报告**：Google 搜索 filetype:pdf + 机构名
- **行业报告**：艾瑞 / Gartner / McKinsey（现实源）
