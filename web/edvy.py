#!/usr/bin/python3
"""Route for Web"""
from flask import Flask, render_template, url_for, flash, redirect
from flask_cors import CORS
import uuid
from web.accounts.users import users_bp
from web.accounts.admin import admin_bp
from web.forms import RegistrationForm
import bcrypt
from models.school import School
from web import app

#Register blueprint for users and admin
app.register_blueprint(users_bp)
app.register_blueprint(admin_bp)
app.config['SECRET_KEY'] = '&dont[you]just*love^edvy$'

cors = CORS(app, resources={r"/*": {"origins": "http://localhost:5000"}})

@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Retrieve home """
    return render_template('index.html', cache_id=str(uuid.uuid4()))

@app.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    """School signup"""
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pwd = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
        sc = School(name=form.school_name.data, email=form.email.data, password=hash_pwd)
        sc.save()
        flash('Account created succesfully for {}. Please login!'.format(form.school_name.data), 'success')
        return(redirect(url_for('admin_bp.adminLogin')))
    return render_template('signup.html', form=form, cache_id=str(uuid.uuid4()))


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug="True")
