"""
RECORD CHECK  -  my version
===========================

Name  :ARAME BENI WINNER
Lane  :  AI
Date  :18/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = input("Dataset name: ")

value = float(input("Value: "))

limit = float(input("Limit: "))


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference = value - limit

percent = (value / limit) * 100


# Decide the status using if / elif / else

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 40)
print(f"  RECORD CHECK - {label}")
print("=" * 40)

print(f"{'Value':<20}: {value:>10.2f}")
print(f"{'Limit':<20}: {limit:>10.2f}")
print(f"{'Difference':<20}: {difference:>+10.2f}")
print(f"{'Percentage':<20}: {percent:>10.2f} %")
print(f"{'Status':<20}: {status:>10}")

print("=" * 40)

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
