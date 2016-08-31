from app.models import User, Workout, Lift
from app import db
from datetime import datetime
import pytz
from random import randint

user = User.query.filter_by(email = 'test3@test.com').first()
session = db.session()

for i in range(15):
    workout = Workout(user, datetime(2016, 8, i, 12, 0, 0, tzinfo=pytz.utc))
    print workout
    session.add(workout)
    lift1 = Lift(workout, 'Deadlift', randint(200, 600), randint(1, 10), randint(1, 15))
    lift1 = Lift(workout, 'Squat', randint(200, 600), randint(1, 10), randint(1, 15))
    session.add(lift1)
    session.add(lift2)
    session.commit()
