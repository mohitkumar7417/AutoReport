import typer
import os

app = typer.Typer()


@app.command()
def generate():
    """Generate report"""
    print("Generating report...")
    os.system("py run_final_report.py")


@app.command()
def validate():
    """Validate project files"""

    required_files = [
        "data/sales.csv",
        "templates/report_template.html",
        "templates/report_template.yaml"
    ]

    missing = []

    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)

    if missing:
        print("Missing files:")
        for file in missing:
            print(f" - {file}")
    else:
        print("All required files exist.")


@app.command()
def list_templates():
    """List available templates"""

    template_folder = "templates"

    if os.path.exists(template_folder):
        for file in os.listdir(template_folder):
            print(file)
    else:
        print("Templates folder not found.")


if __name__ == "__main__":
    app()