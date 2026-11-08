"""
RECORD CHECK  -  my version
===========================

Name  :ARAME BENI WINNER
Lane  :  AI
Date  :29-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def check_record(value, limit):
    """Calculate remaining rows, percentage and status."""
    difference = limit - value
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print the report for one dataset."""
    print()
    print("=" * 34)
    print(f"RECORD CHECK - {label}")
    print("=" * 34)

    print(f"Rows loaded: {value}")
    print(f"Rows expected: {limit}")
    print(f"Rows remaining: {difference}")
    print(f"Percentage: {percent:.2f}%")
    print(f"Status: {status}")

    print("=" * 34)


# ====================================================================== STORE
def load_records(path):
    """Read dataset records from a text file."""
    records = []

    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")

            record = {
                "label": label,
                "value": float(value),
                "limit": float(limit)
            }

            records.append(record)

    return records


records = load_records("TYPICAL.txt")



# =============================================================== PROCESS + OUTPUT
for record in records:
    difference, percent, status = check_record(
        record["value"],
        record["limit"]
    )

    print_report(
        record["label"],
        record["value"],
        record["limit"],
        difference,
        percent,
        status
    )

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
