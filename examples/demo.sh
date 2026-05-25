#!/bin/bash
# Demo script showing various analyzer capabilities

echo "🔍 GitHub Repository Analyzer - Demo"
echo "======================================"
echo ""

# Check if tool is installed
if ! command -v repo-analyzer &> /dev/null; then
    echo "❌ repo-analyzer not found. Installing..."
    pip install -e .
fi

echo "📊 Example 1: Analyze a popular repository"
echo "-------------------------------------------"
repo-analyzer analyze torvalds/linux -o examples/linux-report.md
echo ""

echo "📊 Example 2: Deep analysis"
echo "-------------------------------------------"
repo-analyzer analyze microsoft/vscode --deep -o examples/vscode-report.md
echo ""

echo "📊 Example 3: JSON output"
echo "-------------------------------------------"
repo-analyzer analyze facebook/react -f json -o examples/react-report.json
echo ""

echo "📊 Example 4: Compare multiple repositories"
echo "-------------------------------------------"
repo-analyzer compare facebook/react vuejs/vue angular/angular -o examples/framework-comparison.md
echo ""

echo "✅ Demo complete! Check the examples/ directory for generated reports."
