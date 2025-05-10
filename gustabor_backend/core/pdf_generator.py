from fpdf import FPDF
from typing import List

def generate_pdf(patient_name: str, recommendations: List[str], file_path: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=f"Personalized Recipe Report for {patient_name}", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=11)
    for i, rec in enumerate(recommendations, 1):
        pdf.multi_cell(0, 10, f"{i}. {rec}", border=0)
        pdf.ln(2)

    pdf.output(file_path)
