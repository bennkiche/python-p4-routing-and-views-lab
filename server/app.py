#!/usr/bin/env python3

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Print the string in the console
    return f"<h1>{param}</h1>"  # Display the string in the browser

@app.route('/count/<int:param>')
def count(param):
    numbers = "\n".join(str(i) for i in range(1, param + 1))
    return f"<pre>{numbers}</pre>"  # Display numbers on separate lines

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Cannot divide by zero", 400
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation", 400
    return f"<h1>{num1} {operation} {num2} = {result}</h1>"

# if __name__ == '__main__':
#     app.run(debug=True)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
