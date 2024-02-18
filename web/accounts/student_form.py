from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import storage


class StudentRegistrationForm(FlaskForm):
        """student signup Form"""
        first_name = StringField('first name',
                validators=[DataRequired(), Length(min=3, max=45)],
                render_kw={'placeholder': 'first name'}
                )

        last_name = StringField('last name',
                validators=[DataRequired(), Length(min=3, max=45)],
                render_kw={'placeholder': 'last name'}
                )

        password = PasswordField('password', validators=[DataRequired()],
                render_kw={'placeholder': 'password'}
                )

        confirm_password = PasswordField('confirm Password',
                validators=[DataRequired(), EqualTo('password')],
                render_kw={'placeholder': 'confirm password'}
                )

        submit = SubmitField('Register')
