/*jshint loopfunc: true */
function validateFields (inputs) {
  var errorCounter = 0;
  for (var b = 0; b < inputs.length; b++) {
    var name = $(inputs[b]).attr('name');
    var value = $(inputs[b]).val();
    switch (name) {
      case 'name':
        if (!(/\S/.test($(inputs[b]).val()))) {
          $(inputs[b]).addClass('animated shake formerror').one(
            'webkitAnimationEnd oanimationend oAnimationEnd msAnimationEnd animationend',
            function() {
              $(this).removeClass('animated shake');
            });
            $(inputs[b]).next().html('This can\'t be blank.');
          errorCounter += 1;
        } else {
            $(inputs[b]).removeClass('formerror');
            $(inputs[b]).next().html('&nbsp;');
          } break;

      case 'weight':
        if (!$.isNumeric(value)) {
          $(inputs[b]).addClass('animated shake formerror').one(
            'webkitAnimationEnd oanimationend oAnimationEnd msAnimationEnd animationend',
            function() {
              $(this).removeClass('animated shake');
            });
          $(inputs[b]).next().html('Please enter a number.');
          errorCounter += 1;
        } else {
          $(inputs[b]).removeClass('formerror');
          $(inputs[b]).next().html('&nbsp;');
          }break;

        case 'sets':
          if (!$.isNumeric(value)) {
            $(inputs[b]).addClass('animated shake formerror').one(
              'webkitAnimationEnd oanimationend oAnimationEnd msAnimationEnd animationend',
              function() {
                $(this).removeClass('animated shake');
              });
              $(inputs[b]).next().html('Please enter a number.');
            errorCounter += 1;
          } else {
            $(inputs[b]).removeClass('formerror');
            $(inputs[b]).next().html('&nbsp;');
            }break;

          case 'reps':
            if (!$.isNumeric(value)) {
              $(inputs[b]).addClass('animated shake formerror').one(
                'webkitAnimationEnd oanimationend oAnimationEnd msAnimationEnd animationend',
                function() {
                  $(this).removeClass('animated shake');
                });
                $(inputs[b]).next().html('Please enter a number.');
              errorCounter ++;
            } else {
              $(inputs[b]).removeClass('formerror');
              $(inputs[b]).next().html('&nbsp;');
              }break;

              case 'distance':
                if (!$.isNumeric(value)) {
                  $(inputs[b]).addClass('animated shake formerror').one(
                    'webkitAnimationEnd oanimationend oAnimationEnd msAnimationEnd animationend',
                    function() {
                      $(this).removeClass('animated shake');
                    });
                    $(inputs[b]).next().html('Please enter a number.');
                  errorCounter ++;
                } else {
                  $(inputs[b]).removeClass('formerror');
                  $(inputs[b]).next().html('&nbsp;');
                  }break;

                  case 'duration':
                    if (!$.isNumeric(value)) {
                      $(inputs[b]).addClass('animated shake formerror').one(
                        'webkitAnimationEnd oanimationend oAnimationEnd msAnimationEnd animationend',
                        function() {
                          $(this).removeClass('animated shake');
                        });
                        $(inputs[b]).next().html('Please enter a number.');
                      errorCounter ++;
                    } else {
                      $(inputs[b]).removeClass('formerror');
                      $(inputs[b]).next().html('&nbsp;');
                      }break;

          default:
            break;
    }
  }
  return errorCounter;
}

$(document).ready(function() {
  $('#save').click(function() {
    var data = {};
    var errorCounter2 = 0;
    var liftFields = $('.liftField.workout-form.live');
    var cardioFields = $('.runField.workout-form.live');
    for (var f = 0; f < $(liftFields).length; f++) {
      var inputs = $($(liftFields)[f]).children('.form-group').children('input');
      errorCounter2 += validateFields(inputs);
    }
    for (var h = 0; h < cardioFields.length; h++) {
      inputs2 = $($(cardioFields)[h]).children('.form-group').children('input');
      errorCounter2 += validateFields(inputs2);
    }
    for (var x = 0; x < liftFields.length; x++) {
      var liftFormGroups = $(liftFields[x]).children('.form-group');
      console.log(liftFormGroups);
      var grass = {};
      for (var k = 0; k < $(liftFormGroups).length; k++) {
        grass[$(liftFormGroups[k]).children('input').attr('name')] = $(liftFormGroups[k]).children('input').val();
      }
      data[$(liftFields[x]).attr('id')] = grass;
    }
    for (var m = 0; m < cardioFields.length; m++) {
      var cardioFormGroups = $(cardioFields[m]).children('.form-group');
      console.log(cardioFormGroups);
      var brab = {};
      for (var n = 0; n < $(cardioFormGroups).length; n++) {
        brab[$(cardioFormGroups[n]).children('input').attr('name')] = $(cardioFormGroups[n]).children('input').val();
      }
      data[$(cardioFields[m]).attr('id')] = brab;
    }

    if (errorCounter2 === 0) {
      $.ajax({
        url: '/saveworkout/',
        data: JSON.stringify(data),
        type: 'POST',
        contentType: 'application/json',
        success: function(response) {
          console.log(data);
          console.log(response);
          $('.live').addClass('animated fadeOutLeft').one(
            'webkitAnimationEnd oanimationend oAnimationEnd msAnimationEnd animationend',
            function(event) {
              $('#workout-modal').modal('hide').one('hidden.bs.modal', function() {
                $('.live').remove();
              });
            });
        },
        error: function(error) {
          console.log(error);
        }
      });
    }
  });
});
