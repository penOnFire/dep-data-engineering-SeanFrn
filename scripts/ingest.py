"""
Phase 2 — Data Ingestion (Frictionless Public Version)
Official Stack Overflow CDN Ingestion Logic
"""

import time
import requests
from pathlib import Path
from datetime import datetime

# Bootcamp directory setup
RAW_DATA_DIR = Path(__file__).parent.parent / "data" / "raw"

def ingest():
    """Hits the official Stack Overflow public CDN with retries, timestamps, and logging."""
    
    # 1. Target URL (100% Public, NO API TOKEN REQUIRED)
    # Direct endpoint to the Stack Overflow production CDN for the raw survey data
    download_url = "https://cdn.stackoverflow.co/files/jo7n4k8s/production/49915bfd46d0902c3564fd9a06b509d08a20488c.zip"
    
    print(f"Targeting public Stack Overflow CDN at: {download_url}")

    # 2. Setup Timestamping (Week 6 Requirement)
    today_str = datetime.now().strftime("%Y-%m-%d")
    output_filename = f"stack-overflow-raw_{today_str}.zip"
    output_file = RAW_DATA_DIR / output_filename
    
    # 3. Download with Retries (Week 6 Requirement)
    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            print(f"Download attempt {attempt}/{max_retries}...")
            # No headers needed, purely public GET request
            download_response = requests.get(download_url, timeout=60, stream=True)
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