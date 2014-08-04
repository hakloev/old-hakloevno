$(document).ready(function () {
    $('.adminpanel').hide();
    $('#adminbutton').on('click', function () {
        $('.adminpanel').slideToggle(350);
    });    
});
