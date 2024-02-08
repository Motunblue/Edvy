#!/usr/bin/python3
""" Admin routes """
from flask import Blueprint, render_template, redirect, url_for
from web.forms import LoginForm
import uuid

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin') 

@admin_bp.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def adminLogin():
    """Login for admin"""
    cached_id = str(uuid.uuid4())
    form = LoginForm()
    form.user_id.validators = []
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'pass':
            return redirect(url_for('admin_bp.adminBlog'))
        else:
            pass #return a block incorrect user name or password
    return render_template('login.html', admin=True,
                        form=form, cached_id=cached_id)
                    

@admin_bp.route('/blog', methods=['GET'], strict_slashes=False)
def adminBlog():
    """Admin blog"""
    return render_template('users/blog.html', cached_id=str(uuid.uuid4()))
