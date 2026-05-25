from setuptools import setup, find_packages

setup(
    name="repo-analyzer",
    version="1.0.0",
    description="AI-powered GitHub repository analyzer with intelligent insights",
    author="TiusLauren",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
        "requests>=2.28.0",
        "pygments>=2.14.0",
        "tabulate>=0.9.0",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "repo-analyzer=analyzer.cli:main",
        ],
    },
    python_requires=">=3.8",
)
