from autoreport.ingestion import read_csv
from autoreport import analysis
from autoreport.report_generator import generate_summary

# Load data
df = read_csv("data/sales.csv")

# Map analysis functions
analysis_functions = {
    "count": analysis.count_records,
    "sum": analysis.total_sum,
    "average": analysis.average,
    "min": analysis.minimum,
    "max": analysis.maximum,
}

# Generate report
report = generate_summary(df, analysis_functions)

# Print report
print("\n===== AUTO REPORT =====")
for key, value in report.items():
    print(f"{key}: {value}")