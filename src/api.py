from flask import Flask, jsonify # type: ignore
from inventory import Inventory
from loan import Loan

app = Flask(__name__)
inventory = Inventory()
loan_system = Loan()

@app.route("/available_items", methods=["GET"])
def get_available_items():
    return jsonify(inventory.get_available_items())

@app.route("/loan_status", methods=["GET"])
def get_loan_status():
    return jsonify(loan_system.loans)

if __name__ == "__main__":
    app.run(debug=True)