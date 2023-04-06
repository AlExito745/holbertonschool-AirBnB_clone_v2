#!/usr/bin/python3
"""01. Script that start a flask web application"""

from flask import Flask
from flask import render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_01():
    """Returns some text."""
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_02():
    """Returns other text."""
    return "HBNB"


@app.route("/c/<text>")
def hello_03(text):
    """Replace text with variable."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/")
@app.route("/python/<text>")
def hello_04(text="is cool"):
    """Replace more text with another variable."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>")
def hello_05(n):
    """Replace with "int" if only given "int"."""
    n = str(n)
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def hello_06(n):
    """Display a HTML page if only given "int"."""
    n = str(n)
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def hello_07(n):
    """Display a different HTML page if only given "int" even or odd."""
    return render_template("6-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
