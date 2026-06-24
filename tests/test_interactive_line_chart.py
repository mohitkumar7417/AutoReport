from autoreport.ingestion import read_csv
from autoreport.interactive_charts import create_interactive_line_chart

df = read_csv("data/sales.csv")

create_interactive_line_chart(
    df,
    "Product",
    "Sales",
    "reports/interactive_line_chart.html"
)

print("Interactive line chart generated successfully!")