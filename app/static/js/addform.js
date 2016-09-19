var liftCounter = 0;
var runCounter = 0;
function addLiftField() {
  // liftCounter++;
  // var newLiftField = $('#liftField').clone();
  // $(newLiftField[0].div).attr('class', 'form-group field');
  // console.log(newLiftField[0]);
  // $('#formanchor').append(newLiftField[0]);
  var newLiftFields = document.getElementById('liftField').cloneNode(true);
  newLiftFields.id = '';
  newLiftFields.style.display = 'inline-block';
  var newLiftField = newLiftFields.childNodes;
  for (var i = 0; i<newLiftField.length; i++) {
    var theName = newLiftField[i].name;
    if (theName) {
      newLiftField[i].name = theName + liftCounter;
    }
  }
  // var children = newLiftFields.getElementsByTagName('div');
  // for (var x = 0; x < children.length; x) {
  //   chilren[x].className = ''
  // }
  for (var x = 0; x < newLiftFields.getElementsByTagName('div').length; x++) {
    newLiftFields.getElementsByTagName('div')[x].className = 'form-group field';
  }
  $(newLiftFields).addClass('live');
  $(newLiftFields).children().addClass('live');
  for (var g = 0; g < $(newLiftFields).children().length; g++) {
    $($(newLiftFields).children()[g]).children().addClass('live');
  }
  newLiftFields.id = 'liftField-workout-form-live' + liftCounter;
  $($(newLiftFields).children('.form-group')[1]).children('input').typeahead({
    hint: false,
    highlight: true,
    minLength: 1
  },
  {
    name: 'lifts',
    source: substringMatcher(lifts)
  });
  $(newLiftFields).addClass('animated fadeIn');
  var insertHere = document.getElementById('formanchor');
  insertHere.parentNode.insertBefore(newLiftFields, insertHere);
  liftCounter++;
}

function addRunField() {
  var newRunFields = document.getElementById('runField').cloneNode(true);
  newRunFields.id = 'runField'+runCounter;
  newRunFields.style.display = 'inline-block';
  var newRunField = newRunFields.childNodes;
  for (var i = 0; i<newRunField.length; i++) {
    var theName = newRunField[i].name;
    if (theName) {
      newRunField[i].name = theName + runCounter;
    }
  }
  for (var x = 0; x < newRunFields.getElementsByTagName('div').length; x++) {
    newRunFields.getElementsByTagName('div')[x].className = 'form-group field';
  }
  $(newRunFields).addClass('live');
  $(newRunFields).children().addClass('live');
  for (var g = 0; g < $(newRunFields).children().length; g++) {
    $($(newRunFields).children()[g]).children().addClass('live');
  }
  $($(newRunFields).children('.form-group')[1]).children('input').typeahead({
    hint: false,
    highlight: true,
    minLength: 1
  },
  {
    name: 'cardios',
    source: substringMatcher(cardios)
  });

  $(newRunFields).addClass('animated fadeIn');
  var insertHere = document.getElementById('formanchor');
  insertHere.parentNode.insertBefore(newRunFields, insertHere);
  runCounter++;
}

function removeField() {
  $(this).closest('.liftField').remove();
}
