from flask import Flask, render_template, redirect, request
import pandas as pd

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


if __name__ == "__main__":
    app.run(debug=True, port=5003)