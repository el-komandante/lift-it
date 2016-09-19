/*jshint loopfunc: true */
function validateFields (inputs) {
  var errorCounter = 0;
  // console.log(inputs);
  for (var b = 0; b < inputs.length; b++) {
    if ($(inputs[b]).children().length > 1) {
      if ($(inputs[b]).children()[1].nodeName === 'SPAN') {
        // console.log(inputs[b]);
        name = $(inputs[b]).children('span').children('input').attr('name');
        value = $(inputs[b]).children('span').children('input').val();
      } else {
        name = $(inputs[b]).children('input').attr('name');
        value = $(inputs[b]).children('input').val();
      }
    } else {
        name = $(inputs[b]).children('input').attr('name');
        value = $(inputs[b]).children('input').val();
    }
    switch (name) {
      case 'name':
        // console.log($(inputs[b]));
        if (!(/\S/.test($($(inputs[b]).children('span')).children('input').val()))) {
          $(inputs[b]).children('span').children('input').addClass('animated shake formerror').one(
            'webkitAnimationEnd oanimationend oAnimationEnd msAnimationEnd animationend',
            function() {
              // console.log($(this));
              $(this).removeClass('animated shake');
            });
            $(inputs[b]).children('span').next('.error').html('This can\'t be blank.');
          errorCounter += 1;
        } else {
            $(inputs[b]).children('span').children('input').removeClass('formerror');
            $(inputs[b]).children('span').next('.error').html('&nbsp;');
          } break;

      case 'weight':
        if (!$.isNumeric(value)) {
          $(inputs[b]).children('input').addClass('animated shake formerror').one(
            'webkitAnimationEnd oanimationend oAnimationEnd msAnimationEnd animationend',
            function() {
              $(this).removeClass('animated shake');
            });
          $(inputs[b]).children('input').next('span').html('Please enter a number.');
          errorCounter += 1;
        } else {
          $(inputs[b]).children('input').removeClass('formerror');
          $(inputs[b]).children('input').next('span').html('&nbsp;');
          }break;

        case 'sets':
          if (!$.isNumeric(value)) {
            $(inputs[b]).children('input').addClass('animated shake formerror').one(
              'webkitAnimationEnd oanimationend oAnimationEnd msAnimationEnd animationend',
              function() {
                $(this).removeClass('animated shake');
              });
              $(inputs[b]).children('input').next().html('Please enter a number.');
            errorCounter += 1;
          } else {
            $(inputs[b]).children('input').removeClass('formerror');
            $(inputs[b]).children('input').next().html('&nbsp;');
            }break;

          case 'reps':
            if (!$.isNumeric(value)) {
              $(inputs[b]).children('input').addClass('animated shake formerror').one(
                'webkitAnimationEnd oanimationend oAnimationEnd msAnimationEnd animationend',
                function() {
                  $(this).removeClass('animated shake');
                });
                $(inputs[b]).children('input').next().html('Please enter a number.');
              errorCounter ++;
            } else {
              $(inputs[b]).children('input').removeClass('formerror');
              $(inputs[b]).children('input').next().html('&nbsp;');
              }break;

              case 'distance':
                if (!$.isNumeric(value)) {
                  $(inputs[b]).children('input').addClass('animated shake formerror').one(
                    'webkitAnimationEnd oanimationend oAnimationEnd msAnimationEnd animationend',
                    function() {
                      $(this).removeClass('animated shake');
                    });
                    $(inputs[b]).children('input').next().html('Please enter a number.');
                  errorCounter ++;
                } else {
                  $(inputs[b]).children('input').removeClass('formerror');
                  $(inputs[b]).children('input').next().html('&nbsp;');
                  }break;

              case 'duration':
                if (!$.isNumeric(value)) {
                  $(inputs[b]).children('input').addClass('animated shake formerror').one(
                    'webkitAnimationEnd oanimationend oAnimationEnd msAnimationEnd animationend',
                    function() {
                      $(this).removeClass('animated shake');
                    });
                    $(inputs[b]).children('input').next().html('Please enter a number.');
                  errorCounter ++;
                } else {
                  $(inputs[b]).children('input').removeClass('formerror');
                  $(inputs[b]).children('input').next().html('&nbsp;');
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
      var inputs = $($(liftFields)[f]).children('.form-group');
      errorCounter2 += validateFields(inputs);
    }
    for (var h = 0; h < cardioFields.length; h++) {
      inputs2 = $($(cardioFields)[h]).children('.form-group');
      errorCounter2 += validateFields(inputs2);
    }
    for (var x = 0; x < liftFields.length; x++) {
      var liftFormGroups = $(liftFields[x]).children('.form-group');
      // console.log(liftFormGroups);
      var grass = {};
      for (var k = 0; k < $(liftFormGroups).length; k++) {
        // console.log($(liftFormGroups[k]).children().nodeName);
        if ($(liftFormGroups[k]).children().length > 1) {
          if ($(liftFormGroups[k]).children()[1].nodeName == 'SPAN') {
            grass[$($(liftFormGroups[k]).children('span')).children('input').attr('name')] = $($(liftFormGroups[k]).children()).children('input').val();
          }
          else {
            grass[$(liftFormGroups[k]).children('input').attr('name')] = $(liftFormGroups[k]).children('input').val();
          }
        }
        else {
          grass[$(liftFormGroups[k]).children('input').attr('name')] = $(liftFormGroups[k]).children('input').val();
        }
      }
      data[$(liftFields[x]).attr('id')] = grass;
    }
    for (var m = 0; m < cardioFields.length; m++) {
      var cardioFormGroups = $(cardioFields[m]).children('.form-group');
      // console.log(cardioFormGroups);
      var brab = {};
      for (var n = 0; n < $(cardioFormGroups).length; n++) {
        brab[$(cardioFormGroups[n]).children('input').attr('name')] = $(cardioFormGroups[n]).children('input').val();
        if ($(cardioFormGroups[n]).children().length > 1) {
          if ($(cardioFormGroups[n]).children()[1].nodeName == 'SPAN') {
            brab[$($(cardioFormGroups[n]).children('span')).children('input').attr('name')] = $($(cardioFormGroups[n]).children()).children('input').val();
          }
          else {
            brab[$(cardioFormGroups[n]).children('input').attr('name')] = $(cardioFormGroups[n]).children('input').val();
          }
        }
        else {
          brab[$(cardioFormGroups[n]).children('input').attr('name')] = $(cardioFormGroups[n]).children('input').val();
        }
      }
      data[$(cardioFields[m]).attr('id')] = brab;
    }

    if (errorCounter2 === 0) {
      $('#save').button('loading');
      console.log(data);
      $.ajax({
        url: '/saveworkout/',
        data: JSON.stringify(data),
        type: 'POST',
        contentType: 'application/json',
        success: function(response) {
          console.log(data);
          console.log(response);
          setTimeout(function() {
            $('#save').button('reset');
          }, 2000);
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
