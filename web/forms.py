from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import storage

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

    def validate_email(self, email):
        user_email = storage.all(cls='School', email=email.data)
        if user_email:
            raise ValidationError('Email already exits. Please Login')


class LoginForm(FlaskForm):
    """ Admin Login Form"""
    email = StringField('email',
                        validators=[DataRequired(), Email()],
                        render_kw={'placeholder': 'email'}
                    )
    user_id = StringField('id',
                        validators=[DataRequired()],
                        render_kw={'placeholder': 'id'}
                    )
    password = PasswordField('password', validators=[DataRequired()],
                            render_kw={'placeholder': 'password'}
                            )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PostBlog(FlaskForm):
    """Post a blog"""
    title = TextAreaField('Post Title', 
                        validators=[DataRequired(), Length(min=2, max=125)])
    content = TextAreaField('Content', 
                        validators=[DataRequired(), Length(min=2, max=2048)])
    submit = SubmitField('post')
