import requests
from flask import Flask, request, Response
from query import  get_company_information
from query_example import get_example
import json
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Yadira!'

@app.route('/api/yahoo')
def get_company():
    symbol = request.args.get('ticker')
    if symbol in None:
        return Response(json.dumps({"error": "missing 'ticker' query-parameter"}), status=400, mimetype='application/json')
    return Response(json.dumps(get_company_information(symbol)), status=200, mimetype='application/json')
@app.route('/api/example')
def get_product_and_price_average():
   query = request.args.get('search_text')
   if query is None:
       return Response(json.dumps({"error": "missing 'search_text' query-parameter"}), status=400, mimetype='application/json')
   return Response(json.dumps(get_example(query)), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()