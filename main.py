from fpdf import FPDF
import pandas as pd


df = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()
    
    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)
    
    # Set the footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
    
    # lines
    x1 = 10
    y1 = 21
    x2 = 200
    y2 = 21
    for l in range(25):
        y1 += 10
        y2 += 10
        pdf.line(x1, y1, x2, y2)
    
    if int(row["Pages"]) > 1:
        for i in range(int(row["Pages"])-1):
            pdf.add_page()
            
            # Set the footer
            pdf.ln(273)
            pdf.set_font(family="Times", style="I", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
            
            # lines
            x1 = 10
            y1 = 11
            x2 = 200
            y2 = 11
            for l in range(26):
                y1 += 10
                y2 += 10
                pdf.line(x1, y1, x2, y2)

pdf.output("output.pdf")