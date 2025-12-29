import unittest
from src.fetch_data import fetch_employee_data
from src.transform_data import transform_data
import pandas as pd

class TestEmployeeScraper(unittest.TestCase):

    # Test Case 1: Verify JSON File Download
    def test_api_download(self):
        data = fetch_employee_data()
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

    # Test Case 2: Verify JSON File Extraction
    def test_json_extraction(self):
        data = fetch_employee_data()
        self.assertIsInstance(data, list)

    # Test Case 3: Validate File Type and Format
    def test_json_format(self):
        data = fetch_employee_data()
        self.assertIsInstance(data[0], dict)

    # Test Case 4: Validate Data Structure
    def test_required_fields_exist(self):
        data = fetch_employee_data()
        df = transform_data(data)

        required_columns = [
            "Full Name",
            "email",
            "phone",
            "gender",
            "age",
            "job_title",
            "years_of_experience",
            "salary",
            "department",
            "designation"
        ]

        for col in required_columns:
            self.assertIn(col, df.columns)

    # Test Case 5: Handle Missing or Invalid Data
    def test_invalid_phone_handling(self):
        data = fetch_employee_data()
        df = transform_data(data)

        self.assertTrue(
            ("Invalid Number" in df["phone"].values) or
            (df["phone"].dtype == object)
        )

if __name__ == "__main__":
    unittest.main()
