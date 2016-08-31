var ctx1 = document.getElementById('chart1');
var data = {
  labels: ['6/10/2016', '6/13/2016', '6/20/2016', '6/25/2016', '6/30/2016', '7/3/2016', '7/10/2016'],
  datasets: [
    {
      label: 'Squat',
      fill: false,
      lineTension: 0.1,
      backgroundColor: "#007FFF",
      borderColor: "#007FFF",
      borderCapStyle: 'butt',
      borderDash: [],
      borderDashOffset: 0.0,
      borderJoinStyle: 'miter',
      pointBorderColor: "#007FFF",
      pointBackgroundColor: "#fff",
      pointBorderWidth: 5,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(75,192,192,1)",
      pointHoverBorderColor: "rgba(220,220,220,1)",
      pointHoverBorderWidth: 2,
      pointRadius: 1,
      pointHitRadius: 10,
      data: [100, 150, 200, 175, 180, 190, 225],
    }
  ]
};
var chart1 = new Chart(ctx1, {
  type: 'line',
  data: data,
  options: {
      title: {
              display: true,
              text: 'Squat',
              fontSize: 24,
              fontColor: 'black',
              fontFamily: 'Roboto'
          },
      scales: {
          yAxes: [{
              ticks: {
                  beginAtZero:true
              }
          }]
      }
  },
  spanGaps: true,
});

// chart 2
var ctx2 = document.getElementById('chart2');
var data2 = {
  labels: ['6/10/2016', '6/13/2016', '6/20/2016', '6/25/2016', '6/30/2016', '7/3/2016', '7/10/2016'],
  datasets: [
    {
      label: 'Squat',
      fill: false,
      lineTension: 0,
      backgroundColor: "#007FFF",
      borderColor: "#007FFF",
      borderCapStyle: 'butt',
      borderDash: [],
      borderDashOffset: 0.0,
      borderJoinStyle: 'miter',
      pointBorderColor: "#007FFF",
      pointBackgroundColor: "#fff",
      pointBorderWidth: 5,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(75,192,192,1)",
      pointHoverBorderColor: "rgba(220,220,220,1)",
      pointHoverBorderWidth: 2,
      pointRadius: 1,
      pointHitRadius: 10,
      data: [100, 150, 200, 175, 180, 190, 225],
      spanGaps: true,
    },
    {
      label: 'Deadlift',
      fill: false,
      lineTension: 0,
      backgroundColor: "#13293d",
      borderColor: "#13293d",
      borderCapStyle: 'butt',
      borderDash: [],
      borderDashOffset: 0.0,
      borderJoinStyle: 'miter',
      pointBorderColor: "#13293d",
      pointBackgroundColor: "#fff",
      pointBorderWidth: 5,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(75,192,192,1)",
      pointHoverBorderColor: "rgba(220,220,220,1)",
      pointHoverBorderWidth: 2,
      pointRadius: 1,
      pointHitRadius: 10,
      data: [140, 170, 220, null, 250, 190, 270],
      spanGaps: true,
    },
  ]
};

var chart2 = new Chart(ctx2, {
  type: 'line',
  data: data2,
  options: {
    title: {
      display: true,
      text: 'Squat + Deadlift',
      fontSize: 24,
      fontColor: 'black',
      fontFamily: 'Roboto'
    },
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero:true
        }
      }]
    }
  },
});
