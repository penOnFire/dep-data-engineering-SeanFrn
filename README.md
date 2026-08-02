# The AI Divide in Computer Studies Education

## Problem Statement

How does AI tool adoption differ between Computer Studies students and professional developers, and what insights can this provide about potential accessibility barriers to premium AI coding tools?

## Target Audience

This project is intended for:

- Computer Studies students preparing to enter the workforce.
- University curriculum directors and academic administrators evaluating whether access to AI coding tools should be provided to students.

## Key Performance Indicator (KPI)

The primary KPI is the **AI Tool Adoption Gap**, defined as the difference in AI coding tool adoption between Computer Studies students and professional developers.

## Data Source

This project uses the **Stack Overflow Annual Developer Survey 2025** dataset as its primary source. The survey is distributed as a static CSV dataset, making it suitable for reproducible analysis without requiring live API requests.

## Dashboard Goal

The dashboard will compare AI tool adoption between students and professional developers. The results will help identify whether significant differences exist in AI tool usage, providing evidence that may inform discussions about accessibility to modern AI development tools in higher education.

---

# Data Source Notes

## Primary Source

- **Name:** Stack Overflow Developer Survey (Official Public Release)
- **URL:** https://cdn.stackoverflow.co/files/jo7n4k8s/production/49915bfd46d0902c3564fd9a06b509d08a20488c.zip
- **Format:** CSV (downloaded as a ZIP archive)
- **Ingestion Strategy:** A Python script (`scripts/ingest.py`) uses the `requests` library to download the dataset directly from Stack Overflow's official CDN into the `data/raw/` directory. No authentication or API key is required.
- **Coverage:** Approximately 49,000 survey responses across roughly 170 variables covering developer demographics, employment, AI usage, and development practices.
- **Why it fits the problem:**
  - Use the `MainBranch` column to distinguish students from professional developers.
  - Analyze the `AITool` column to identify AI coding tools used by respondents.
  - Compare AI tool adoption rates between the two groups.
- **Known Limitations:**
  - Survey responses are self-reported.
  - The survey does not directly measure subscription costs or financial barriers.
  - Differences in adoption should be interpreted as indicators of accessibility rather than direct evidence of affordability.

---

## Fallback Source

- **Name:** GitHub Innovation Graph – Developer Metrics
- **URL:** https://github.com/github/innovationgraph
- **Format:** CSV
- **Ingestion Strategy:** A Python script downloads publicly available CSV files using the `requests` library.
- **Coverage:** Quarterly developer activity metrics across multiple economies.
- **Why it could still work:** Provides contextual developer activity trends if the primary survey becomes unavailable.
- **Known Limitations:**
  - Aggregated by country or region.
  - Does not distinguish students from professionals.
  - Does not measure AI tool adoption.

---

# Data Ingestion Instructions

The ingestion pipeline downloads the dataset directly from Stack Overflow's public CDN. No authentication or API configuration is required.

## Prerequisites

- Python 3.8 or later

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Ingestion Script

```bash
python scripts/ingest.py
```

## Expected Output

```
data/raw/
├── stack-overflow-raw_<YYYY-MM-DD>.zip
└── ingestion_log.txt
```

### Output Files

**stack-overflow-raw\_<YYYY-MM-DD>.zip**

The original Stack Overflow Developer Survey dataset downloaded directly from the official CDN.

**ingestion_log.txt**

Contains:

- Download timestamp
- Source URL
- Download status
- Output filename
