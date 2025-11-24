---
slug: github-wattime-takehome-note-technical-overview
id: github-wattime-takehome-note-technical-overview
title: wattime-takehome
repo: justin-napolitano/wattime-takehome
githubUrl: https://github.com/justin-napolitano/wattime-takehome
generatedAt: '2025-11-24T18:49:13.913Z'
source: github-auto
summary: >-
  This repo is focused on analyzing global methane emissions from rice paddies
  using a Jupyter Book structure. It compares datasets from FAOSTAT and the
  University of Malaysia, replicates academic studies, and integrates geographic
  data.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

This repo is focused on analyzing global methane emissions from rice paddies using a Jupyter Book structure. It compares datasets from FAOSTAT and the University of Malaysia, replicates academic studies, and integrates geographic data.

### Key Features
- Compares methane emission methodologies.
- Replicates and tests academic findings.
- Merges geographic data using GeoPandas.
- Automates builds with Python scripts.

### Tech Stack
- Python 3, Jupyter Book
- Pandas, GeoPandas, Matplotlib, SciPy

### Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/justin-napolitano/wattime-takehome.git
   cd wattime-takehome/jupyter-book
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Build the Jupyter Book:
   ```bash
   python python_build.py
   ```

After building, open the HTML files in `jupyter-book/_build/html/` to view the content.

### Gotchas
- The build automation might not fully commit and push changes yet.
