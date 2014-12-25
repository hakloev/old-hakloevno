var Main = (function ($) {
    
    var months = ["January", "February", "March", "April", "May",
                  "June", "July", "August", "September", "October",
                  "November", "December"];

    var days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    
    var bindNavMobile = function() {
        $('#nav-mobile').on('click', function(e) {
            e.preventDefault();
            $('.nav-fullscreen').slideToggle();
        });    
    }

    var alertDisassemble = function() {
        $('.alert-disassemble').on('click', function(e){
            e.preventDefault();
            $(this).parent().slideUp(350, function() {
                $(this).parent().remove();
            });
        });
    }

    var updateTime = function() {
        var now = new Date();
        var h = now.getHours();
        var m = now.getMinutes();
        var day = now.getDay();
        var month = now.getMonth();
        var date = now.getDate();
        if (m < 10) {
            m = "0" + m;
        }
        $('#clock-hour').text(h);
        $('#clock-minutes').text(m);
        $('#clock-date').text(days[day] + ', ' + months[month] + ' ' + date);
    }
    
    var hasScrolled = function() {
        if (!$('.nav-fullscreen').is(':hidden')) { $('.nav-fullscreen').hide() }
    }

    var activateResponsive = function() {
        bindNavMobile();
        var didScroll;
        var nav = $('.nav-fullscreen');
        $(window).resize(function() {
            if (window.innerWidth > 768) {
                nav.is(':hidden') ? nav.removeAttr('style') : "";
            }
        });
        $(window).scroll(function(e) {
            if (window.innerWidth < 768) {
                didScroll = true;
            }
        });
        setInterval(function() {
            if (didScroll) { hasScrolled(); didScroll = !didScroll };
        }, 350);
    }

    return {
        init: function() {
            alertDisassemble();
            setInterval(updateTime, 1000);
            activateResponsive();
        }
    }

})(jQuery);

$(window).on('load', function() {
    Main.init();
})
