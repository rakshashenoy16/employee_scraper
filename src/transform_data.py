# Contains all data cleaning and transformation logic
import pandas as pd

def transform_data(raw_data):
    # Convert raw JSON data into a Pandas DataFrame
    df = pd.DataFrame(raw_data)

    # Create Full Name
    df["Full Name"] = df["first_name"] + " " + df["last_name"]

    # Designation logic
    def designation(exp):
        if exp < 3:
            return "System Engineer"
        elif 3 <= exp <= 5:
            return "Data Engineer"
        elif 6 <= exp <= 10:
            return "Senior Data Engineer"
        else:
            return "Lead"

    df["designation"] = df["years_of_experience"].apply(designation)

    # Normalize phone numbers
    df["phone"] = df["phone"].apply(
        lambda x: x if str(x).isdigit() else "Invalid Number"
    )

    # Format hired_date if present
    if "hired_date" in df.columns:
        df["hired_date"] = pd.to_datetime(df["hired_date"]).dt.strftime("%Y-%m-%d")

    #  DROP RAW NAME COLUMNS (THIS IS THE KEY FIX)
    df.drop(columns=["first_name", "last_name"], inplace=True)

    # Select ONLY warehouse-ready columns
    df = df[
        [
            "id",
            "Full Name",
            "email",
            "phone",
            "gender",
            "age",
            "job_title",
            "years_of_experience",
            "designation",
            "salary",
            "department"
        ]
    ]

    return df
