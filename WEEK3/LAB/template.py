"""
RECORD CHECK  -  my version
===========================

Name  : ARAME BENI WINNER
Lane  :  AI
Date  :29/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def status_of(percent):
    """Return the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
def check(value, limit):
    """Return the remaining rows and percentage loaded."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent
# ==================================================================== INPUT
# Ask the user for the dataset name and row numbers

label = input("Dataset name: ")
value = float(input("Rows loaded: "))
limit = float(input("Rows expected: "))
# ================================================================== PROCESS
# Calculate the remaining rows and percentage loaded

difference, percent = check(value, limit)
# Determine the status
status = status_of(percent)

# =================================================================== OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK - {label}")
print("=" * 34)

print(f"{'Rows loaded':<20}: {value:>10.2f}")
print(f"{'Rows expected':<20}: {limit:>10.2f}")
print(f"{'Rows remaining':<20}: {difference:>10.2f}")
print(f"{'Percentage':<20}: {percent:>10.2f} %")
print(f"{'Status':<20}: {status:>10}")

print("=" * 34)

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
