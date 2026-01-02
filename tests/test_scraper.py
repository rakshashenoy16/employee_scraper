# Unit tests for validating employee data scraper functionality

import unittest
from src.fetch_data import fetch_employee_data
from src.transform_data import transform_data


class TestEmployeeScraper(unittest.TestCase):

 
    # Test Case 1: Verify API Download
 
    def test_api_download(self):
        data = fetch_employee_data()
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)


    # Test Case 2: Verify JSON Extraction
   
    def test_json_extraction(self):
        data = fetch_employee_data()
        self.assertIsInstance(data, list)


    # Test Case 3: Validate JSON Format

    def test_json_format(self):
        data = fetch_employee_data()
        self.assertIsInstance(data[0], dict)


    # Test Case 4: Validate Required Columns

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

        for column in required_columns:
            self.assertIn(column, df.columns)


    # Test Case 5: Invalid Phone Handling (Simple Invalid)

    def test_invalid_phone_handling(self):
        mock_data = [
            {
                "id": 1,
                "first_name": "Test",
                "last_name": "User",
                "email": "test@example.com",
                "phone": "@123",
                "gender": "male",
                "age": 25,
                "job_title": "Engineer",
                "years_of_experience": 2,
                "salary": 5000,
                "department": "IT"
            },
            {
                "id": 2,
                "first_name": "Test2",
                "last_name": "User2",
                "email": "test2@example.com",
                "phone": "x456",
                "gender": "female",
                "age": 28,
                "job_title": "Analyst",
                "years_of_experience": 3,
                "salary": 6000,
                "department": "HR"
            }
        ]

        df = transform_data(mock_data)

        self.assertEqual(df.loc[0, "phone"], "Invalid Number")
        self.assertEqual(df.loc[1, "phone"], "Invalid Number")

    # Test Case 6: Valid Phone Retained

    def test_valid_phone_retained(self):
        mock_data = [
            {
                "id": 1,
                "first_name": "Valid",
                "last_name": "User",
                "email": "valid@example.com",
                "phone": "9876543210",
                "gender": "female",
                "age": 30,
                "job_title": "Developer",
                "years_of_experience": 5,
                "salary": 8000,
                "department": "IT"
            }
        ]

        df = transform_data(mock_data)

        self.assertEqual(df.loc[0, "phone"], "9876543210")

 
    # Test Case 7: Mixed Character Phone (Negative Scenario)

    def test_mixed_character_phone_invalid(self):
        mock_data = [
            {
                "id": 3,
                "first_name": "Mixed",
                "last_name": "Phone",
                "email": "mixed@example.com",
                "phone": "9@356!09-2",
                "gender": "male",
                "age": 32,
                "job_title": "Tester",
                "years_of_experience": 4,
                "salary": 7000,
                "department": "QA"
            }
        ]

        df = transform_data(mock_data)

        self.assertEqual(df.loc[0, "phone"], "Invalid Number")


if __name__ == "__main__":
    unittest.main()
