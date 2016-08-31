from app import app
from flask import render_template, request, flash, session, url_for, redirect
from forms import SignupForm, SigninForm, RunForm, LiftForm
from models import User, db, Cardio, Lift, Workout, Chart
from sqlalchemy import func
from collections import OrderedDict
import json
from random import shuffle

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
    recent_workouts = Workout.query.filter_by(user_id = user.id).order_by(Workout.completed_time.desc()).limit(5).all()
    dates = [workout.completed_time.strftime('%m/%d/%Y') for workout in recent_workouts]
    counters = [1, 2, 3, 4, 5]
    recent_workouts = zip(recent_workouts, dates, counters)

    colors = ['#0047ab', '#fb3640', '#605f5e', '#1d3461', '#247ba0']
    shuffle(colors)

    #List first three charts + instantiate data variables
    charts = Chart.query.filter_by(user_id = user.id).limit(3).all()
    data_values = []
    xlabels = []
    chartlabels = []

    # Generate chart labels and query associated activities by name and user id
    for chart in charts:
        chartlabels.append(chart.activityName)
        if chart.activityType == 'lift':
            lifts = Lift.query.filter_by(name=str(chart.activityName), user_id=user.id).order_by(Lift.completed_time).all()
            data_values.append([lift.weight for lift in lifts])
            xlabels.append([lift.workout.completed_time.strftime('%Y-%m-%d') for lift in lifts])

    if user is None:
        return redirect(url_for('home'))
    else:
        return render_template('dashboard.html', signup_form=SignupForm(), signin_form=SigninForm(), recent_workouts=recent_workouts, charts=charts, data_values=data_values, xlabels=xlabels, chartColors=colors)


@app.route('/about/')
def about():
    return render_template('about.html', signup_form=SignupForm(), signin_form=SigninForm())

@app.route('/saveworkout/', methods=['POST'])
def saveworkout():
    user = User.query.filter_by(email = session['email']).first()
    workout = Workout(user, None)
    db.session.add(workout)
    activities = json.loads(request.data)

    for activity in activities:
        newActivity = activities[activity]
        if newActivity['type'] == 'lift':
            new = Lift(workout, newActivity['name'], int(newActivity['weight']), int(newActivity['sets']), int(newActivity['reps']))
            db.session.add(new)
        elif newActivity['type'] == 'cardio':
            new = Cardio(workout, newActivity['name'], newActivity['duration'], float(newActivity['distance']))
            db.session.add(new)


    db.session.commit()
    return json.dumps({'status':'OK'})

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
    return render_template('myworkouts.html', workouts=workouts_sorted, signin_form=SigninForm(), signup_form=SignupForm())
