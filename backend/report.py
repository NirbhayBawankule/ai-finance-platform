from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(predictions, file_path="report.pdf"):
    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    content = [Paragraph("Monthly Expense Forecast Report", styles["Title"])]

    for category, value in predictions.items():
        content.append(
            Paragraph(f"{category.capitalize()}: ₹{round(value, 2)}", styles["Normal"])
        )

    doc.build(content)
    return file_path
