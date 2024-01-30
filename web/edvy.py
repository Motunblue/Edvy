#!/usr/bin/python3
"""Route for Web"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Retrieve home """
    return render_template('index.html')

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug="True")
