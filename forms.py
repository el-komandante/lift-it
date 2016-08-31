from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms import Form, BooleanField, TextField, PasswordField, validators

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=30)])
    email = TextField('Email Address', [validators.Length])
    password = PasswordField('New Password', [validators.Required(), validators.EqualTo('confirm', message='Passwords must match.')])
    confirm = PasswordField('Repeat Password')
