var Bus = (function ($) {
    
    var parsed = false;
    var runnedBefore = false;

    var resetInfo = function() {
        parsed = false;
        runnedBefore = false;
    }
    
    var parseInfo = function(place) {
        var departureList = [];
        for (var i = 0; i < place.next.length; i++) {
            if (place.next[i].l == "5") {
                departureList.push(place.next[i]);
            }
            if (departureList.length == 3) {
                break;
            }
        }
        printInfo(departureList);
    } 
    var printInfo = function(list) {
        parsed ? place = "#bus-berg" : place = "#bus-ila";
        var row = "";
        for (var i = 0; i < list.length; i++) {
            row += "<strong>" + list[i].t.substring(11, 16) + "</strong><small> &ndash; " + calcTime(list[i].t, list[i].rt) + "</small><br>"
        }
        $(place).html(row);
    }

     var calcTime = function(time, realtime) {
         var d = time.match(/^(\d{2}).(\d{2}).(\d{4}) (\d{2}):(\d{2})$/);
         var today = new Date();
         var departure = new Date(d[3], d[2] - 1, d[1], d[4], d[5]);
         var diff = Math.floor((departure.getTime() - today.getTime()) / (1000 * 60));
         if (diff <= -1 || diff <= 0) {
             return realtime ? "now (RT)" : "approx. now";
         } else {
             return (realtime ? (diff + " min (RT)") : "approx. " + diff + " min");
         }  
     }


    return {
        init: function() {
            $.ajax({
                type: "GET",
                url: "/bustimes/",
                dataType: "json",
                success: function(data) {
                    runnedBefore ? resetInfo() : $('#busloading').html("route 5, to the city center");
                    parseInfo(data.berg);
                    parsed = !parsed;
                    parseInfo(data.ila);
                    runnedBefore = !runnedBefore; 
                },
                error: function(xhr, options, error) {
                    $('#busloading').html("failed to load bus times.")
                    console.log("Failed to fetch bus data!");  
                }
            });
        }
    }
})(jQuery);

$(document).ready(function () {
    Bus.init();
    setInterval(Bus.init, 30000);
    $('.bus-toggle').on('click', function() {
        $('#bus-widget').slideToggle(350);
    });
});
