---
slug: "github-wattime-takehome"
title: "wattime-takehome"
repo: "justin-napolitano/wattime-takehome"
githubUrl: "https://github.com/justin-napolitano/wattime-takehome"
generatedAt: "2025-11-23T09:50:24.547994Z"
source: "github-auto"
---


# Technical Overview: Analysis of Global Methane Emissions from Rice Paddies

## Motivation

Methane (CH4) is a potent greenhouse gas with a global warming potential significantly greater than carbon dioxide over a 20-year horizon. The agricultural sector, particularly rice paddy cultivation, contributes approximately 8% of anthropogenic methane emissions. Accurate measurement of these emissions is critical for climate policy and mitigation efforts.

The United Nations Environment Programme and other agencies provide emission estimates, but discrepancies exist between traditional reporting methods and newer satellite-based approaches. Notably, the University of Malaysia published a report suggesting underreporting of methane emissions by the UN by about 16%. This project aims to critically analyze these claims by replicating their methodology, comparing datasets, and performing statistical tests.

## Problem Statement

Methane emission estimates rely on data sources that may be subject to manipulation or undercounting. The Food and Agricultural Organization (FAOSTAT) uses official government data, which may be inaccurate. Climate TRACE employs satellite imaging to estimate cultivated paddy areas, potentially offering more objective measurements but with its own limitations.

The challenge is to reconcile these datasets, quantify differences, and assess the validity of claims regarding underreporting.

## Project Composition and Implementation

### Data Sources

- **University of Malaysia Data:** Emission estimates from 2015 to 2021 extracted from an Excel file.
- **FAOSTAT Data:** Official methane emission data from FAO, also in Excel and CSV formats.
- **Geographic Data:** Country shapefiles and natural earth datasets used for spatial merging and visualization.

### Analytical Approach

- **Data Merging:** Emission data from different sources are merged on ISO3 country codes to enable direct comparison.
- **Difference Calculation:** Tonnes of methane emissions difference and percent differences are computed between datasets.
- **Visualization:** Horizontal bar plots visualize differences by country.
- **Statistical Testing:** Hypothesis tests (Shapiro-Wilk for normality, T-test, Mann-Whitney U) evaluate whether distributions and means differ significantly between years and datasets.

### Software and Tools

- Python scripts automate dependency installation and book building using `subprocess` to run shell commands.
- Jupyter Book organizes notebooks and markdown files into a cohesive, navigable report.
- Libraries like pandas, geopandas, matplotlib, folium, and scipy facilitate data manipulation, mapping, plotting, and statistics.

### Build Automation

A Python build pipeline script handles:

- Installing required Python packages from `requirements.txt`.
- Cleaning previous Jupyter Book builds.
- Building the HTML version of the book.
- (Partially implemented) Git operations to add, commit, and push changes.

This automation supports reproducibility and ease of updating the report.

## Interesting Implementation Details

- The use of Jupyter Book allows combining narrative, code, and output in a single document, enhancing reproducibility.
- Geographic merging uses coordinate reference system transformations to align shapefiles with emission data.
- Statistical tests are carefully chosen based on data distribution characteristics, reflecting sound methodological rigor.
- The build pipeline integrates command-line tools (`jupyter-book`) with Python subprocess calls, demonstrating a hybrid automation approach.

## Practical Notes

- Data paths in notebooks use absolute local paths, indicating the need for environment adaptation when sharing or deploying.
- Some build pipeline methods (commit, push) are incomplete and require finalization for full automation.
- The project focuses on transparency and replicability, emphasizing data provenance and method validation.

## Conclusion

This project serves as a technical reference for analyzing methane emission discrepancies in rice paddy cultivation. It combines data science, geographic information systems, and statistical analysis within a reproducible Jupyter Book framework. The approach and code provide a foundation for further research, refinement, and potential policy impact assessment.