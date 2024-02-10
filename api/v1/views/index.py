#!/usr/bin/python3
"""Index routes"""
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', method=['GET'], strict_slashes=False)
def status():
    """Testing API"""
    return jsonify({"status": "OK"})
