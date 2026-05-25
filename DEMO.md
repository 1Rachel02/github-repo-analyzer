# 🎯 Demo & Usage Examples

## Quick Demo

```bash
# Install the tool
pip install -e .

# Analyze any GitHub repository
repo-analyzer analyze torvalds/linux

# With your GitHub token (recommended)
export GITHUB_TOKEN=your_token_here
repo-analyzer analyze microsoft/vscode -o vscode-report.md
```

## Example Output

When you run the analyzer, you'll see:

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

## Sample Analysis Report

The generated report includes:

### 📊 Executive Summary
- Overall health score with visual indicators
- Key metrics (stars, forks, watchers)
- Primary language and activity level
- Security assessment score

### 💻 Language Distribution
- Primary language identification
- Diversity score calculation
- Visual percentage breakdown

### 🔥 Activity Analysis
- Days since last push
- Activity level classification
- Recent commit analysis

### 👥 Community Health
- Documentation completeness (README, LICENSE, CONTRIBUTING)
- Governance files (Code of Conduct, Security Policy)
- Contributor engagement metrics

### 🔒 Security Assessment
- Security policy presence
- Identified security issues
- Recommendations for improvement

### 🧠 AI-Powered Insights
- **Strengths** — What the project does well
- **Weaknesses** — Areas needing attention
- **Recommendations** — Actionable next steps

## Advanced Usage

### Deep Analysis Mode
```bash
repo-analyzer analyze facebook/react --deep
```

### JSON Output
```bash
repo-analyzer analyze vuejs/vue -f json -o vue-data.json
```

### Compare Multiple Repos
```bash
repo-analyzer compare facebook/react vuejs/vue angular/angular
```

## Use Cases

1. **Before Adopting a Library** — Check if it's actively maintained
2. **Security Audits** — Identify missing security policies
3. **Competitive Analysis** — Compare similar projects
4. **Portfolio Documentation** — Generate professional reports for your repos
5. **Due Diligence** — Evaluate open source projects before integration

---

**Built for Xiaomi MiMo 100T Creator Program** 🚀
