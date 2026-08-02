"""
Phase 2 — Data Ingestion
Kaggle API Ingestion Logic for Stack Overflow Dataset
"""

import os
import requests
from pathlib import Path

# Bootcamp's directory setup, upgraded to use pathlib
RAW_DATA_DIR = Path(__file__).parent.parent / "data" / "raw"

def get_kaggle_token():
    """Reads the Kaggle API Bearer token."""
    token_path = Path.home() / ".kaggle" / "access_token"
    with open(token_path, 'r') as f:
        token = f.read().strip()
    return token

def ingest():
    """Hits the Kaggle API to search and download the dataset."""
    token = get_kaggle_token()
    
    # 1. Search Kaggle (Week 5 Focus: Query Parameters & Headers)
    search_url = "https://www.kaggle.com/api/v1/datasets/list"
    search_term = "aliaslam25/stack-overflow-developer-survey-2025"
    
    params = {"search": search_term}
    headers = {"Authorization": f"Bearer {token}"}
    
    print(f"Searching Kaggle API for: '{search_term}'...")
    search_response = requests.get(search_url, params=params, headers=headers, timeout=30)
    search_response.raise_for_status() 
    
    # Parse JSON to get the official dataset reference
    datasets = search_response.json()
    dataset_ref = datasets[0]['ref']
    print(f"Found dataset: {dataset_ref}")

    # 2. Download the raw data
    download_url = f"https://www.kaggle.com/api/v1/datasets/download/{dataset_ref}"
    print(f"Downloading raw data from {download_url}...")
    
    download_response = requests.get(download_url, headers=headers, timeout=60, stream=True)
    download_response.raise_for_status()
    
    # 3. Save it to data/raw/
    output_file = RAW_DATA_DIR / "stack-overflow-2025-raw.zip"
    with open(output_file, 'wb') as f:
        for chunk in download_response.iter_content(chunk_size=8192):
            f.write(chunk)
            
    print(f"Success! Saved raw extract to {output_file}")

if __name__ == "__main__":
    # Ensure the directory exists
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    try:
        ingest()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except FileNotFoundError:
        print("Error: Could not find ~/.kaggle/access_token. Please ensure you saved the token.")
    except Exception as err:
        print(f"An error occurred: {err}")
        
    print("Ingestion script finished.")