"""
Setup configuration for QuickHooks (devtools-init package)
Automated git hooks manager for Python projects
Compatible with Python 3.6+ and older pip versions
"""
from setuptools import setup, find_packages
import os

# Read long description if available
long_description = "QuickHooks - Automated git hooks manager for Python projects. Zero-configuration tool inspired by pre-commit."
readme_path = os.path.join(os.path.dirname(__file__), "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="devtools-init",
    version="3.0.0",
    author="Dev Team",
    author_email="dev@example.com",
    description="QuickHooks - Automated git hooks manager for Python projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarcMPR/devtools-init",
    project_urls={
        "Bug Tracker": "https://github.com/MarcMPR/devtools-init/issues",
        "Documentation": "https://github.com/MarcMPR/devtools-init#readme",
        "Source Code": "https://github.com/MarcMPR/devtools-init",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Version Control :: Git",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    keywords="git hooks pre-commit code-quality automation quickhooks",
    python_requires=">=3.6",
    install_requires=[
        # No external dependencies for maximum compatibility
    ],
    extras_require={
        "dev": [],
    },
)
