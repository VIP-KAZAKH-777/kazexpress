from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=128)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=128)])
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=128)])
    password = PasswordField('New Password', validators=[DataRequired(), Length(min=8, max=128)])
    confirm  = PasswordField('Repeat Password', validators=[DataRequired(), Length(min=8, max=128), EqualTo('password', message="passwords do not match")])
    submit = SubmitField('Sign Up')