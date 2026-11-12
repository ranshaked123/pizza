#https://github.com/ranshaked123/pizza

from flask import Flask, request, jsonify
import time
import random

app = Flask(__name__)

@app.route('/approve', methods=['POST'])
def approve():
    data = request.get_json()

    print("Name:", data.get('name'))
    print("Phone:", data.get('phone'))
    print("Order:", data.get('invite'))
    print("Price:", data.get('price'))

    wait = random.randint(1, 10)
    time.sleep(wait)

    return "1"


app.run(host='0.0.0.0', port=8090)