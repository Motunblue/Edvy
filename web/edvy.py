#!/usr/bin/python3
"""Route for Web"""
from flask import Flask, render_template
from flask_cors import CORS
import uuid


app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "http://localhost:5000"}})

@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Retrieve home """
    return render_template('index.html', cache_id=str(uuid.uuid4()))

@app.route('/signup/', methods=['GET'], strict_slashes=False)
def signUp():
    return render_template('signup.html')

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug="True")
