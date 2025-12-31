import pandas as pd


def transform_data(raw_data):
    # Handles raw data
    df = pd.DataFrame(raw_data)

    # Create Full Name
    df["Full Name"] = df["first_name"] + " " + df["last_name"]

    # Drop unused name columns
    df.drop(columns=["first_name", "last_name"], inplace=True)

    # Designation logic
    def designation(exp):
        if exp < 3:
            return "System Engineer"
        elif 3 <= exp <= 5:
            return "Data Engineer"
        elif 5 < exp <= 10:
            return "Senior Data Engineer"
        else:
            return "Lead"

    df["designation"] = df["years_of_experience"].apply(designation)

    # Phone validation
    def validate_phone(phone):
        phone_str = str(phone)
        return phone_str if phone_str.isdigit() else "Invalid Number"

    df["phone"] = df["phone"].apply(validate_phone)

    # Data type enforcement
    df = df.astype({
        "email": "string",
        "gender": "string",
        "age": "int",
        "job_title": "string",
        "years_of_experience": "int",
        "salary": "int",
        "department": "string"
    })

    # Final column order
    final_columns = [
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

    df = df[final_columns]

    return df
