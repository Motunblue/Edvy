#!/usr/bin/python3
""" Users routes """
from flask import Blueprint, render_template, redirect, url_for
from web.forms import LoginForm
from web.accounts.student_form import StudentRegistrationForm
import uuid

users_bp = Blueprint('user_bp', __name__, url_prefix='/') 

@users_bp.route('/student/signup', methods=['GET', 'POST'], strict_slashes=False)
def studentSignUp():
    """Student Signup"""
    form = StudentRegistrationForm()
    if form.validate_on_submit():
        flash('Account created succesfully for {}. Please login!'.format(form.student_name.data), 'success')
        return(redirect(url_for('users_bp.studentSignUp')))
    return render_template('users/student_signup.html', form=form, ccache_id=str(uuid.uuid4()))

@users_bp.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def userLogin():
    """Login for users"""
    form = LoginForm()
    form.email.validators = []
    if form.validate_on_submit():
        return redirect(url_for('user_bp.userBlog'))
    return render_template('login.html', admin=False,
                        form=form, cache_id=str(uuid.uuid4())
                        )


@users_bp.route('/blog', methods=['GET'], strict_slashes=False)
def userBlog():
    """Admin blog"""
    return render_template('users/blog.html')
