$(document).ready(function () {
  // easy way to get it done
  $('#toggle_header').click(function () {
    $('header').toggleClass('green red');
  });
//   $('#toggle_header').click(function () {
//     if ($('header').hasClass('green')) {
//       $('header').removeClass('green');
//       $('header').addClass('red');
//     } else {
//       $('header').removeClass('red');
//       $('header').addClass('green');
//     }
//   });
});
