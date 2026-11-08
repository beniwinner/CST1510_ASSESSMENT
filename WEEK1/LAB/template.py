# RECORD CHECK - AI / DATA SCIENCE
# Name: ARAME BENI WINNER
# Lane: AI
# Date: 05/12/2003

# ==================================================================== INPUT
# Ask the user for the three values
dataset_name = input("Dataset name: ")
rows_loaded = float(input("Rows loaded: "))
rows_expected = float(input("Rows expected: "))

# ================================================================== PROCESS
# Calculate the number of rows remaining
difference = rows_expected - rows_loaded
# Calculate the percentage of rows loaded
percent = (rows_loaded / rows_expected) * 100
# Calculate the percentage of rows still missing
missing_percent = (difference / rows_expected) * 100
# =================================================================== OUTPUT
# Display the report
print()
print("=" * 34)
print(f"  RECORD CHECK - {dataset_name}")
print("=" * 34)
print(f"  Rows loaded         : {rows_loaded:>10.2f}")
print(f"  Rows expected       : {rows_expected:>10.2f}")
print(f"  Rows remaining      : {difference:>+10.2f}")
print(f"  Loaded percentage   : {percent:>10.2f} %")
print(f"  Missing percentage  : {missing_percent:>10.2f} %")
print("=" * 34)