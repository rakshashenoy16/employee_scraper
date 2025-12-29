import logging

from fetch_data import fetch_employee_data
from transform_data import transform_data


logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    data = fetch_employee_data()
    if not data:
        logging.error("Data fetch failed.")
        return

    transformed_df = transform_data(data)

    # Save ONLY transformed data
    transformed_df.to_csv("employee_cleaned.csv", index=False)

    logging.info("Employee data processed successfully.")

if __name__ == "__main__":
    main()
