#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_text(parameter):
    print(parameter)
    return parameter 

@app.route('/count/<parameter>')
def count(parameter):
    count_str = ''
    count = 0
    while count < int(parameter):
        count_str += str(count) + '\n'
        count += 1
    return count_str

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(int(num1) + int(num2))
    elif operation == '-':
        return str(int(num1) - int(num2))
    elif operation == '*':
        return str(int(num1) * int(num2))
    elif operation == 'div':
        return str(int(num1) / int(num2))
    elif operation == '%':
        return str(int(num1) % int(num2))

if __name__ == '__main__':
    app.run(port=5555, debug=True)