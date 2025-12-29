import requests
import logging
from time import sleep

URL = "https://api.slingacademy.com/v1/sample-data/files/employees.json"

def fetch_employee_data(retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(URL, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                logging.error(f"Failed with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Attempt {attempt+1}: {e}")
            sleep(2)
    return None
