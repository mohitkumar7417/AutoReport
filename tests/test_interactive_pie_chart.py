from autoreport.ingestion import read_csv
from autoreport.interactive_charts import create_interactive_pie_chart

df = read_csv("data/sales.csv")

create_interactive_pie_chart(
    df,
    "Product",
    "Sales",
    "reports/interactive_pie_chart.html"
)

print("Interactive pie chart generated successfully!")