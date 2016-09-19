import json
from random import shuffle, randint
from models import Lift
from orderedset import OrderedSet

def make_dataset(label, color, values):
    return {
        'label':label,
        'fill': False,
        'lineTension': 0.25,
        'backgroundColor': color,
        # 'borderWidth': 3.,
        'borderColor': color,
        'borderCapStyle': 'butt',
        'borderDash': [],
        'borderDashOffset': 0.0,
        'borderJoinStyle': 'miter',
        'pointBorderColor': color,
        'pointBackgroundColor': '#fff',
        'pointBorderWidth': 5,
        'pointHoverRadius': 5,
        'pointHoverBackgroundColor': color,
        'pointHoverBorderColor': color,
        'pointHoverBorderWidth': 2,
        'pointRadius': 1,
        'pointHitRadius': 10,
        'showLine': True,
        'spanGaps': True,
        'data': values
        }

def create_chart(chart):
    colors = ['#0047ab', '#fb3640', '#605f5e', '#1d3461', '#247ba0']
    shuffle(colors)
    datasets = []
    activities = {}
    chartType = chart.chartType
    names = chart.activityNames
    title = names[0]
    if len(names) > 1:
        for i in range(len(names)-1):
            title += (' + ' + names[i+1])
    data_values = []
    dates = set()
    if chart.activityType == 'lift':
        for label in names:
            print label
            activities[label] = Lift.query.filter_by(name=label, user_id=chart.user_id).order_by(Lift.completed_time).all()
            print activities[label]
            for lift in activities[label]:
                dates.add(lift.completed_time)
        dates = sorted(dates)
        for label in names:
            lifts = Lift.query.filter_by(name=label, user_id=chart.user_id).order_by(Lift.completed_time).all()
            data_values.append([lift.weight for lift in activities[label]])
            yValues = []

            for date in dates:
                lift = Lift.query.filter_by(completed_time=date).filter_by(name=label).first()
                if lift:
                    if lift.weight != None:
                        yValues.append(lift.weight)
                elif not lift:
                    yValues.append(None)
            col = colors[randint(0,4)]
            dataset = make_dataset(label, col, yValues)
            datasets.append(dataset)
    elif chart.activityType == 'cardio':
        pass

    data = {
        'labels': [date.strftime('%m/%d/%Y') for date in dates],
        'datasets': datasets
        }
    chart_object = {
      'type': chartType,
      'data': data,
      'spanGaps': True,
      'options': {
            'title': {
                  'display': True,
                  'text': title,
                  'fontSize': 24,
                  'fontColor': 'black',
                  'fontFamily': 'Roboto'
                  },
            'scales': {
                'yAxes': [{
                    'ticks': {
                        'beginAtZero': True
                    }
                }]
            }
      },
    }
    return json.dumps(chart_object)
