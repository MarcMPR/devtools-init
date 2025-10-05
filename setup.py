"""
Setup configuration for devtools-init package
Compatible with Python 3.6+ and older pip versions
"""
from setuptools import setup, find_packages
import os

# Read long description if available
long_description = "Development tools initialization package for workspace setup"
readme_path = os.path.join(os.path.dirname(__file__), "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="devtools-init",
    version="1.0.0",
    author="Dev Team",
    author_email="dev@example.com",
    description="Development tools initialization for workspace setup",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/example/devtools-init",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
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
    ],
    python_requires=">=3.6",
    install_requires=[
        # No external dependencies for maximum compatibility
    ],
    extras_require={
        "dev": [],
    },
)
