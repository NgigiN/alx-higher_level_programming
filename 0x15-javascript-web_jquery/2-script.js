// Updates the text color of the <header> to red #FF0000
// when the user clicks on the tag DIV#red_header
// can't use document.querySelector
// must use JQuery API

document.getElementById('red_header').addEventListener('click', function () { $('header').css('color', '#FF0000') })
