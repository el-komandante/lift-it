from app.models import User, Workout, Lift
from app import db
from datetime import datetime
import pytz
from random import randint

user = User.query.filter_by(email = 'test2@test.com').first()
session = db.session()
# user = User('test2', 'test2@test.com', 'test')
for i in range(1, 15):
    workout = Workout(user, datetime(2016, 8, i, 12, 0, 0, tzinfo=pytz.utc))
    print workout
    session.add(workout)
    lift1 = Lift(workout, 'Deadlift', randint(100, 600), randint(1, 10), randint(1, 15))
    lift2 = Lift(workout, 'Squat', randint(100, 600), randint(1, 10), randint(1, 15))
    print 'lift1 ' + str(lift1.weight), 'lift2 ' + str(lift2.weight)
    session.add(lift1)
    session.add(lift2)
    session.commit()
