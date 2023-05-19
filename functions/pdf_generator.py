from datetime import date

from fpdf import FPDF

def pdf_generator(client_nr, array):
    this_date = date.today().strftime("%d-%m-%y")


    pdf = FPDF("P", "mm", "A4")
    pdf.add_page()

    pdf.image("../static/images/brand-logo.PNG", 8, 5, 50)

    pdf.ln(32)

    # Create header section
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(40, 20, "Invoice", ln=1)

    pdf.set_font("Helvetica", "B", 8)
    pdf.cell(120, 5, "Billing address:", ln=0)
    pdf.cell(30, 5, "Client info: ", ln=1)

    pdf.set_font("Helvetica", "", 8)
    pdf.cell(25, 5, "Company name: ", ln=0)
    pdf.cell(95, 5, "Tom Roche Software Development", ln=0)
    pdf.cell(25, 5, "Name: ", ln=0)
    pdf.cell(30, 5, "{CLIENT NAME}", ln=1)

    pdf.cell(25, 5, "Address: ", ln=0)
    pdf.cell(95, 5, "Example Road 2", ln=0)
    pdf.cell(25, 5, "Client number: ", ln=0)
    pdf.cell(30, 5, str(client_nr), ln=1)

    pdf.cell(25, 5, "Postal code: ", ln=0)
    pdf.cell(95, 5, "1234 AB, Example City, The Netherlands", ln=0)
    pdf.cell(25, 5, "Address: ", ln=0)
    pdf.cell(30, 5, "{CLIENT ADDRESS}", ln=1)

    pdf.cell(25, 5, "Email: ", ln=0)
    pdf.cell(95, 5, "info@tomrochedevelopment.com", ln=0)
    pdf.cell(25, 5, "Email: ", ln=0)
    pdf.cell(30, 5, "{CLIENT EMAIL}", ln=1)

    pdf.cell(25, 5, "Phone: ", ln=0)
    pdf.cell(95, 5, "+31 612345678", ln=0)
    pdf.cell(25, 5, "Phone: ", ln=0)
    pdf.cell(30, 5, "{CLIENT PHONE}", ln=1)

    pdf.ln(10)

    # Create subheader section
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(30, 5, "Invoice date: ", ln=0)
    pdf.cell(25, 5, f"{this_date}", ln=1)

    pdf.set_font("Helvetica", "", 10)
    pdf.cell(30, 5, "Invoice number: ", ln=0)
    pdf.cell(25, 5, "{INVOICE NUMBER}")

    pdf.ln(12)

    pdf.line(10, 126, 200, 126)

    # Create table header
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(85, 8, "Service", ln=0)
    pdf.cell(35, 8, "Cost", ln=0)
    pdf.cell(35, 8, "Tax", ln=0)
    pdf.cell(35, 8, "Total", ln=1)


    # for service in array:
    #     pdf.cell(40, 10, txt=service[0])

    pdf.output("../my_invoices/example.pdf")

pdf_generator(123,[])