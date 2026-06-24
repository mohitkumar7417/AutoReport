from autoreport.ingestion import read_csv
from autoreport.analysis import (
    count_records,
    total_sum,
    average,
    minimum,
    maximum,
)

df = read_csv("data/sales.csv")

print("\n===== SALES ANALYSIS REPORT =====")
print("Count:", count_records(df))
print("Total Sales:", total_sum(df, "Sales"))
print("Average Sales:", round(average(df, "Sales"), 2))
print("Minimum Sales:", minimum(df, "Sales"))
print("Maximum Sales:", maximum(df, "Sales"))
print("================================")