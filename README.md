# Google Cloud Day Taipei '26 — ADK Multi-Agent Workshop

Google ADK v2.4.0 多智能體系統工作坊，包含三種 Workflow Agent 模式：Sequential、Parallel、Loop。

## 專案結構

```
Skills_Google/
├── adk-lab/                          # ADK 實作 Lab
│   ├── main.py                       # 三種 Workflow Agent 範例
│   ├── skills/research_skill/        # ADK Skills 範例
│   │   ├── SKILL.md
│   │   └── references/search_guide.md
│   └── .env                          # Gemini API Key 設定
├── Google_Cloud_Day_Taipei_26_ADK_Workshop.pdf  # 課程簡報
└── README.md
```

## 環境需求

- Python 3.13+
- `google-adk` v2.4.0
- Gemini API Key（免費方案可用）

## 快速開始

```bash
cd adk-lab
pip install google-adk
# 將 .env 中的 GEMINI_API_KEY 換成你的 Key
python main.py
```

## 三種 Workflow 類型

| 類型 | 流程 | 適用場景 |
|------|------|----------|
| Sequential | Extract → Analyze → Summarize | 線性資料處理管線 |
| Parallel | Market + Tech + Risk 並行分析 | 多面向同時分析 |
| Loop | Draft → Review → Fix（最多 3 次迭代） | 反覆改善直到品質達標 |

## 參考資源

- [Google ADK 官方文件](https://google.github.io/adk-docs/)
- [Gemini API 取得 Key](https://aistudio.google.com/apikey)
- [Google Cloud Skills Boost 原課程](https://www.cloudskillsboost.google/catalog_lab/125061)
