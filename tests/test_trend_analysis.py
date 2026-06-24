from autoreport.ingestion import read_csv
from autoreport.trend_analysis import (
    moving_average,
    growth_rate,
    cumulative_growth
)

df = read_csv("data/sales.csv")

print("Moving Average:")
print(moving_average(df, "Sales"))

print("\nGrowth Rate (50 -> 80):")
print(growth_rate(50, 80))

print("\nCumulative Growth:")
print(cumulative_growth(df["Sales"]))