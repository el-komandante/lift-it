from app import app, db
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import pytz
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy_utils import ChoiceType

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    pw_hash = db.Column(db.String(255), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    date_registered = db.Column(db.DateTime, default=datetime.now(pytz.utc), nullable=False)


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def is_active(self):
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False
    def get_recent_workouts(self):
        return Workout.query.filter_by(user_id=self.id).order_by(Workout.completed_time.desc()).limit(5).all()

    def get_goals(self):
        return Goal.query.filter_by(user_id=self.id).filter_by(show=True).all()

    def get_charts(self):
        return Chart.query.filter_by(user_id=self.id).all()

    def get_lift_names(self):
        return db.session.query(Lift.name.distinct()).filter_by(user_id=self.id).all()

    def get_cardio_names(self):
        return db.session.query(Cardio.name.distinct()).filter_by(user_id=self.id).all()

    def __repr__(self):
        return '<User (username="%r">, email="%r", id="%r")>' % (self.username, self.email, self.id)

class Cardio(db.Model):
    __tablename__ = 'cardios'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    duration = db.Column(db.Interval)
    distance = db.Column(db.Integer)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    created_time = db.Column(db.DateTime, default=datetime.now(pytz.utc), nullable=False)
    workout = db.relationship('Workout', backref='cardios')
    user_id = db.Column(db.Integer)

    def __init__(self, workout, name, duration, distance):
        self.workout = workout
        self.name = name
        self.duration = duration
        self.distance = distance
        self.user_id = workout.user.id

    def get_duration_as_int(self):
        return self.duration.total_seconds()

    def __repr__(self):
        return '<Cardio (name="%r", id="%r")>' % (self.name, self.id)

class Lift(db.Model):
    __tablename__ = 'lifts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    weight = db.Column(db.Float)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    created_time = db.Column(db.DateTime)
    workout = db.relationship('Workout', backref='lifts')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    completed_time = db.Column(db.DateTime)
    created_time = db.Column(db.DateTime, default=datetime.now(pytz.utc), nullable=False)


    def __init__(self, workout, name, weight, sets, reps):
        self.workout = workout
        self.name = name
        self.weight = weight
        self.sets = sets
        self.reps = reps
        self.created_time = datetime.now(pytz.utc)
        self.workout_id = workout.id
        self.user_id = workout.user_id
        self.completed_time = workout.completed_time

    def __repr__(self):
        return '<Lift (name="%r", id="%r")>' % (self.name, self.id)

class Workout(db.Model):
    __tablename__ = 'workouts'
    id = db.Column(db.Integer, primary_key=True)
    completed_time = db.Column(db.DateTime, default=datetime.now(pytz.utc), nullable=False)
    user_id = db.Column(db.ForeignKey('users.id'))
    user = db.relationship('User', backref='workouts')
    created_time = db.Column(db.DateTime, default=datetime.now(pytz.utc), nullable=False)


    def __init__(self, user, completed_time):
        self.user = user
        if completed_time is None:
            completed_time = datetime.now(pytz.utc)
        self.completed_time = completed_time
        self.user_id = user.id

    def __repr__(self):
        return '<Workout (completed_time="%r", id="%r")>' % (self.completed_time, self.id)

class Goal(db.Model):
    __tablename__ = 'goals'
    TYPES = [
        ('lift', 'Lift'),
        ('cardio', 'Cardio')
    ]
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('users.id'))
    user = db.relationship('User', backref='goals')
    type = db.Column(ChoiceType(TYPES))
    name = db.Column(db.String(70))
    weight = db.Column(db.Integer)
    duration = db.Column(db.Interval)
    created_time = db.Column(db.DateTime, default=datetime.now(pytz.utc), nullable=False)
    show = db.Column(db.Boolean, default=True)

    def __init__(self, user, name, type):
        self.user = user
        self.type = type
        self.user_id = user.id
        self.display = True

    def __repr__(self):
        return '<Goal (type="%r", name="%r" id="%r")>' % (self.type, self.name, self.id)


class Chart(db.Model):
    __tablename__ = 'charts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('users.id'))
    chartType = db.Column(db.String(40))
    activityType = db.Column(db.String(10))
    display = db.Column(db.Boolean(), default=True)
    user = db.relationship('User', backref='charts')
    activityNames = db.Column(ARRAY(db.String(70)))
    created_time = db.Column(db.DateTime, default=datetime.now(pytz.utc), nullable=False)

    def __init__(self, chartType, user, activityNames, activityType):
        self.chartType = chartType
        self.user = user
        self.user_id = user.id
        self.display = True
        self.activityNames = activityNames
        self.activityType = activityType

    def __repr__(self):
        return '<Chart (chartType="%r", id="%r", activityNames="%r")>' % (self.chartType, self.id, self.activityNames)
