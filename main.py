from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():

    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, text=row["Topic"], align="L", ln=1)
    
    # Set the body 
    # pdf.line(start_x, start_y, end_x, end_y)
    start_y = 20
    end_y = 298
    space_betweem_lines = 10
    # for each line position from current place to bottom:
    #      draw a horizontal line
    for line_y in range(start_y, end_y, space_betweem_lines):
        pdf.line(10, line_y, 200, line_y)

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, text=row["Topic"], align="R")

    for i in range(row["Pages"] -1):
        pdf.add_page()

        for line_y in range(start_y, end_y, space_betweem_lines):
            pdf.line(10, line_y, 200, line_y)

        # Set the footer
        pdf.ln(265)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, text=row["Topic"], align="R")

pdf.output("output.pdf") 
