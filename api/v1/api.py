#!/usr/bin/python3
"""
    Edvy API application
"""
from os import getenv
from models import storage
from api.v1.views import app_views
from flask import Flask

app = Flask(__name__)
app.register_blueprint(app_views, strict_slashes=False)


if __name__ == "__main__":
    host = getenv('Edvy_API_HOST', '0.0.0.0')
    port = getenv('Edvy_API_PORT', '5000')

    app.run(host=host, port=port, threaded=True)
