#!/usr/bin/python3
"""01. Script that start a flask web application"""

from flask import Flask

app = Flask(__name__)

@app.route("/hbnb", strict_slashes=False)
def hello():
    """Returns some text."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
