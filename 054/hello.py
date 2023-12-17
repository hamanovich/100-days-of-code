from flask import Flask
from markupsafe import escape
import random

random_number = random.randint(0, 9)
print(random_number)


def make_bold(function):
    def wrapper_func():
        return f'<b>{function()}</b>'
    return wrapper_func


def make_emphasis(function):
    def wrapper_func():
        return f'<em>{function()}</em>'
    return wrapper_func


app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Hello world</h1>"



@app.route("/bye")
@make_bold
@make_emphasis
def bye():
    return "Bye!"


@app.route("/username/<name>")
def greet(name, number):
    return f"Hello there {escape(name)}!"
