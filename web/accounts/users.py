#!/usr/bin/python3
""" Users routes """
from flask import Blueprint, render_template, redirect, url_for, flash, request
from web.forms import LoginForm
from models import storage
from flask_login import login_user, current_user, logout_user
import uuid
import bcrypt
from functools import wraps
from web.forms import PostBlog
from models.post import Post

users_bp = Blueprint('users_bp', __name__, url_prefix='/')

def userProtected(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        if not current_user.is_authenticated or not hasattr(current_user, "school_id"):
            flash('Please login to access this page')
            return redirect(url_for('user_bp.userLogin'))
        return func(*args, **kwargs)
    return decorator


@users_bp.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def userLogin():
    """Login for users"""
    form = LoginForm()
    form.email.validators = []
    if form.validate_on_submit():
        if form.user_id.data[:3] == "STD":
            user = storage.all(cls='Student', id=form.user_id.data)
        else:
            user = storage.all(cls='Staff', id=form.user_id.data)
        if user and bcrypt.checkpw(form.password.data.encode('utf-8'), user.password.encode('utf-8')):
            login_user(user, form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('user_bp.userBlog'))
        else:
            flash('Unsuccessful Login. Please check email or password')
    return render_template('login.html', admin=False,
                        form=form, cache_id=str(uuid.uuid4())
                        )


@users_bp.route('/account', methods=['GET', 'POST'], strict_slashes=False)
@userProtected
def adminAccount():
    """Admin Account"""
    return render_template('users/blog.html', cached_id=str(uuid.uuid4()))

@users_bp.route('/blog', methods=['GET'], strict_slashes=False)
@userProtected
def userBlog():
    """User blog"""
    return render_template('users/blog.html', admin=False)


@users_bp.route('/blog/create-post', methods=['GET', 'POST'], strict_slashes=False)
@userProtected
def userPost():
    """Admin create blog post"""
    form = PostBlog()
    if form.validate_on_submit():
        if current_user.id[:3] == "STD":
            post = Post(title=form.title.data, content=form.content.data,
                     school_id=current_user.school_id, student_id=current_user.id)
        else:
            post = Post(title=form.title.data, content=form.content.data,
                     school_id=current_user.school_id, staff_id=current_user.id)
        post.save()
        return redirect(url_for('users_bp.userBlog'))
    return render_template('users/postblog.html', form=form, admin=False,
                           cached_id=str(uuid.uuid4()))


@users_bp.route('/logout', methods=['GET'], strict_slashes=False)
@userProtected
def userLogout():
    """Logout User"""
    logout_user()
    return redirect(url_for('users_bp.userLogin'))
