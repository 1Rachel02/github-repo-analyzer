"""Core analysis engine with AI-powered insights"""

from typing import Dict
from datetime import datetime, timezone
import math


class AnalyzerEngine:
    """Analyzes repository data and generates insights"""
    
    def __init__(self, github_client):
        self.github = github_client
    
    def analyze(self, repo_data: Dict, deep: bool = False) -> Dict:
        """Perform comprehensive repository analysis
        
        Args:
            repo_data: Repository data from GitHub API
            deep: Enable deep analysis (more detailed, slower)
            
        Returns:
            Analysis results dictionary
        """
        repo = repo_data["repo"]
        
        # Basic metrics
        basic = self._analyze_basic_metrics(repo)
        
        # Language analysis
        languages = self._analyze_languages(repo_data["languages"])
        
        # Activity analysis
        activity = self._analyze_activity(repo, repo_data["commits"])
        
        # Community health
        community = self._analyze_community(repo, repo_data)
        
        # Security assessment
        security = self._analyze_security(repo, repo_data)
        
        # Calculate overall health score
        health_score = self._calculate_health_score(basic, activity, community, security)
        
        # Generate AI insights
        insights = self._generate_insights(repo, basic, languages, activity, community, security)
        
        return {
            "repo_name": repo["full_name"],
            "analyzed_at": datetime.now(timezone.utc).isoformat(),
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "watchers": repo["watchers_count"],
            "language": repo["language"] or "Unknown",
            "health_score": health_score,
            "security_score": security["score"],
            "basic_metrics": basic,
            "languages": languages,
            "activity": activity,
            "community": community,
            "security": security,
            "insights": insights,
        }
    
    def _analyze_basic_metrics(self, repo: Dict) -> Dict:
        """Analyze basic repository metrics"""
        return {
            "size_kb": repo["size"],
            "open_issues": repo["open_issues_count"],
            "has_wiki": repo["has_wiki"],
            "has_pages": repo["has_pages"],
            "has_downloads": repo["has_downloads"],
            "is_fork": repo["fork"],
            "is_archived": repo["archived"],
            "default_branch": repo["default_branch"],
            "created_at": repo["created_at"],
            "updated_at": repo["updated_at"],
            "pushed_at": repo["pushed_at"],
        }
    
    def _analyze_languages(self, languages: Dict) -> Dict:
        """Analyze language distribution"""
        if not languages:
            return {"primary": "Unknown", "distribution": {}, "diversity_score": 0}
        
        total = sum(languages.values())
        distribution = {lang: round(bytes / total * 100, 2) for lang, bytes in languages.items()}
        
        # Calculate diversity score (Shannon entropy)
        diversity = 0
        for percentage in distribution.values():
            p = percentage / 100
            if p > 0:
                diversity -= p * math.log2(p)
        
        diversity_score = min(100, int(diversity * 30))  # Normalize to 0-100
        
        return {
            "primary": max(languages, key=languages.get),
            "distribution": distribution,
            "diversity_score": diversity_score,
            "count": len(languages),
        }
    
    def _analyze_activity(self, repo: Dict, commits: list) -> Dict:
        """Analyze repository activity"""
        now = datetime.now(timezone.utc)
        last_push = datetime.fromisoformat(repo["pushed_at"].replace('Z', '+00:00'))
        days_since_push = (now - last_push).days
        
        # Activity score based on recency
        if days_since_push < 7:
            activity_level = "Very Active"
            activity_score = 100
        elif days_since_push < 30:
            activity_level = "Active"
            activity_score = 80
        elif days_since_push < 90:
            activity_level = "Moderate"
            activity_score = 60
        elif days_since_push < 180:
            activity_level = "Low"
            activity_score = 40
        else:
            activity_level = "Inactive"
            activity_score = 20
        
        return {
            "level": activity_level,
            "score": activity_score,
            "days_since_last_push": days_since_push,
            "recent_commits": len(commits),
        }
    
    def _analyze_community(self, repo: Dict, repo_data: Dict) -> Dict:
        """Analyze community health"""
        contributors = repo_data["contributors"]
        issues = repo_data["issues"]
        
        # Community metrics
        has_readme = repo_data["community"].get("files", {}).get("readme") is not None
        has_contributing = repo_data["community"].get("files", {}).get("contributing") is not None
        has_license = repo["license"] is not None
        has_code_of_conduct = repo_data["community"].get("files", {}).get("code_of_conduct") is not None
        
        # Calculate community score
        score = 0
        if has_readme: score += 25
        if has_license: score += 25
        if has_contributing: score += 20
        if has_code_of_conduct: score += 15
        if len(contributors) > 5: score += 15
        
        return {
            "score": min(100, score),
            "contributors_count": len(contributors),
            "has_readme": has_readme,
            "has_license": has_license,
            "has_contributing": has_contributing,
            "has_code_of_conduct": has_code_of_conduct,
            "open_issues_count": len(issues),
        }
    
    def _analyze_security(self, repo: Dict, repo_data: Dict) -> Dict:
        """Analyze security posture"""
        score = 50  # Base score
        issues = []
        
        # Check for security features
        if repo["license"]:
            score += 15
        else:
            issues.append("No license detected")
        
        if repo_data["community"].get("files", {}).get("code_of_conduct"):
            score += 10
        
        # Check for security policy
        if repo_data["community"].get("files", {}).get("security"):
            score += 15
        else:
            issues.append("No SECURITY.md file")
        
        # Check activity (stale repos are security risks)
        days_since_push = (datetime.now(timezone.utc) - 
                          datetime.fromisoformat(repo["pushed_at"].replace('Z', '+00:00'))).days
        if days_since_push < 90:
            score += 10
        else:
            issues.append(f"No updates in {days_since_push} days")
        
        return {
            "score": min(100, score),
            "issues": issues,
            "has_security_policy": repo_data["community"].get("files", {}).get("security") is not None,
        }
    
    def _calculate_health_score(self, basic: Dict, activity: Dict, 
                                community: Dict, security: Dict) -> int:
        """Calculate overall repository health score"""
        # Weighted average
        weights = {
            "activity": 0.35,
            "community": 0.30,
            "security": 0.25,
            "maintenance": 0.10,
        }
        
        maintenance_score = 0 if basic["is_archived"] else 100
        
        health = (
            activity["score"] * weights["activity"] +
            community["score"] * weights["community"] +
            security["score"] * weights["security"] +
            maintenance_score * weights["maintenance"]
        )
        
        return int(health)
    
    def _generate_insights(self, repo: Dict, basic: Dict, languages: Dict,
                          activity: Dict, community: Dict, security: Dict) -> Dict:
        """Generate AI-powered insights and recommendations"""
        strengths = []
        weaknesses = []
        recommendations = []
        
        # Analyze strengths
        if repo["stargazers_count"] > 1000:
            strengths.append(f"Popular project with {repo['stargazers_count']:,} stars")
        
        if activity["score"] >= 80:
            strengths.append("Actively maintained with recent updates")
        
        if community["score"] >= 80:
            strengths.append("Strong community health with proper documentation")
        
        if languages["diversity_score"] > 50:
            strengths.append(f"Diverse tech stack with {languages['count']} languages")
        
        # Analyze weaknesses
        if activity["score"] < 40:
            weaknesses.append("Low activity - project may be abandoned")
            recommendations.append("Consider reaching out to maintainers or forking")
        
        if not community["has_license"]:
            weaknesses.append("No license - unclear usage rights")
            recommendations.append("Add an appropriate open source license")
        
        if not community["has_contributing"]:
            weaknesses.append("No contribution guidelines")
            recommendations.append("Add CONTRIBUTING.md to encourage contributions")
        
        if security["score"] < 60:
            weaknesses.append("Security posture needs improvement")
            recommendations.append("Add SECURITY.md and enable security features")
        
        if basic["open_issues"] > 100:
            weaknesses.append(f"High number of open issues ({basic['open_issues']})")
            recommendations.append("Triage and close stale issues")
        
        # Default messages if none found
        if not strengths:
            strengths.append("Repository is functional and accessible")
        
        if not weaknesses:
            weaknesses.append("No major issues detected")
        
        if not recommendations:
            recommendations.append("Continue current maintenance practices")
        
        return {
            "strengths": strengths,
            "weaknesses": weaknesses,
            "recommendations": recommendations,
        }
