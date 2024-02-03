from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    """signup Form"""
    school_name = StringField('school name',
                            validators=[DataRequired(), Length(min=3, max=50)],
                            render_kw={'placeholder': 'school name'}
                            )
    email = StringField('email',
                        validators=[DataRequired(), Email()],
                        render_kw={'placeholder': 'email'}
                        )
    password = PasswordField('password', validators=[DataRequired()],
                            render_kw={'placeholder': 'password'}
                            )
    confirm_password = PasswordField('confirm Password',
                                    validators=[DataRequired(), EqualTo('password')],
                                    render_kw={'placeholder': 'confirm password'}
                                    )


    submit = SubmitField('Sign-up')


class LoginForm(FlaskForm):
    """Login Form"""
    email = StringField('email',
                        validators=[DataRequired(), Email()],
                        render_kw={'placeholder': 'email'}
                    )
    password = PasswordField('password', validators=[DataRequired()],
                            render_kw={'placeholder': 'password'}
                            )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
