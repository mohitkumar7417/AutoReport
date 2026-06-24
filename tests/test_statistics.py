from autoreport.ingestion import read_csv
from autoreport.analysis import (
    median,
    standard_deviation,
    percentile,
    group_by_sum
)

df = read_csv("data/sales.csv")

print("Median:", median(df, "Sales"))
print("Standard Deviation:", standard_deviation(df, "Sales"))
print("25th Percentile:", percentile(df, "Sales", 0.25))
print("75th Percentile:", percentile(df, "Sales", 0.75))

print("\nGroup By:")
print(group_by_sum(df, "Product", "Sales"))