import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from autoreport.ingestion import read_csv
from autoreport import analysis
from autoreport.report_generator import generate_summary, generate_html_report

# Load data
df = read_csv("data/sales.csv")

# Analysis functions mapping
analysis_functions = {
    "count": analysis.count_records,
    "sum": analysis.total_sum,
    "average": analysis.average,
    "min": analysis.minimum,
    "max": analysis.maximum,
}

# Generate report dictionary
report = generate_summary(df, analysis_functions)

# Generate HTML report
file_path = generate_html_report(df)

print("HTML Report generated at:", file_path)