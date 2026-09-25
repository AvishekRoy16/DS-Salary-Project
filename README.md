# Data Science Salary Study

An archived learning project that adapts a public salary-estimation walkthrough and extends it with an India-focused exploratory workflow.

> **Status:** historical study (2022), not a maintained salary benchmark or production service. The stored datasets and notebook outputs have not been independently refreshed or reproduced in the current environment.

## What this repository contains

The repository has two distinct parts:

1. **Guided US salary-estimation project** — the root-level scraper, cleaning, modelling and Flask API files follow the public [PlayingNumbers data-science salary project](https://github.com/PlayingNumbers/ds_salary_proj). Its structure, documentation and reported results originate from that upstream project.
2. **India-focused extension** — `India-Data-Science/` contains a separate 2022 exploration of Indian data-science job listings, including collection, cleaning, exploratory analysis and model-development notebooks.

This distinction matters: the upstream project's reported model scores are not presented here as original results.

## India extension

The added workflow explores whether structured attributes from job listings can help describe variation in advertised salary estimates.

### Pipeline

```text
Glassdoor listings (historical scrape)
        |
        v
Cleaning and salary parsing
        |
        v
Role, location, company and skill features
        |
        v
Exploratory analysis
        |
        v
Regression experiments
```

The notebooks cover:

- parsing salary ranges and company metadata;
- extracting role, seniority, location and skill indicators;
- inspecting distributions and categorical relationships;
- comparing linear, regularised-linear and tree-based regression approaches.

The historical modelling notebook contains only 110 observations after cleaning. A single random train/test split on a dataset this small is not sufficient evidence for a reliable salary estimator. Stored scores should therefore be treated as exploratory notebook output, not current performance claims.

## Repository map

```text
.
|-- India-Data-Science/       # India-focused extension
|   |-- data_collection.py
|   |-- data_cleaning.ipynb
|   |-- EDA.ipynb
|   `-- model_building.ipynb
|-- FlaskAPI/                 # guided-project API example
|-- data_collection.py       # guided-project files
|-- data_cleaning.ipynb
|-- data_eda.ipynb
`-- Model_building.ipynb
```

CSV snapshots and serialized models remain in the history for study context. Do not load untrusted pickle files: Python pickle is not a safe interchange format.

## Reproducibility and responsible use

This repository is preserved as evidence of an early end-to-end learning exercise, but it is not currently reproducible without remediation:

- the scraper uses deprecated Selenium APIs and brittle page selectors;
- the collection source and website terms must be reviewed before any new scrape;
- dependencies are not pinned for the notebook workflows;
- the India sample is small and historical;
- no time-based or repeated cross-validation is provided;
- salary estimates may reflect selection bias and should not be used for employment decisions.

A production-quality rebuild would use a permitted, versioned data source; schema validation; a reproducible environment; leakage checks; repeated or time-aware validation; baseline comparisons; subgroup error analysis; and a documented model card.

## References and attribution

- Base walkthrough: [PlayingNumbers/ds_salary_proj](https://github.com/PlayingNumbers/ds_salary_proj)
- Scraper foundation referenced by the walkthrough: [arapfaik/scraping-glassdoor-selenium](https://github.com/arapfaik/scraping-glassdoor-selenium)
- Flask productionisation tutorial referenced by the walkthrough: [Productionize a Machine Learning Model with Flask and Heroku](https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2)

The upstream repository does not declare a licence. No new licence is asserted here over upstream material.
