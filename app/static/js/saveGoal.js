$(document).ready(function() {
  $('#goal-lift-names').multiselect({
    buttonClass: 'btn btn-default lift-multiselect',
    selectedClass: 'selected-lift'
  });

  $('#save-goal').on('click', function() {
    var data = {
      activityNames: [],
      chartType: $('#chart-type').val(),
      activityType: $('#activity-type').val()
    };
    var names = $('#goal-lift-names option:selected');
    for (q=0; q < names.length; q++) {
      data.activityNames.push($(names[q]).val());
    }
    $('#save-goal').button('loading');
    $.ajax({
      url: '/goals/',
      data: JSON.stringify(data),
      type: 'POST',
      contentType: 'application/json',
      success: function(response) {
        setTimeout(function() {
          $('#save-goal').button('reset');
        }, 2000);
        console.log(response);
        console.log(data);
      }
    });
  });
});
