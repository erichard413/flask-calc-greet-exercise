# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_ints():
    #add integers from query string
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{add(a, b)}"
@app.route('/sub')
def subtract_ints():
    #subtract integers from query string
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{sub(a, b)}"
@app.route('/mult')
def mult_ints():
    #multiply integers from query string
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{mult(a, b)}"
@app.route('/div')
def divide_ints():
    #divide integers from query string
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{div(a, b)}"

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.route("/math/<oper>")
def maths(oper):
    #Do math on integers from query string
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{operators[oper](a,b)}"