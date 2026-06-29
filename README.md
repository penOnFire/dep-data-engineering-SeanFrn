# The AI Divide in Computer Studies Education

## Problem Statement

I want to answer: "Is the software development industry becoming 'pay-to-win' for BSIT and CS students, and how does the inability to afford premium AI coding tools impact their job readiness compared to working professionals?"

## Audience

This project is for BSIT students entering the job market and university curriculum directors who need to understand if paid AI tools are becoming a mandatory barrier to entry.

## KPI or Key Metric

The main metric I want to track is the **Premium AI Adoption Gap** (the difference in usage rates of paid AI tools between students and employed developers).

## Likely Data Source

I will explore the Stack Overflow Annual Developer Survey (https://survey.stackoverflow.co/).

## Possible Final Dashboard

The dashboard should help the audience quickly see the gap in paid AI tool usage between students and professionals, allowing educators to decide if university-sponsored AI subscriptions are necessary to keep students competitive.

## Data Source Notes

### Primary Source

- **Name:** Stack Overflow Developer Survey (2025 Data)
- **URL:** https://www.kaggle.com/datasets/aliaslam25/stack-overflow-developer-survey-2025
- **Format:** CSV
- **Coverage:** 49,123 rows × 170 columns covering global tech tool usage.
- **Why it fits the problem:** We will filter the `MainBranch` column to isolate students and cross-reference this with the `AIToolCurrentlyUsing` column to track adoption of premium tools. We will also analyze the `TechPurchase` metrics to see how often "Prohibitive pricing" is cited as a blocker.
- **Known limitations:** Data is self-reported. We must infer financial barriers from employment status and pricing sentiment.

### Fallback Source

- **Name:** Global AI Tool Adoption Across Industries
- **URL:** https://www.kaggle.com/datasets/tfisthis/global-ai-tool-adoption-across-industries
- **Format:** CSV
- **Coverage:** Global AI tool adoption rates spanning 2023–2025, categorized by age group.
- **Why it could still work:** If the primary data fails, this dataset still allows us to track the adoption rates of specific paid AI tools across different age groups (acting as a proxy for students).
- **Known limitations:** The dataset is aggregated globally rather than raw, individual survey submissions.
