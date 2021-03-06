from app import app
from flask import render_template, request, flash, session, url_for, redirect
from forms import SignupForm, SigninForm, RunForm, LiftForm
from models import User, db, Cardio, Lift, Workout, Chart
from sqlalchemy import func
from collections import OrderedDict
import json
from random import shuffle
from orderedset import OrderedSet
from create_chart import create_chart
import datetime


@app.route('/', methods=['GET', 'POST'])
def home():
    signin_form = SigninForm(prefix='signin_form')
    signup_form = SignupForm(prefix='signup_form')

    if signup_form.validate_on_submit() and signup_form.submit.data:
        newuser = User(signup_form.username.data, signup_form.email.data, signup_form.password.data)
        db.session.add(newuser)
        db.session.commit()
        return redirect(url_for('dashboard'))


    elif signin_form.validate_on_submit() and signin_form.submit.data:
        session['email'] = signin_form.email.data
        return redirect(url_for('dashboard'))

    return render_template('frontpage.html', signin_form=signin_form, signup_form=signup_form)

# @app.route('/login/', methods=['GET', 'POST'])
# def login():
#     l_form = SigninForm(request.form, prefix='login-form')
#
#     if l_form.validate() == False:
#         return render_template('frontpage.html', lform=l_form, rform=SignupForm())
#     else:
#         session['email'] = l_form.email.data
#         return redirect(url_for('dashboard'))
#
@app.route('/signout/', methods=['GET', 'POST'])
def signout():
    if 'email' not in session:
        return redirect(url_for('home'))
    session.pop('email', None)
    return redirect(url_for('home'))

# @app.route('/register/', methods=['GET', 'POST'])
# def register():
#     r_form = SignupForm(request.form, prefix='register-form')
#
#     if r_form.validate() == False:
#         return render_template('frontpage.html', rform=r_form, lform=SigninForm())
#     else:
#         newuser = User(r_form.username.data, r_form.email.data, r_form.password.data)
#         db.session.add(newuser)
#         db.session.commit()
#
#         session['email'] = newuser.email
#         return redirect(url_for('dashboard'))


@app.route('/dashboard/', methods=['GET', 'POST'])
def dashboard():
    # return render_template('dashboard.html')
    if 'email' not in session:
        return redirect(url_for('home'))

    user = User.query.filter_by(email = session['email']).first()

    # Create list of 5 most recent workouts, date headings, and dropdown href id's
    recent_workouts = user.get_recent_workouts()
    dates = [workout.completed_time.strftime('%m/%d/%Y') for workout in recent_workouts]
    counters = [1, 2, 3, 4, 5]
    recent_workouts = zip(recent_workouts, dates, counters)
    goals = user.get_goals()
    goal_progress = []
    current_progress = []
    for goal in goals:
        if goal.type.code == 'lift':
            weight = max([lift.weight for lift in Lift.query.filter_by(user_id=user.id, name=goal.name).all()])
            progress = int((weight/goal.weight)*100)
            goal_progress.append(progress)
            current_progress.append(weight)
        elif goal.type.code == 'cardio':
            goal_progress.append(Cardio.query.filter_by(user_id=user.id, name=goal.name).order_by(Cardio.completed_time).first().duration)

    goals = zip(goals, goal_progress, current_progress)

    #List first three charts
    charts = user.get_charts()
    chart_json = []

    lift_names = user.get_lift_names()
    cardio_names = user.get_cardio_names()
    # Generate chart labels and query associated activities by name and user id
    for chart in charts:
        chart_json.append(create_chart(chart))
    if user is None:
        return redirect(url_for('home'))
    else:
        return render_template('dashboard.html', signup_form=SignupForm(), signin_form=SigninForm(), recent_workouts=recent_workouts, charts=chart_json, goals=goals, lift_names=lift_names)


@app.route('/about/')
def about():
    return render_template('about.html', signup_form=SignupForm(), signin_form=SigninForm())

@app.route('/saveworkout/', methods=['POST'])
def saveworkout():
    user = User.query.filter_by(email = session['email']).first()
    workout = Workout(user, None)
    db.session.add(workout)
    activities = json.loads(request.data)
    print activities

    for activity in activities:
        newActivity = activities[activity]
        if newActivity['type'] == 'lift':
            new = Lift(workout, newActivity['name'], int(newActivity['weight']), int(newActivity['sets']), int(newActivity['reps']))
            db.session.add(new)
        elif newActivity['type'] == 'cardio':
            new = Cardio(workout, newActivity['name'], datetime.timedelta(hours=int(newActivity['duration']['hours']), minutes=int(newActivity['duration']['minutes']), seconds=int(newActivity['duration']['seconds'])), float(newActivity['distance']))
            db.session.add(new)

    db.session.commit()
    return json.dumps({'status':'OK', 'status_code': 201})

@app.route('/myworkouts/', methods=['GET'])
def myworkouts():
    if 'email' not in session:
        return redirect(url_for('home'))

    user = User.query.filter_by(email = session['email']).first()

    if user is None:
        return redirect(url_for('home'))

    #Create top-level headings (labeled by month) and sub-headings for individual workouts
    dates = db.session.query(func.date_trunc('month', Workout.completed_time)).filter_by(user_id = user.id).distinct().all()
    workouts = Workout.query.filter_by(user_id = user.id).order_by(Workout.completed_time.desc()).all()
    workouts_sorted = OrderedDict()
    for date in dates:
        workouts_sorted.update({date[0].strftime('%B'):[]})
    for workout in workouts:
        for month in dates:
            if workout.completed_time.month == month[0].month:
                workouts_sorted[month[0].strftime('%B')].append(workout)
    for month in workouts_sorted:
        for workout in workouts_sorted[month]:
            print workout.cardios, workout.lifts, workout.user_id
    return render_template('myworkouts.html', workouts=workouts_sorted, signin_form=SigninForm(), signup_form=SignupForm())

@app.route('/charts/', methods=['GET', 'POST'])
def charts():
    if 'email' not in session:
        return None
    elif request.method == 'POST':
        chart_data = json.loads(request.data)
        user = User.query.filter_by(email = session['email']).first()
        chart = Chart(chart_data['chartType'].lower(), user, chart_data['activityNames'], chart_data['activityType'].lower())
        db.session.add(chart)
        db.session.commit()
        return json.dumps({'status': 'OK', 'status_code': 201})

@app.route('/goals/', methods=['GET', 'POST'])
def goals():
    if 'email' not in session:
        return None
    elif request.method == 'POST':
        goal_data = json.loads(request.data)
        user = User.query.filter_by(email = session['email']).first()
        goal = Goal(chart_data['chartType'].lower(), user, chart_data['activityNames'], chart_data['activityType'].lower())
        if goal.type == 'lift':
            goal.weight = goal_data.weight
        elif goal.type == 'cardio':
            goal.duration = goal_data.duration

        db.session.add(goal)
        db.session.commit()
        return json.dumps({'status': 'OK', 'status_code': 201})
