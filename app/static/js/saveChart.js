$(document).ready(function() {

  $('#chart-lift-names').multiselect({
    buttonClass: 'btn btn-default lift-multiselect',
    selectedClass: 'selected-lift'
  });

  $('#save-chart').on('click', function() {
    var data = {
      activityNames: [],
      chartType: $('#chart-type').val(),
      activityType: $('#activity-type').val()
    };
    var names = $('#chart-lift-names option:selected');
    for (q=0; q < names.length; q++) {
      data.activityNames.push($(names[q]).val());
    }
    $('#save-chart').button('loading');
    $.ajax({
      url: '/charts/',
      data: JSON.stringify(data),
      type: 'POST',
      contentType: 'application/json',
      success: function(response) {
        setTimeout(function() {
          $('#save-chart').button('reset');
        }, 2000);
        console.log(response);
        console.log(data);
      }
    });
  });
});
