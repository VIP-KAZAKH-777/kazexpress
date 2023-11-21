from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TelField, FileField, SearchField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Length

class SearchForm(FlaskForm):
    searched = SearchField("Search", [DataRequired()])
    submit = SubmitField("Find")

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=128)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=128)])
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=128)])
    password = PasswordField('New Password', validators=[DataRequired(), Length(min=8, max=128)])
    confirm  = PasswordField('Repeat Password', validators=[DataRequired(), Length(min=8, max=128), EqualTo('password', message="passwords do not match")])
    submit = SubmitField('Sign Up')

class ProfileForm(FlaskForm):
    pic = FileField('Profile picture')
    fullname = StringField('Full name')
    email = EmailField('Email')
    phone = TelField('Phone')
    address = StringField('Address')
    submit = SubmitField('Save')

class DeliveryForm(FlaskForm):
    address = StringField('Address')
    pcode = StringField('Postal code', validators=[Length(min = 6, max=6)])
    submit = SubmitField('Save')
