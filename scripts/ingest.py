"""
Phase 2 — Data Ingestion & Extraction (Frictionless Public Version)
Official Stack Overflow CDN Ingestion & Automatic Unzipping Logic
"""

import time
import zipfile
import requests
from pathlib import Path
from datetime import datetime

# Bootcamp directory setup
RAW_DATA_DIR = Path(__file__).parent.parent / "data" / "raw"

def ingest():
    """Hits the official Stack Overflow public CDN, extracts files, and logs."""
    
    # Direct endpoint to the Stack Overflow production CDN for the raw survey data
    download_url = "https://cdn.stackoverflow.co/files/jo7n4k8s/production/49915bfd46d0902c3564fd9a06b509d08a20488c.zip"
    
    print(f"Targeting public Stack Overflow CDN at: {download_url}")

    today_str = datetime.now().strftime("%Y-%m-%d")
    zip_filename = f"stack-overflow-raw_{today_str}.zip"
    zip_path = RAW_DATA_DIR / zip_filename
    
    # Download with Retries
    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            print(f"Download attempt {attempt}/{max_retries}...")
            download_response = requests.get(download_url, timeout=60, stream=True)
            download_response.raise_for_status()
            
            with open(zip_path, 'wb') as f:
                for chunk in download_response.iter_content(chunk_size=8192):
                    f.write(chunk)
                    
            print(f"Success! Saved raw zip extract to {zip_path}")
            break 
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt == max_retries:
                raise Exception("Max retries reached. Download failed.")
            print("Retrying in 3 seconds...")
            time.sleep(3)

    # Automatically extract individual files as requested by reviewer
    print("Extracting individual files to data/raw/...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(RAW_DATA_DIR)
    
    # Optional: remove the zip file if you only want individual files in raw, 
    # or keep it. Let's remove the zip so raw strictly contains individual files.
    zip_path.unlink()
    print("Extraction complete. Zip file cleaned up, leaving individual files.")

    # Logging
    log_file = RAW_DATA_DIR / "ingestion_log.txt"
    with open(log_file, "a") as f:
        f.write(f"[{datetime.now().isoformat()}] Downloaded and extracted contents from {download_url}\n")
    print(f"Logged source URL and timestamp to {log_file}")

if __name__ == "__main__":
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    try:
        ingest()
    except Exception as err:
        print(f"An error occurred: {err}")