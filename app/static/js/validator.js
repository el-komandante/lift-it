var validator = {}

validator.util = {
  setupFormValidation: function() {
    $('addWorkout').validate({
      rules: {
        name: 'required',
        weight: {
          required: true,
          number: true
        },
        sets: {
          required: true,
          number: true
        },
        reps: {
          required: true,
          number: true
        }
      },
      messages: {
        name: 'Please enter the name of an exercise.',
        
      }
    })
  }
}
