from flask import Flask, render_template, request, redirect
import pandas as pd
from functions.pdf_generator import pdf_generator
app = Flask(__name__)


@app.route("/")
def dashboard():

    clients_df = pd.read_csv("data/client_data.csv")

    client_list = []

    for client in clients_df.iterrows():
        client_nr = client[1]["client_nr"]
        first_name = client[1]["Fname"]
        last_name = client[1]["Lname"]
        address = client[1]["address"]
        email = client[1]["email"]
        phone = client[1]["phone"]

        client_data_to_append_client_list = [client_nr, f"{first_name} {last_name}", address, email, phone]

        client_list.append(client_data_to_append_client_list)

    return render_template("dashboard.html", client_list=client_list)


@app.route("/create_new_invoice", methods=["POST"])
def create_new_invoice():
    # Check how many services are given
    data = request.form
    row_counter = 0
    client_nr = request.form["select-client-input"]

    for key in data:
        if "name" in key:
            row_counter = row_counter + 1

    type_counter = 1
    form_data = [client_nr, []]

    while type_counter <= row_counter:
        service_name = request.form[f"service-name-{type_counter}"]
        service_hours = request.form[f"hours-{type_counter}"]
        service_wage = request.form[f"wage-{type_counter}"]

        form_data_set = [service_name, service_hours, service_wage]

        form_data[1].append(form_data_set)

        type_counter = type_counter + 1

    pdf_generator(client_nr, form_data[1])

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
