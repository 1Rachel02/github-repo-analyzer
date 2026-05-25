#!/usr/bin/env python3
"""CLI interface for GitHub Repository Analyzer"""

import click
import sys
from .github_client import GitHubClient
from .analyzer_engine import AnalyzerEngine
from .report_generator import ReportGenerator


@click.group()
@click.version_option(version="1.0.0")
def main():
    """AI-Powered GitHub Repository Analyzer
    
    Analyze any GitHub repository and get intelligent insights about:
    - Code complexity and quality
    - Dependencies and security
    - Project health metrics
    - AI-generated recommendations
    """
    pass


@main.command()
@click.argument('repo', required=True)
@click.option('--token', '-t', envvar='GITHUB_TOKEN', help='GitHub personal access token')
@click.option('--output', '-o', default='report.md', help='Output file path')
@click.option('--format', '-f', type=click.Choice(['markdown', 'json', 'both']), default='markdown')
@click.option('--deep', is_flag=True, help='Enable deep analysis (slower, more detailed)')
def analyze(repo, token, output, format, deep):
    """Analyze a GitHub repository
    
    REPO: Repository in format 'owner/repo' (e.g., 'torvalds/linux')
    
    Examples:
        repo-analyzer analyze torvalds/linux
        repo-analyzer analyze 1Rachel02/xiaomi --deep
        repo-analyzer analyze microsoft/vscode -o vscode-report.md
    """
    click.echo(f"🔍 Analyzing repository: {repo}")
    
    try:
        # Initialize components
        github = GitHubClient(token)
        analyzer = AnalyzerEngine(github)
        reporter = ReportGenerator()
        
        # Fetch repo data
        click.echo("📡 Fetching repository data...")
        repo_data = github.get_repo_info(repo)
        
        # Analyze
        click.echo("🧠 Running AI analysis...")
        analysis = analyzer.analyze(repo_data, deep=deep)
        
        # Generate report
        click.echo("📝 Generating report...")
        if format in ['markdown', 'both']:
            md_output = output if format == 'markdown' else output.replace('.json', '.md')
            reporter.generate_markdown(analysis, md_output)
            click.echo(f"✅ Markdown report saved to: {md_output}")
        
        if format in ['json', 'both']:
            json_output = output if format == 'json' else output.replace('.md', '.json')
            reporter.generate_json(analysis, json_output)
            click.echo(f"✅ JSON report saved to: {json_output}")
        
        # Print summary
        click.echo("\n" + "="*60)
        click.echo(f"📊 Analysis Summary for {repo}")
        click.echo("="*60)
        click.echo(f"⭐ Stars: {analysis['stars']:,}")
        click.echo(f"🍴 Forks: {analysis['forks']:,}")
        click.echo(f"📂 Primary Language: {analysis['language']}")
        click.echo(f"📈 Health Score: {analysis['health_score']}/100")
        click.echo(f"🔒 Security Score: {analysis['security_score']}/100")
        click.echo("="*60)
        
    except Exception as e:
        click.echo(f"❌ Error: {str(e)}", err=True)
        sys.exit(1)


@main.command()
@click.argument('repos', nargs=-1, required=True)
@click.option('--token', '-t', envvar='GITHUB_TOKEN', help='GitHub personal access token')
@click.option('--output', '-o', default='comparison.md', help='Output file path')
def compare(repos, token, output):
    """Compare multiple repositories
    
    REPOS: Multiple repositories in format 'owner/repo'
    
    Example:
        repo-analyzer compare facebook/react vuejs/vue angular/angular
    """
    if len(repos) < 2:
        click.echo("❌ Please provide at least 2 repositories to compare", err=True)
        sys.exit(1)
    
    click.echo(f"🔍 Comparing {len(repos)} repositories...")
    
    try:
        github = GitHubClient(token)
        analyzer = AnalyzerEngine(github)
        reporter = ReportGenerator()
        
        analyses = []
        for repo in repos:
            click.echo(f"📡 Analyzing {repo}...")
            repo_data = github.get_repo_info(repo)
            analysis = analyzer.analyze(repo_data, deep=False)
            analyses.append(analysis)
        
        click.echo("📝 Generating comparison report...")
        reporter.generate_comparison(analyses, output)
        click.echo(f"✅ Comparison report saved to: {output}")
        
    except Exception as e:
        click.echo(f"❌ Error: {str(e)}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
