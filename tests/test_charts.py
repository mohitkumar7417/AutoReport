import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from autoreport.ingestion import read_csv
from autoreport.visualization import (
    create_line_chart,
    create_pie_chart,
    create_scatter_plot
)

df = read_csv("data/sales.csv")

create_line_chart(
    df,
    "Product",
    "Sales",
    "reports/line_chart.png"
)

create_pie_chart(
    df,
    "Product",
    "Sales",
    "reports/pie_chart.png"
)

create_scatter_plot(
    df,
    "Product",
    "Sales",
    "reports/scatter_plot.png"
)

print("Charts generated successfully!")