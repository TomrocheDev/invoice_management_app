from datetime import date
from fpdf import FPDF
import pandas as pd

def pdf_generator(client_nr, list):
    this_date = date.today().strftime("%d-%m-%y")

    # Get client info
    client_df = pd.read_csv("data/client_data.csv")

    client_info = {}

    for client in client_df.iterrows():
        if client[1]["client_nr"] == client_nr:
            client_info["name"] = f"{client[1]['Fname']} {client[1]['Lname']}"
            client_info["address"] = client[1]["address"]
            client_info["email"] = client[1]["email"]
            client_info["phone"] = client[1]["phone"]

    pdf = FPDF("P", "mm", "A4")
    pdf.add_page()

    pdf.image("static/images/brand-logo.PNG", 8, 5, 50)

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
    pdf.cell(30, 5, client_info["name"], ln=1)

    pdf.cell(25, 5, "Address: ", ln=0)
    pdf.cell(95, 5, "Example Road 2", ln=0)
    pdf.cell(25, 5, "Client number: ", ln=0)
    pdf.cell(30, 5, str(client_nr), ln=1)

    pdf.cell(25, 5, "Postal code: ", ln=0)
    pdf.cell(95, 5, "1234 AB, Example City, The Netherlands", ln=0)
    pdf.cell(25, 5, "Address: ", ln=0)
    pdf.cell(30, 5, client_info["address"], ln=1)

    pdf.cell(25, 5, "Email: ", ln=0)
    pdf.cell(95, 5, "info@tomrochedevelopment.com", ln=0)
    pdf.cell(25, 5, "Email: ", ln=0)
    pdf.cell(30, 5, client_info["email"], ln=1)

    pdf.cell(25, 5, "Phone: ", ln=0)
    pdf.cell(95, 5, "+31 612345678", ln=0)
    pdf.cell(25, 5, "Phone: ", ln=0)
    pdf.cell(30, 5, str(client_info["phone"]), ln=1)

    pdf.ln(10)

    # OPTIONAL!
    # Create  box around invoice details
    # pdf.line(10, 98, 75, 98)
    # pdf.line(10, 115, 75, 115)
    # pdf.line(10, 98, 10, 115)
    # pdf.line(75, 115, 75, 98)

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

    pdf.ln(2)

    # Generate given data from the app onto the invoice
    amounts_list = []

    pdf.set_font("Helvetica", "", 9)
    for service in list:
        service_name = service[0]
        cost = service[2] * service[1]
        rounded_cost = round(cost, 2)
        total_cost = cost * 1.21
        rounded_total_cost = round(total_cost, 2)
        amounts_list.append(total_cost)

        pdf.cell(85, 7, service_name.capitalize(), ln=0)
        pdf.cell(35, 7, chr(128) + str(rounded_cost), ln=0)
        pdf.cell(35, 7, "21%", ln=0)
        pdf.cell(35, 7, chr(128) + str(rounded_total_cost), ln=1)

    pdf.ln(10)

    # Create total invoice worth section
    pdf.cell(120, 7, "", ln=0)

    pdf.set_font("Helvetica", "B", 9)
    pdf.cell(35, 7, "Total amount to pay:")

    pdf.set_font("Helvetica", "", 9)
    pdf.cell(35, 7, chr(128) + str(round((float(sum(amounts_list))), 2))) # This rounds, floats and sums the list

    pdf.ln(20)

    # Create section for payment details
    pdf.cell(50, 7, "Please make sure to pay this invoice before {EXPIRATION DATE}.", ln=1) # Generated dynamically
    pdf.cell(50, 7, "Bankaccount number: NL01 JAEF 1234 5678 90") # Generated dynamically

    pdf.ln(81)

    # Create footer
    pdf.set_font("", "", 7)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(10, 8, "", ln=0)
    pdf.cell(200, 8, "Tom Roche Software Development  -  NL01 JAEF 1234 5678 90  -  Example Road 2, Example City  -  "
                     "info@tomrochedevelopment.com  -  +31 612345678")

    pdf.output("my_invoices/example.pdf")


# pdf_generator(123, [
#     ["EEN", 1, 1],
#     ["TWEE", 2 ,2],
#     ["DRIE", 3, 3]
# ])