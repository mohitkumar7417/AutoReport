import pandas as pd
from autoreport.report_generator import generate_html_report
from pdf_generator import generate_pdf_report

# Load data
df = pd.read_csv("data/sales.csv")

# Charts (use file paths from your previous steps)
charts = {
    "bar": "reports/interactive_bar_chart.html",
    "line": "reports/interactive_line_chart.html",
    "pie": "reports/interactive_pie_chart.html"
}

# Generate final report
generate_html_report(df, charts, "reports/final_report.html")

summary = {
    "generated_at": "Generated from AutoReport",
    "total_records": len(df),
    "total_sales": df["Sales"].sum(),
    "average_sales": round(df["Sales"].mean(), 2),
    "min_sales": df["Sales"].min(),
    "max_sales": df["Sales"].max()
}

generate_pdf_report(summary)

print("FINAL REPORT GENERATED SUCCESSFULLY")