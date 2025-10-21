import os
from setuptools import setup, find_packages

setup(
    name="ai-persona-wrapper",
    version="1.0.0",
    packages=find_packages(where="src/python"),
    package_dir={"": "src/python"},
    install_requires=[
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
        "fastapi>=0.100.0",
        "uvicorn>=0.23.0",
        "pydantic>=2.1.0",
        "tiktoken>=0.4.0",
        "python-jose[cryptography]>=3.3.0",
        "pytest>=7.4.0",
        "httpx>=0.24.1",
        "tenacity>=8.2.2",
        "structlog>=23.1.0"
    ],
    extras_require={
        "dev": [
            "black>=23.7.0",
            "isort>=5.12.0",
            "mypy>=1.5.0",
            "pytest-cov>=4.1.0",
            "bandit>=1.7.5",
        ]
    },
    python_requires=">=3.9",
)