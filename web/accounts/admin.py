#!/usr/bin/python3
""" Admin routes """
from flask import Blueprint, render_template, redirect, url_for, flash, request
from web.forms import LoginForm, PostBlog, StudentRegistrationForm, StaffRegistrationForm
import uuid
import bcrypt
from models import storage
from flask_login import login_user, current_user, logout_user
from models.student import Student
from models.staff import Staff
from models.post import Post
import secrets
import os
from web import app
from PIL import Image
from functools import wraps

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin') 


def adminProtected(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        if not current_user.is_authenticated or hasattr(current_user, "school_id"):
            flash('Please login as admin to access this page')
            return redirect(url_for('admin_bp.adminLogin'))
        return func(*args, **kwargs)
    return decorator


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
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('admin_bp.adminBlog'))
        else:
            flash('Unsuccessful Login. Please check email or password')
    return render_template('login.html', admin=True,
                        form=form, cached_id=cached_id)
                    
@admin_bp.route('/account', methods=['GET', 'POST'], strict_slashes=False)
@adminProtected
def adminAccount():
    """Admin Account"""
    return render_template('users/account_admin.html', admin=True,
                           cached_id=str(uuid.uuid4()))



@admin_bp.route('/blog', methods=['GET'], strict_slashes=False)
@adminProtected
def adminBlog():
    """Admin blog"""
    return render_template('users/blog.html', admin=True, 
                           cached_id=str(uuid.uuid4()))


@admin_bp.route('/blog/create-post', methods=['GET', 'POST'], strict_slashes=False)
@adminProtected
def adminPost():
    """Admin create blog post"""
    form = PostBlog()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, school_id=current_user.id)
        post.save()
        return redirect(url_for('admin_bp.adminBlog'))
    return render_template('users/postblog.html', form=form, admin=True,
                           cached_id=str(uuid.uuid4()))


def save_picture(picture):
    _, f_ex = os.path.splitext(picture.filename)
    picture_fn = secrets.token_hex(8) + f_ex 
    picture_path = os.path.join(app.root_path, 'static/assests/user_imgs', picture_fn)

    user_pic = Image.open(picture)
    user_pic.thumbnail((120, 120))
    user_pic.save(picture_path)

    return picture_fn

@admin_bp.route('/register/student', methods=['GET', 'POST'], strict_slashes=False)
@adminProtected
def studentSignUp():
    """Student Signup"""
    form = StudentRegistrationForm()
    if form.validate_on_submit():
        hash_pwd = bcrypt.hashpw(form.last_name.data.lower().encode('utf-8'), bcrypt.gensalt())
        st = Student(first_name=form.first_name.data, last_name=form.last_name.data, password=hash_pwd,
                     school_id=current_user.id, dob= form.dob.data,
                     address=form.address.data, guardian_phone_no=form.guardian_phone_no.data)
        if form.picture.data:
            pic_fn = save_picture(form.picture.data)
            st.picture = pic_fn
        st.save()
        flash('Account created succesfully for {} {} with id {}'.format(
            form.first_name.data, form.last_name.data, st.id), 'success')
        return(redirect(url_for('admin_bp.studentSignUp')))
    return render_template('users/register_user.html', form=form, staff=False, admin=True)


@admin_bp.route('/register/staff', methods=['GET', 'POST'], strict_slashes=False)
@adminProtected
def staffSignUp():
    """Student Signup"""
    form = StaffRegistrationForm()
    if form.validate_on_submit():
        hash_pwd = bcrypt.hashpw(form.last_name.data.lower().encode('utf-8'), bcrypt.gensalt())
        stf = Staff(first_name=form.first_name.data, last_name=form.last_name.data, password=hash_pwd,
                     school_id=current_user.id, dob=form.dob.data, email=form.email.data,
                     address=form.address.data, phone_number=form.phone_no.data)
        if form.picture.data:
            pic_fn = save_picture(form.picture.data)
            stf.picture = pic_fn
        stf.save()
        flash('Account created succesfully for {} {} with id {}.'.format(
            form.first_name.data, form.last_name.data, stf.id), 'success')
        return(redirect(url_for('admin_bp.staffSignUp')))
    return render_template('users/register_user.html', form=form, staff=True, admin=True)


@admin_bp.route('/view/students', methods=['GET'], strict_slashes=False)
@adminProtected
def viewStudent():
    """Student Signup"""
    students = current_user.students
    print(students)
    return render_template('users/view.html', users=students, admin=True)

@admin_bp.route('/view/staff', methods=['GET'], strict_slashes=False)
@adminProtected
def viewStaff():
    """Student Signup"""
    staff = current_user.staffs
    return render_template('users/view.html', users=staff, admin=True)

@admin_bp.route('/logout', methods=['GET'], strict_slashes=False)
@adminProtected
def adminLogout():
    """Logout User"""
    logout_user()
    return redirect(url_for('admin_bp.adminLogin'))
