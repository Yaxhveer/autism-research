import pandas as pd
import dateparser
from datetime import datetime
import math

# === CONFIG ===
INPUT_CSV = "out.csv"
OUTPUT_CSV = "out.csv"
TIME_COLUMN = "date_1"  # Replace with actual column name in your CSV

# === FUNCTION TO CONVERT TIME TO 'Xyr' FORMAT ===
def convert_to_years_ago(timestring):
    if not isinstance(timestring, str) or timestring.strip() == "":
        return 0
    
    if timestring.startswith("Updated"):
        timestring = timestring[len("Updated "):]

    dt = dateparser.parse(timestring)
    if not dt:
        return 0
    
    today = datetime.today()
    diff_years = (today - dt).days / 365
    years_ago = math.floor(diff_years)
    return years_ago

# === MAIN SCRIPT ===
def process_csv(input_path, output_path, time_col):
    df = pd.read_csv(input_path)

    if time_col not in df.columns:
        raise Exception(f"Column '{time_col}' not found in CSV")

    df["extracted_comment_date"] = df[time_col].apply(convert_to_years_ago)
    
    df.to_csv(output_path, index=False)
    print(f"[+] Output written to {output_path}")

# === RUN ===
if __name__ == "__main__":
    process_csv(INPUT_CSV, OUTPUT_CSV, TIME_COLUMN)
