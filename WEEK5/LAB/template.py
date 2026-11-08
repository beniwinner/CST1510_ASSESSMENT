"""
RECORD CHECK  -  my version
===========================

Name  :arame beni winner
Lane  : ai
Date  :29-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS

class Record:
    def __init__(self, label, value, limit):
        """Store the dataset information."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status based on the percentage."""
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"




# ======================================================================RECORDS

def load_records(path):
    """Read records from a file and return Record objects."""
    records = []

    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")

            record = Record(
                label,
                float(value),
                float(limit)
            )

            records.append(record)

    return records


records = load_records("results.txt")


# ==================================================================== OUTPUT
over_limit_count = 0

for record in records:
    status = record.status()

    print()
    print("=" * 34)
    print(f"RECORD CHECK - {record.label}")
    print("=" * 34)

    print(f"Rows loaded: {record.value}")
    print(f"Rows expected: {record.limit}")
    print(f"Status: {status}")

    print("=" * 34)

    if status == "OVER LIMIT":
        over_limit_count += 1


print()
print("=" * 34)
print(f"TOTAL OVER LIMIT: {over_limit_count}")
print("=" * 34)
