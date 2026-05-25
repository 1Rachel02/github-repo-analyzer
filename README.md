# 🔍 AI-Powered GitHub Repository Analyzer

> **Intelligent repository analysis with AI-generated insights**

Analyze any GitHub repository and get comprehensive reports on code quality, security, community health, and actionable recommendations — all powered by AI.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![MiMo 100T](https://img.shields.io/badge/MiMo-100T%20Creator-orange.svg)](https://github.com/1Rachel02/xiaomi)

---

## ✨ Features

- 📊 **Comprehensive Metrics** — Stars, forks, languages, activity levels
- 🧠 **AI-Powered Insights** — Intelligent analysis of strengths, weaknesses, and recommendations
- 🔒 **Security Assessment** — Detect security issues and missing policies
- 👥 **Community Health** — Evaluate documentation, governance, and contributor engagement
- 📈 **Health Scoring** — Overall repository health score (0-100)
- 📝 **Multiple Formats** — Export reports as Markdown or JSON
- 🔄 **Comparison Mode** — Compare multiple repositories side-by-side

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/1Rachel02/github-repo-analyzer.git
cd github-repo-analyzer

# Install dependencies
pip install -r requirements.txt

# Install CLI tool
pip install -e .
```

### Basic Usage

```bash
# Analyze a repository
repo-analyzer analyze torvalds/linux

# Analyze with GitHub token (recommended for rate limits)
export GITHUB_TOKEN=your_token_here
repo-analyzer analyze microsoft/vscode

# Deep analysis (more detailed)
repo-analyzer analyze facebook/react --deep

# Custom output
repo-analyzer analyze vuejs/vue -o vue-report.md

# JSON format
repo-analyzer analyze angular/angular -f json

# Compare multiple repositories
repo-analyzer compare facebook/react vuejs/vue angular/angular
```

---

## 📊 Sample Output

```
🔍 Analyzing repository: torvalds/linux
📡 Fetching repository data...
🧠 Running AI analysis...
📝 Generating report...
✅ Markdown report saved to: report.md

============================================================
📊 Analysis Summary for torvalds/linux
============================================================
⭐ Stars: 180,234
🍴 Forks: 53,891
📂 Primary Language: C
📈 Health Score: 92/100
🔒 Security Score: 85/100
============================================================
```

### Generated Report Preview

The tool generates detailed markdown reports with:

- **Executive Summary** — Key metrics and overall health score
- **Language Distribution** — Visual breakdown of codebase languages
- **Activity Analysis** — Commit frequency and maintenance status
- **Community Health** — Documentation, governance, contributor metrics
- **Security Assessment** — Security policies and potential issues
- **AI Insights** — Strengths, weaknesses, and actionable recommendations

---

## 🔑 GitHub Token (Optional)

For better rate limits and private repo access:

1. Generate a token at [github.com/settings/tokens](https://github.com/settings/tokens)
2. Set it as environment variable:
   ```bash
   export GITHUB_TOKEN=your_token_here
   ```
3. Or create a `.env` file:
   ```
   GITHUB_TOKEN=your_token_here
   ```

---

## 🛠️ Tech Stack

- **Python 3.8+** — Core language
- **Click** — CLI framework
- **Requests** — GitHub API client
- **AI Analysis** — Custom scoring algorithms and insight generation

---

## 📖 Use Cases

- **Due Diligence** — Evaluate open source projects before adoption
- **Security Audits** — Identify security gaps in repositories
- **Project Health** — Monitor maintenance status of dependencies
- **Competitive Analysis** — Compare similar projects
- **Portfolio Showcase** — Generate professional reports for your projects

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest features
- Submit pull requests

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details

---

## 🏆 Built For

This project is part of the **Xiaomi MiMo 100T Creator Program** — showcasing AI-powered developer tools.

**Author:** [TiusLauren](https://github.com/1Rachel02)

---

## 🔗 Links

- [GitHub Repository](https://github.com/1Rachel02/github-repo-analyzer)
- [MiMo Campaign](https://github.com/1Rachel02/xiaomi)
- [Report Issues](https://github.com/1Rachel02/github-repo-analyzer/issues)

---

**Made with ❤️ and AI**
