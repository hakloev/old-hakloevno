$(document).ready(function () {
    $('.beer-admin-toggle').on('click', function () {
        $('.beer-admin-panel').slideToggle(350);
    });   

    $('.beer-stats-toggle').on('click', function() {
        $('.beer-stats-widget').slideToggle(350);
    });
});
