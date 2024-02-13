#!/usr/bin/python3
""" Admin routes """
from flask import Blueprint, render_template, redirect, url_for, flash
from web.forms import LoginForm
import uuid
import bcrypt
from models import storage
from flask_login import login_user, current_user, logout_user

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin') 

@admin_bp.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def adminLogin():
    """Login for admin"""
    cached_id = str(uuid.uuid4())
    form = LoginForm()
    form.user_id.validators = []
    if form.validate_on_submit():
        sc = storage.all(cls='School', email=form.email.data)
        if sc and bcrypt.checkpw(form.password.data.encode('utf-8'), sc.password.encode('utf-8')):
            login_user(sc, form.remember.data)
            return redirect(url_for('admin_bp.adminBlog'))
        else:
            flash('Unsuccessful Login. Please check email or password')
    return render_template('login.html', admin=True,
                        form=form, cached_id=cached_id)
                    

@admin_bp.route('/blog', methods=['GET'], strict_slashes=False)
def adminBlog():
    """Admin blog"""
    return render_template('users/blog.html', cached_id=str(uuid.uuid4()))


@admin_bp.route('/blog/create-post', methods=['GET', 'POST'], strict_slashes=False)
def adminPost():
    """Admin blog"""
    return render_template('users/post.html', cached_id=str(uuid.uuid4()))

@admin_bp.route('/logout', methods=['GET'], strict_slashes=False)
def adminLogout():
    """Admin blog"""
    logout_user()
    return redirect(url_for('admin_bp.adminLogin'))
