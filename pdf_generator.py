from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(summary, output_file="reports/final_report.pdf"):
    doc = SimpleDocTemplate(output_file)

    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Automated Sales Report", styles["Title"]))
    content.append(Spacer(1, 12))

    content.append(
        Paragraph(f"Generated At: {summary['generated_at']}", styles["Normal"])
    )
    content.append(Spacer(1, 12))

    content.append(
        Paragraph(f"Total Records: {summary['total_records']}", styles["Normal"])
    )
    content.append(
        Paragraph(f"Total Sales: {summary['total_sales']}", styles["Normal"])
    )
    content.append(
        Paragraph(f"Average Sales: {summary['average_sales']}", styles["Normal"])
    )
    content.append(
        Paragraph(f"Minimum Sales: {summary['min_sales']}", styles["Normal"])
    )
    content.append(
        Paragraph(f"Maximum Sales: {summary['max_sales']}", styles["Normal"])
    )

    doc.build(content)

    print(f"PDF report generated successfully at {output_file}")