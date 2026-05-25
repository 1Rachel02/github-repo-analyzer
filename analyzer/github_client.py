"""GitHub API client for fetching repository data"""

import requests
from typing import Dict, Optional, List


class GitHubClient:
    """Client for interacting with GitHub API"""
    
    BASE_URL = "https://api.github.com"
    
    def __init__(self, token: Optional[str] = None):
        self.token = token
        self.session = requests.Session()
        if token:
            self.session.headers.update({"Authorization": f"token {token}"})
        self.session.headers.update({"Accept": "application/vnd.github.v3+json"})
    
    def get_repo_info(self, repo: str) -> Dict:
        """Fetch comprehensive repository information
        
        Args:
            repo: Repository in format 'owner/repo'
            
        Returns:
            Dictionary containing repository data
        """
        owner, name = repo.split('/')
        
        # Main repo info
        repo_url = f"{self.BASE_URL}/repos/{owner}/{name}"
        repo_data = self._request(repo_url)
        
        # Languages
        languages = self._request(f"{repo_url}/languages")
        
        # Contributors
        contributors = self._request(f"{repo_url}/contributors", params={"per_page": 10})
        
        # Recent commits
        commits = self._request(f"{repo_url}/commits", params={"per_page": 10})
        
        # Issues and PRs
        issues = self._request(f"{repo_url}/issues", params={"state": "open", "per_page": 10})
        
        # Releases
        releases = self._request(f"{repo_url}/releases", params={"per_page": 5})
        
        # Community profile
        try:
            community = self._request(f"{repo_url}/community/profile")
        except:
            community = {}
        
        return {
            "repo": repo_data,
            "languages": languages,
            "contributors": contributors,
            "commits": commits,
            "issues": issues,
            "releases": releases,
            "community": community,
        }
    
    def _request(self, url: str, params: Optional[Dict] = None) -> Dict:
        """Make authenticated request to GitHub API"""
        response = self.session.get(url, params=params)
        
        if response.status_code == 404:
            raise ValueError(f"Repository not found or not accessible")
        elif response.status_code == 403:
            raise ValueError(f"Rate limit exceeded. Please provide a GitHub token.")
        elif response.status_code == 204:
            # No content - return empty dict for endpoints that may be empty
            return {}
        elif response.status_code != 200:
            raise ValueError(f"GitHub API error: {response.status_code}")
        
        return response.json() if response.text else {}
