#!/usr/bin/python3
"""01. Script that start a flask web application"""

from flask import Flask

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


@app.route("/number/<n>")
def hello_05(n):
    """Returns other text."""
    if n is type(int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
