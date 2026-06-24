from autoreport.ingestion import read_csv
from autoreport.interactive_charts import create_interactive_bar_chart

df = read_csv("data/sales.csv")

create_interactive_bar_chart(
    df,
    "Product",
    "Sales",
    "reports/interactive_bar_chart.html"
)

print("Interactive chart generated successfully!")

