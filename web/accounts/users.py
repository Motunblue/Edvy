#!/usr/bin/python3
""" Users routes """
from flask import Blueprint, render_template, redirect, url_for, flash, session
from web.forms import LoginForm
from web.accounts.student_form import StudentRegistrationForm
from models.student import Student
import uuid

users_bp = Blueprint('user_bp', __name__, url_prefix='/') 

@users_bp.route('/student/signup', methods=['GET', 'POST'], strict_slashes=False)
def studentSignUp():
    """Student Signup"""
    admin_id = session.get('admin_id')
    if admin_id:
        form = StudentRegistrationForm()
        if form.validate_on_submit():
            flash('Account created succesfully for {} {}.'.format(form.first_name.data, form.last_name.data), 'success')
            hash_pwd = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
            st = Student(first_name=form.first_name.data, last_name=form.last_name.data, password=hash_pwd, school_id=admin_id)
            st.save()
            return(redirect(url_for('user_bp.studentSignUp')))
        return render_template('users/student_signup.html', form=form)
    else:
        return(redirect(url_for('admin_bp.adminLogin')))

@users_bp.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def userLogin():
    """Login for users"""
    form = LoginForm()
    form.email.validators = []
    if form.validate_on_submit():
        return redirect(url_for('users_bp.userBlog'))
    return render_template('login.html', admin=False,
                        form=form, cache_id=str(uuid.uuid4())
                        )


@users_bp.route('/blog', methods=['GET'], strict_slashes=False)
def userBlog():
    """Admin blog"""
    return render_template('users/blog.html')
