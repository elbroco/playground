import pandas as pd


# Load the Excel file
excel_file = "data1.xlsx"
df = pd.read_excel(
    excel_file, sheet_name="Hoja1"
)  # Change 'Sheet1' to the sheet you want to read

# Save as CSV
csv_file = "data2.csv"
df.to_csv(csv_file, index=False)  # Set index=False to not write row numbers

df_eco = pd.read_csv("data2.csv", sep=",", header=0)
