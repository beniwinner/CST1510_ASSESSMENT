
"""
RECORD CHECK - AI / DATA SCIENCE
================================

Name  :arame beni winner
Lane  : AI
Date  : 08-11-2026
"""

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Clean and parse one survey record into a dictionary."""

    clean_line = raw_line.strip().lower()
    parts = clean_line.split(",")

    record = {"dataset": parts[0].strip()}

    for piece in parts[1:]:
        key, value = piece.split("=")
        record[key.strip()] = float(value.strip())

    return record


# ====================================================================== INPUT

raw_records = [
    "  Survey_2026 , RATING=4 , AGE=23  ",
    "survey_2026,rating=2,age=19",
    "  CUSTOMER_SURVEY , rating = 5 , Age = 34",
    "Product_Feedback , RATING= 1 , age= 27",
    "  Market_Research , rating=3 , AGE=41"
]


# =============================================================== PROCESS + OUTPUT

for raw_record in raw_records:
    record = parse_line(raw_record)
    print(record)
