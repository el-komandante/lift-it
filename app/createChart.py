def createChart(chart):
    colors = ['#0047ab', '#fb3640', '#605f5e', '#1d3461', '#247ba0']
    shuffle(colors)
    datasets = []
    xlabels = []
    activities = {}
    names = chart.activityNames
    data = {}
    if chart.type == 'line':
        chartType = 'line'
        data_values =
        dates = set()
        for label in chart.Activitynames:
            activities[label] = Lift.query.filter_by(name=label, user_id=chart.user_id).all()
            dates.add([lift.completed_time for lift in activities[label]])
        for label in chart.activityNames:
            data_values.append([lift.weight for lift in lifts])
            xlabels.append([lift.workout.completed_time.strftime('%Y-%m-%d') for lift in lifts])
            lifts = Lift.query.filter_by(name=str(chart.activityName), user_id=user.id).order_by(Lift.completed_time).all()
            for date in dates:
                for lift in lifts:
                    if date.date == lift.completed_time.date:
                        data.append(lift.weight)
                    else:
                        data.append(None)
            yValues = []
            dataset = {
                'label':label,
                'fill': False,
                'lineTension': 0,
                'backgroundColor': colors[0],
                'borderColor': colors[0],
                'borderCapStyle': 'butt',
                'borderDash': [],
                'borderDashOffset': 0.0,
                'borderJoinStyle': 'miter',
                'pointBorderColor': colors[0],
                'pointBackgroundColor': '#fff',
                'pointBorderWidth': 5,
                'pointHoverRadius': 5,
                'pointHoverBackgroundColor': ((colors[0] & 0x7E7E7E) >> 1),
                'pointHoverBorderColor': ((colors[0] & 0x7E7E7E) >> 1),
                'pointHoverBorderWidth': 2,
                'pointRadius': 1,
                'pointHitRadius': 10,
                'data': yValues
                }
            datasets.append(dataset)
        data = {
            'labels': dates,
            'datasets': datasets
        }
        chart = {
          'type': chartType,
          'data': data,
          'options': {
                'title': {
                      display: true,
                      text: string,
                      fontSize: 24,
                      fontColor: 'black',
                      fontFamily: 'Roboto'
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

    return chart
