#!/usr/bin/env python3
# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="local-mcp-py",
    version="0.1.0",
    author="AIGC-Open",
    author_email="aigc-open@gmail.com",
    description="A modular MCP (Model Context Protocol) server with various tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aigc-open/local-mcp-py",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "mcp>=1.0.0",
        "fire>=0.7.0",
    ],
    entry_points={},
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.900",
        ],
    },
    include_package_data=True,
    zip_safe=False,
) 