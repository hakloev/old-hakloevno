$(function() {
    var button = $('#mobile-nav-button')
    var menu = $('#main-nav ul')
    var menuHeight = menu.height;

    $(button).click(function(e) {
        e.preventDefault;
        $(menu).slideToggle()
    });
    
    $(window).resize(function() {
        var width = $(window).width()
        if (width > 320 && menu.is(':hidden')) { // Remember the pixels here!
            menu.removeAttr('style');
        }
    });

});
