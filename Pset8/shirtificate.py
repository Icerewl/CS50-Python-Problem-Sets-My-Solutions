
from fpdf import FPDF

name = input("Name: ")
name = name + " took CS50"
pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.set_font('helvetica', size=60)
pdf.image("shirtificate.png", x=3, y=70)
pdf.cell(w=0,h=60,txt="CS50 Shirtificate",align="C",)
#pdf.text(x=30,y=40,txt="CS50 Shirtificate")
pdf.set_font('helvetica', size=25)
pdf.set_text_color(255, 255, 255)
pdf.cell(w=-185,h=260,txt=name,align="C",)

pdf.output("shirtificate.pdf")