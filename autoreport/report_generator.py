from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import yaml


def generate_summary(df, analysis_function=None):

    if isinstance(df, dict):
        return df

    summary = {
        "rows": len(df),
        "columns": list(df.columns),
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return summary


def generate_html_report(df, charts=None, output_file="reports/final_report.html"):
    if charts is None:
        charts = {}

    """
    Generates a full HTML report using Jinja2
    Includes:
    - Data summary
    - Charts (HTML files from Plotly)
    """

    with open("templates/report_template.yaml", "r") as f:
        config = yaml.safe_load(f)

    # Create summary
    summary = generate_summary(df)


    # Combine report data
    report_data = {
    "title": config.get("title", "Automated Report"),

    "generated_at": summary["generated_at"],

    "total_records": len(df),

    "total_sales": df["Sales"].sum(),

    "average_sales": round(df["Sales"].mean(), 2),

    "min_sales": df["Sales"].min(),

    "max_sales": df["Sales"].max(),

    "charts": charts
}

    # Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader("templates"))

    template = env.get_template("report_template.html")

    # Render HTML
    html_content = template.render(report_data)

    # Save HTML file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Report generated successfully at {output_file}")
    return output_file