var Main = (function ($) {
    
    var months = ["January", "February", "March", "April", "May",
                  "June", "July", "August", "September", "October",
                  "November", "December"];

    var days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
     
    var alertDisassemble = function() {
        $('.alert-disassemble').on('click', function(e){
            e.preventDefault();
            $(this).parent().fadeOut(200);
        });
    }

    var updateTime = function() {
        var now = new Date();
        var h = now.getHours();
        var m = now.getMinutes();
        var day = now.getDay();
        var month = now.getMonth();
        var date = now.getDate();
        $('#clock-hour').text(h);
        $('#clock-minutes').text(m);
        $('#clock-date').text(days[day] + ', ' + months[month] + ' ' + date);
    }

    return {
        init: function() {
            alertDisassemble();
            setInterval(updateTime, 1000);
        }
    }

})(jQuery);

$(window).on('load', function() {
    Main.init();
})
