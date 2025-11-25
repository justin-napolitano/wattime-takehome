---
slug: github-wattime-takehome
id: github-wattime-takehome
title: Analyzing Global Methane Emissions with Jupyter Book
repo: justin-napolitano/wattime-takehome
githubUrl: https://github.com/justin-napolitano/wattime-takehome
generatedAt: '2025-11-24T21:36:47.406Z'
source: github-auto
summary: >-
  Explore a Jupyter Book project that analyzes global methane emissions from
  rice paddies using various data sources and methodologies.
tags:
  - jupyter-book
  - python
  - geopandas
  - git
  - matplotlib
  - faostat
seoPrimaryKeyword: jupyter book methane emissions analysis
seoSecondaryKeywords:
  - methane emission datasets
  - data visualization
  - geographic data integration
  - build automation
  - academic replication studies
seoOptimized: true
topicFamily: null
topicFamilyConfidence: null
kind: project
entryLayout: project
showInProjects: true
showInNotes: false
showInWriting: false
showInLogs: false
---

This repository contains a Jupyter Book project analyzing global methane emissions from rice paddies. The work compares estimation methodologies, replicates academic studies, and explores geographic data integration to better understand discrepancies in methane emission reporting.

## Features

- Comparative analysis of methane emission datasets from FAOSTAT and University of Malaysia
- Replication and hypothesis testing of academic papers on methane emissions
- Geographic data merging and visualization using shapefiles and geopandas
- Automated build and dependency management pipelines using Python scripts
- Jupyter Book structure for organized presentation of notebooks and blog posts

## Tech Stack

- Python 3
- Jupyter Notebook / Jupyter Book
- Pandas, GeoPandas, Matplotlib, Folium
- SciPy for statistical testing
- subprocess module for build automation
- GitHub for version control and hosting

## Getting Started

### Prerequisites

- Python 3 environment
- pip package manager

### Installation

1. Clone the repository:

```bash
git clone https://github.com/justin-napolitano/wattime-takehome.git
cd wattime-takehome/jupyter-book
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Build the Jupyter Book

Run the included Python build script to clean and build the book:

```bash
python python_build.py
```

This script automates cleaning old builds, building HTML outputs, and managing Git commits and pushes.

### Viewing the Book

Open the generated HTML files in `jupyter-book/_build/html/` with a browser to navigate the notebooks and blog posts.

## Project Structure

```
wattime-takehome/
├── jupyter-book/                 # Jupyter Book source files
│   ├── notebooks/                # Analysis and blog notebooks
│   ├── _config.yml               # Book configuration
│   ├── _toc.yml                  # Table of contents
│   ├── index.md                  # Introduction and overview
│   └── python_build.py           # Build automation script
├── wattime-takehome-submission/ # (Assumed) submission files or deliverables
├── python_build.py               # Possibly duplicate or main build script
└── requirements.txt              # Python dependencies
```

## Future Work / Roadmap

- Complete implementation of build automation (commit and push methods appear incomplete)
- Add detailed documentation and comments to build scripts
- Expand geographic data analysis and visualization
- Automate data updates and integration pipelines
- Include more comprehensive testing and validation of statistical analyses
- Publish the Jupyter Book online with continuous integration

---

*Note: Some assumptions were made about missing documentation and project structure based on file contents and naming conventions.*
