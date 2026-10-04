#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)


# Look up a contract by its numeric id.
# 200 + contract info if found, 404 if not.
@app.route('/contract/<int:id>')
def contract(id):
    for c in contracts:
        if c["id"] == id:
            return make_response(c["contract_information"], 200)
    return make_response("", 404)


# Check whether a customer exists by name.
# 204 with an empty body if found (data is sensitive), 404 if not.
@app.route('/customer/<customer_name>')
def customer(customer_name):
    if customer_name in customers:
        return make_response("", 204)
    return make_response("", 404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)