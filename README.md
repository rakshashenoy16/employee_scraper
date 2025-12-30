# Employee Data Scraper

Fetches employee data from an API, cleans and transforms it, and exports a CSV.

## Setup
pip install -r requirements.txt

## Run
python src/main.py




# Option 2: Add logging to code (Professional PR)
In `main.py` or `fetch_data.py`, add logging.

# Example (main.py)
```python
import logging

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Employee scraper started")
