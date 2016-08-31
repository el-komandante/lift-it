from flask_wtf import Form
from wtforms.fields import TextField, SubmitField, PasswordField, FloatField, IntegerField, FieldList, FormField
from wtforms import validators, ValidationError
from models import User
from app import db

class SignupForm(Form):
    username = TextField("Username", [validators.Required('Please enter a username.')])
    email = TextField("Email", [validators.Required('Please enter your email address.'), validators.Email('Please enter your email address.')])
    password = PasswordField('Password', [validators.Required('Please enter a password.')])
    submit = SubmitField("Create account")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already in use.")
            return False
        else:
            return True

class SigninForm(Form):
    email = TextField('Email', [validators.Required('Please enter your email address.'), validators.Email('Please enter your email address.')])
    password = PasswordField('Password', [validators.Required('Please enter a password.')])
    submit = SubmitField('Sign In')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user and user.check_password(self.password.data):
            return True
        else:
            self.email.errors.append("Invalid e-mail or password.")
            return False

class LiftForm(Form):
    lift = TextField('Lift', [validators.Required('Please enter a lift.')])
    sets = IntegerField('Sets')
    reps = IntegerField('Reps')
    weight = FloatField('Weight')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

class RunForm(Form):
    distance = FloatField('Distance')
    duration = FloatField('Time')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

# class WorkOutForm(Form):
#     lifts = FieldList(FormField(LiftForm))
#     runs = FieldList(FormField(RunForm))
#     submit = SubmitField('Save')
