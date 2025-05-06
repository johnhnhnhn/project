# app/report.py

import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(articles):
    # Generate CSV
    df = pd.DataFrame(articles)
    df.to_csv('report.csv', index=False)

    # Generate PDF
    c = canvas.Canvas("report.pdf", pagesize=letter)
    c.drawString(100, 750, "News Report")
    c.save()
