"""
RECORD CHECK  -  my version
===========================

Name  :arame beni winner 
Lane  :  AI 
Date  :05-11-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
df = pd.read_csv("datasets.csv")

# ================================================================= PROCESS

df["percent"] = (
    df["rows_loaded"] / df["rows_expected"]
) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100
    else "WARNING" if p >= 90
    else "OK"
)

# ================================================================== OUTPUT
print("DATASET RECORD CHECK")
print("=" * 45)

print(df)

print()
print("COUNT PER STATUS")
print("=" * 45)

status_counts = df.groupby("status").size()

print(status_counts)

df.to_csv("datasets_report.csv", index=False)


#bar chartt

status_counts.plot(kind="bar")

plt.title("Dataset Status Counts")
plt.xlabel("Status")
plt.ylabel("Number of Datasets")
plt.tight_layout()

plt.savefig("dataset_status_chart.png")

plt.show()
