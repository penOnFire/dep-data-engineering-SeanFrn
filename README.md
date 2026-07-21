# The AI Divide in Computer Studies Education

## Problem Statement

How does the financial barrier of premium AI coding tools impact the job readiness of Computer Studies students compared to working professionals?

## Audience

This project is for Computer Studies students entering the job market and university curriculum directors who need to understand if paid AI tools are becoming a mandatory barrier to entry.

## KPI or Key Metric

The main metric I want to track is the **Premium AI Adoption Gap** (the difference in usage rates of paid AI tools between students and employed developers).

## Likely Data Source

I will explore the Stack Overflow Annual Developer Survey 2025 dataset (https://www.kaggle.com/datasets/aliaslam25/stack-overflow-developer-survey-2025). This dataset will be downloaded and used as a **static CSV file**, as the survey results are released annually rather than updated live.

## Possible Final Dashboard

The dashboard should help the audience quickly see the gap in paid AI tool usage between students and professionals, allowing educators to decide if university-sponsored AI subscriptions are necessary to keep students competitive.

## Data Source Notes

### Primary Source

- **Name:** Stack Overflow Developer Survey (2025 Data)
- **URL:** https://www.kaggle.com/datasets/aliaslam25/stack-overflow-developer-survey-2025
- **Format:** CSV
- **Ingestion Strategy:** I will write a Python script (`scripts/ingest.py`) that uses the official `kaggle` Python API library to programmatically authenticate, download, and extract the dataset directly into my local `data/raw/` folder.
- **Coverage:** 49,123 rows × 170 columns covering global tech tool usage.
- **Why it fits the problem:** We will filter the `MainBranch` column to isolate students and cross-reference this with the `AIToolCurrentlyUsing` column to track adoption of premium tools. We will also analyze the `TechPurchase` metrics to see how often "Prohibitive pricing" is cited as a blocker.
- **Known limitations:** Data is self-reported. We must infer financial barriers from employment status and pricing sentiment.

### Fallback Source

- **Name:** GitHub Innovation Graph - Developer Metrics
- **URL:** https://github.com/github/innovationgraph
- **Format:** CSV / API
- **Ingestion Strategy:** I will use a Python script utilizing the `requests` library to fetch the quarterly metrics via the GitHub REST API or programmatically download the raw CSVs into the `data/raw/` folder.
- **Coverage:** Official quarterly metrics on developer activity, push events, and repository data spanning multiple economies.
- **Why it could still work:** If the primary data fails, this official repository from GitHub provides concrete, non-Kaggle data on developer activity that we can use as a proxy for engagement and tool adoption.
- **Known limitations:** Aggregated by economy/region rather than granular, individual student vs. professional survey responses.
