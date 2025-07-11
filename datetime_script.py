import pandas as pd
import dateparser
from datetime import datetime
import math

INPUT_CSV = "IRE_Grief.csv"
OUTPUT_CSV = "out.csv"
TIME_COLUMNS = ["updated_year_main", "date_1"]  
UPDATED_COLUMS = ["extracted_year", "extracted_comment_date"]

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
    if years_ago < 0:
        return 0
    return years_ago

def process_csv(input_path, output_path, time_col, updated_col):
    df = pd.read_csv(input_path)

    if time_col not in df.columns:
        raise Exception(f"Column '{time_col}' not found in CSV")

    df[updated_col] = df[time_col].apply(convert_to_years_ago)
    
    df.to_csv(output_path, index=False)
    print(f"[+] Output written to {output_path}")

if __name__ == "__main__":
    for i in range(len(TIME_COLUMNS)):
        process_csv(INPUT_CSV, OUTPUT_CSV, TIME_COLUMNS[i], UPDATED_COLUMS[i])
