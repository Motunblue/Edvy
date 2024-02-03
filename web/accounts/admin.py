#!/usr/bin/python3
""" Admin routes """
from flask import Blueprint, render_template
from web.forms import LoginForm
import uuid

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin') 

@admin_bp.route('/login', methods=['GET'], strict_slashes=False)
def adminLogin():
    """Login for admin"""
    form = LoginForm()
    return render_template('login_admin.html', form=form, cache_id=str(uuid.uuid4()))
