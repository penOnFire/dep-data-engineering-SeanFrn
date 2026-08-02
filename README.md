# The AI Divide in Computer Studies Education

## Problem Statement

How does the financial barrier of premium AI coding tools impact the job readiness of Computer Studies students compared to working professionals?

## Target Audience

This project is intended for:

- Computer Studies students preparing to enter the workforce
- University curriculum directors and academic administrators evaluating whether access to premium AI coding tools should be provided to students

## Key Performance Indicator (KPI)

The primary KPI is the **Premium AI Adoption Gap**, defined as the difference in the adoption rate of premium AI coding tools between Computer Studies students and employed software developers.

## Data Source

This project uses the **Stack Overflow Annual Developer Survey 2025** dataset as its primary source. The survey is distributed as a static CSV dataset, making it suitable for reproducible analysis without requiring live API requests.

## Dashboard Goal

The dashboard will visualize differences in premium AI tool adoption between students and professional developers, highlighting whether financial barriers may affect students' job readiness. The insights can help universities determine whether institution-sponsored AI subscriptions are necessary to keep students competitive.

---

# Data Source Notes

## Primary Source

- **Name:** Stack Overflow Developer Survey (2025 Data)
- **URL:** https://www.kaggle.com/datasets/aliaslam25/stack-overflow-developer-survey-2025
- **Format:** CSV
- **Ingestion Strategy:** A Python script (`scripts/ingest.py`) uses the official Kaggle API to authenticate, download, and extract the dataset into the `data/raw/` directory.
- **Coverage:** Approximately 49,123 responses across 170 survey variables covering developer demographics, AI usage, employment, and development tools.
- **Why it fits the problem:**
  - Filter the `MainBranch` column to distinguish students from professional developers.
  - Analyze the `AIToolCurrentlyUsing` column to measure premium AI tool adoption.
  - Examine the `TechPurchase` or related purchasing variables to identify whether pricing influences AI tool adoption.
- **Known Limitations:**
  - Survey responses are self-reported.
  - Financial barriers must be inferred from survey responses rather than measured directly.
  - Results represent survey participants and may not generalize to all developers.

---

## Fallback Source

- **Name:** GitHub Innovation Graph – Developer Metrics
- **URL:** https://github.com/github/innovationgraph
- **Format:** CSV
- **Ingestion Strategy:** A Python script uses the `requests` library to download the latest public CSV datasets directly from the GitHub Innovation Graph repository.
- **Coverage:** Quarterly developer activity metrics across multiple economies.
- **Why it could still work:** If the Stack Overflow dataset becomes unavailable, GitHub Innovation Graph provides publicly accessible developer activity data that can serve as supporting context for developer engagement trends.
- **Known Limitations:**
  - Data is aggregated by country or region.
  - Does not distinguish students from professionals.
  - Does not directly measure premium AI tool usage.

---

# Data Ingestion (CI/CD Pipeline)

To provide a frictionless review experience, the data ingestion process is automated using **GitHub Actions**. Reviewers do not need to install Python or configure Kaggle credentials locally.

## Running the Pipeline (Reviewers)

1. Open the **Actions** tab in this GitHub repository.
2. Select **Automated Kaggle Ingestion Pipeline** from the list of workflows.
3. Click **Run workflow**, then select the green **Run workflow** button.
4. GitHub Actions will:
   - Launch a runner
   - Securely load the stored Kaggle credentials from GitHub Secrets
   - Execute `scripts/ingest.py`
5. After the workflow completes successfully, open the workflow run and download the generated dataset from the **Artifacts** section.

---

# Local Execution (Developers)

Developers who wish to run the ingestion pipeline locally can follow these steps.

## Prerequisites

- Python 3.8 or later
- A Kaggle account
- Kaggle API credentials

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. Configure Kaggle Credentials

Create a `.env` file in the project root:

```env
KAGGLE_USERNAME=your_username
KAGGLE_KEY=your_api_key
```

Alternatively, place the official `kaggle.json` file inside:

```
~/.kaggle/
```

and ensure the file has the correct permissions.

## 3. Run the Ingestion Script

```bash
python scripts/ingest.py
```

---

# Expected Output

After successful execution, the following files will be generated inside the `data/raw/` directory:

```
stack-overflow-2025-raw_<YYYY-MM-DD>.zip
ingestion_log.txt
```

### Output Files

**`stack-overflow-2025-raw_<YYYY-MM-DD>.zip`**

The original dataset downloaded directly from Kaggle.

**`ingestion_log.txt`**

A log containing:

- Download timestamp
- Dataset source
- Download status
- Output filename
