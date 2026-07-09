# Google Cloud Day Taipei '26 — Vibe Coding Challenge (703)

**ADK Agent Workflow Visualizer** — Vibe Coding Challenge Quest 參賽作品。

👉 **作品展示：** [https://ta-lang.github.io/adk-workflow-viz/](https://ta-lang.github.io/adk-workflow-viz/)

## 專案結構

```
Skills_Google/
├── index.html                       # Vibe Coding Challenge 作品（單一 HTML）
├── adk-lab/                         # ADK 實作 Lab（701 工作坊）
│   ├── main.py                      # 三種 Workflow Agent 範例
│   ├── skills/research_skill/       # ADK Skills 範例
│   │   ├── SKILL.md
│   │   └── references/search_guide.md
│   └── .env                         # Gemini API Key 設定
├── Google_Cloud_Day_Taipei_26_ADK_Workshop.pdf  # 課程簡報
├── vibecoding-challenges.csv        # Challenge 提示詞模板
└── README.md
```

## 作品說明

**Agent Workflow Visualizer** 是一個 AI 驅動的 Multi-Agent 工作流設計與可視化工具：

- **AI 驅動**：串接 Gemini API，輸入業務流程描述即可自動生成 Agent 工作流
- **三種架構**：支援 Sequential（線性）、Parallel（並行）、Loop（循環）三種模式
- **即時可視化**：使用 Mermaid.js 將工作流渲染為流程圖
- **模擬執行**：Gemini 模擬各 Agent 的執行過程，輸出詳細 Log

### 使用方式

1. 輸入 Gemini API Key（可從 [Google AI Studio](https://aistudio.google.com/apikey) 取得）
2. 描述一個業務流程（如：客戶訂單處理流程）
3. 選擇 Workflow 類型（Sequential / Parallel / Loop）
4. 點擊「Generate with Gemini」產生流程圖
5. 點擊「Simulate Run」模擬 Agent 執行

## 參考資源

- [Google ADK 官方文件](https://google.github.io/adk-docs/)
- [Gemini API 取得 Key](https://aistudio.google.com/apikey)
- [Google Cloud Skills Boost 原課程](https://www.cloudskillsboost.google/catalog_lab/125061)
