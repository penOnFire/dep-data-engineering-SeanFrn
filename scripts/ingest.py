"""
Phase 2 — Data Ingestion (Week 6 Hardened Version)
Kaggle API Ingestion Logic for Stack Overflow Dataset
"""

import os
from dotenv import load_dotenv
import time
import requests
from pathlib import Path
from datetime import datetime

# Load the environment variables from the .env file in the root folder
load_dotenv()

# Bootcamp directory setup
RAW_DATA_DIR = Path(__file__).parent.parent / "data" / "raw"

def get_kaggle_token():
    """Securely reads the Kaggle API Bearer token from the .env file."""
    token = os.getenv("KAGGLE_BEARER_TOKEN")
    if not token:
        raise ValueError("Missing Kaggle Token! Please set KAGGLE_BEARER_TOKEN in your .env file.")
    return token.strip()

def ingest():
    """Hits the Kaggle API with retries, timestamps, and logging."""
    token = get_kaggle_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    # 1. Search Kaggle to get the official dataset reference
    search_term = "aliaslam25/stack-overflow-developer-survey-2025"
    search_url = "https://www.kaggle.com/api/v1/datasets/list"
    
    print(f"Searching Kaggle API for: '{search_term}'...")
    search_response = requests.get(search_url, params={"search": search_term}, headers=headers, timeout=30)
    search_response.raise_for_status() 
    
    dataset_ref = search_response.json()[0]['ref']
    download_url = f"https://www.kaggle.com/api/v1/datasets/download/{dataset_ref}"
    print(f"Found dataset. Target URL: {download_url}")

    # 2. Setup Timestamping (Week 6 Requirement)
    today_str = datetime.now().strftime("%Y-%m-%d")
    output_filename = f"stack-overflow-2025-raw_{today_str}.zip"
    output_file = RAW_DATA_DIR / output_filename
    
    # 3. Download with Retries (Week 6 Requirement)
    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            print(f"Download attempt {attempt}/{max_retries}...")
            download_response = requests.get(download_url, headers=headers, timeout=60, stream=True)
            download_response.raise_for_status()
            
            with open(output_file, 'wb') as f:
                for chunk in download_response.iter_content(chunk_size=8192):
                    f.write(chunk)
                    
            print(f"Success! Saved raw extract to {output_file}")
            break # Exit the retry loop on success
            
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt == max_retries:
                raise Exception("Max retries reached. Download failed.")
            print("Retrying in 3 seconds...")
            time.sleep(3)

    # 4. Source Logging (Week 6 Requirement)
    log_file = RAW_DATA_DIR / "ingestion_log.txt"
    with open(log_file, "a") as f:
        f.write(f"[{datetime.now().isoformat()}] Downloaded {output_filename} from {download_url}\n")
    print(f"Logged source URL and timestamp to {log_file}")

if __name__ == "__main__":
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    try:
        ingest()
    except Exception as err:
        print(f"An error occurred: {err}")