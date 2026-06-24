from autoreport.ingestion import read_csv
from autoreport.visualization import create_bar_chart

df = read_csv("data/sales.csv")

create_bar_chart(df, "Product", "Sales")

print("Chart created successfully!")