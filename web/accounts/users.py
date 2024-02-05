#!/usr/bin/python3
""" Users routes """
from flask import Blueprint, render_template
from web.forms import LoginForm
import uuid

users_bp = Blueprint('user_bp', __name__, url_prefix='/') 

@users_bp.route('/login', methods=['GET'], strict_slashes=False)
def userLogin():
    """Login for users"""
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('login.html', admin=False,
                        form=form, cache_id=str(uuid.uuid4())
                        )
