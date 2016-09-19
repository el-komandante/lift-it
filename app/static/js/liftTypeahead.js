var substringMatcher = function(strs) {
  return function findMatches(q, cb) {
    var matches, substringRegex;

    matches = [];

    substrRegex = new RegExp(q, 'i');

    $.each(strs, function(i, str) {
      if (substrRegex.test(str)) {
        matches.push(str);
      }
    });

    cb(matches);

  };
};

var lifts = [
  'Squat',
  'Box Squat',
  'Hack Squat',
  'Front Squat',
  'Weighted Decline Sit Up',
  'Split Squat',
  'Leg Extension',
  'Standing Calf Raise',
  'Seated Calf Raise',
  'Reverse Calf Raise',
  'Deadlift',
  'Sumo Deadlift',
  'Rack Pull',
  'Stiff-leg Deadlift',
  'Trap Bar Deadlift',
  'Romanian Deadlift',
  'Lunge',
  'Walking Lunge',
  'Bench Press',
  'Dumbbell Bench Press',
  'Chest Press',
  'Incline Bench Press',
  'Decline Bench Press',
  'Dip',
  'Close Grip Bench Press',
  'Incline Close Grip Bench Press',
  'Skull Crusher',
  'Triceps Extension',
  'Cable Triceps Extension',
  'Tricep Pushdown',
  'Dumbbell Tricep Kickback',
  'Curl',
  'Cable Curl',
  'Dumbbell Curl',
  'Preacher Curl',
  'Concentration Curl',
  'Reverse Curl',
  'Hammer Curl',
  'Dumbbell Hammer Curl',
  'Wrist Curl',
  'Dumbbell Wrist Curl',
  'Reverse Wrist Curl',
  'Dumbbell Reverse Wrist Curl',
  'Bent Over Row',
  'Dumbbell Bent Over Row',
  'Incline Row',
  'Seated Row',
  'Chest Supported Row',
  'Chin Up',
  'Pull Up',
  'Lat Pullover',
  'Lat Pulldown',
  'Shrug',
  'Dumbbell Shrug',
  'Shoulder Press',
  'Cable Shoulder Press',
  'Seated Cable Shoulder Press',
  'Dumbbell Shoulder Press',
  'Overhead Press',
  'Cable Overhead Press',
  'Seated Cable Overhead Press',
  'Dumbbell Overhead Press',
  'Behind Neck Press',
  'Cable Behind Neck Press',
  'Military Press',
  'Seated Military Press',
  'Cable Military Press',
  'Seated Military Press',
  'Dumbbell Military Press',
  'Front Raise',
  'Cable Front Raise',
  'Seated Cable Front Raise',
  'Incline Front Raise',
  'Upright Row',
  'Cable Upright Row',
  'Dumbbell Upright Row',
  'Lateral Raise',
  'Seated Lateral Raise',
  'Dumbbell Lateral Raise',
  'Cable Lateral Raise',
  'Rear Delt Row',
];

var cardios = [
  'Run',
  'Sprint',
  'Bike',
  'Jump Rope',
  'Rowing Machine',
  'Swimming',
  'Cycling',
  'Boxing',
  'Dancing'
];

// $('#addLiftField').on('click', function() {
  // $('.lift-typeahead').each(function () {
    // if ($(this).parent().is('span')) {
        // $(this).typeahead('destroy');
      // }
    // $(this).typeahead({
    //   hint: false,
    //   highlight: true,
    //   minLength: 1
    // },
    // {
    //   name: 'lifts',
    //   source: substringMatcher(lifts)
    // });
    // $(this).attr('name', 'name');
  // }
  // }
// );
// });

// $('.addfields').on('click', function() {
//   $.each($('.cardio-typeahead'), function () {
//     if ($(this).parent().is('span')) {
//       $(this).typeahead('destroy');
//     }
//       $(this).typeahead({
//       hint: false,
//       highlight: true,
//       minLength: 1
//     },
//     {
//       name: 'cardios',
//       source: substringMatcher(cardios)
//     });
//   });
// });
