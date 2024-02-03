#!/usr/bin/python3
""" Users routes """
from flask import Blueprint, render_template

users_bp = Blueprint('user_bp', __name__, url_prefix='/') 

@users_bp.route('/login', methods=['GET'], strict_slashes=False)
def userLogin():
    """Login for users"""
    return ("User login")
