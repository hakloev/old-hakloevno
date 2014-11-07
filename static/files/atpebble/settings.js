window.atpebble = window.atpebble || {}

atpebble.settings = ( function ($) {
     
    var initAll = $.ajax({
        url: 'stops.json',
        dataType: 'json',
        success: function (data) {
            window.busStops = data;
            init(); // Init the rest
        }.bind(this),
        error: function (xhr, status, err) {
            console.log(url, status, err.toString());
        }.bind(this)
    });

    var init = function() {
        var globalTimeout = null;
        $(".search").keyup(function(event) {
            button = this
            if (globalTimeout != null) {
                clearTimeout(globalTimeout);
            }
            globalTimeout = setTimeout(function() {
                globalTimeout = null;
                list = atpebble.stops.searchStopsByName(button.value);
                atpebble.stops.addStopsToList(list, button.id.match(/(\d+)/)[1]);
            }, 300)
        });

        var stopId1 = getURLVariable('stopId1');
        var stopId2 = getURLVariable('stopId2');
        var route = getURLVariable('route');

        if (stopId1 !== false) { 
            $("#stopId1").val(stopId1); 
            var stopName1 = atpebble.stops.searchStopsByLocationId(stopId1).name;
            $("#stopName1").val(stopName1 + " " + atpebble.stops.setDirection(stopId1)); 
        }
        if (stopId2 !== false) { 
            $("#stopId2").val(stopId2); 
            var stopName2 = atpebble.stops.searchStopsByLocationId(stopId2).name;
            $("#stopName2").val(stopName2 + " " +atpebble.stops.setDirection(stopId2)); 
        }
        if (route !== false) { 
            $("#route").val(route); 
        }
    }

    var saveOptions = function() {
        var options = {
            'stopId1': $("#stopId1").val(),
            'stopId2': $("#stopId2").val(),
            'route': $("#route").val()
        }
        return options;
    }

    var getURLVariable = function(name) {
        var query = window.location.search.substring(1);
        var vars = query.split("&");
        for (var i = 0; i < vars.length; i++) {
            var pair = vars[i].split("=");
            if(pair[0] == name){return pair[1]};
        }
        return false;
    }           

    return {
        saveOptions:saveOptions,
        initAll:initAll
    }

})(jQuery);

