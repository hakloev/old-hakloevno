window.atpebble = window.atpebble || {}

atpebble.stops = ( function ($) {

    window.busStops = window.busStops || {};
    
    var setBusToStop = function(element) {
        buttonId = $(element).closest("ul").attr('id').match(/(\d+)/)[1]
        $("#stopId" + buttonId).val($(element).attr('id'))
        $("#stopName" + buttonId).val($(element).html())
        $("#stops" + buttonId).empty()
    }

    var addStopsToList = function(stops, listId) {
        var list = "";
        stops.forEach(function(stop){
            list += '<li><a id="' + stop.locationId + '" onclick="atpebble.stops.setBusToStop(this)">' + stop.name + " " + setDirection(stop.locationId) + '</a></li>';
        });
        $("#stops" + listId).empty();
        $("#stops" + listId).append(list);
        $("#stops" + listId).listview('refresh');
    }

    var searchStopsByName = function(query) {
        var results;
        if (query.length == 0) { return [] }
        query = query.toLowerCase();
        results = busStops.filter(function(entry){
            return entry.name.toLowerCase().indexOf(query) !== -1;
        });
        return results;
    }

    var searchStopsByLocationId = function(query) {
        var results = $.grep(busStops, function(e) {
            return e.locationId === query;
        });
        return results[0];
    }

    var setDirection = function(stop) {
        var direction;
        if (stop.substring(4,5) in ["1", "0", "6", "7"]) {
            console.log("first switch");
        } else {
            console.log("second switch");
            console.log(stop.substring(4,6));
        }
        switch (stop.substring(4,5)) {
            case "1":
                direction = "-- til midtbyen";
                break;
            case "0":
                direction = "-- fra midtbyen";
                break;
            case "6":
            case "7":
                direction = "-- mot Klæbu";
                break;
            default:
                direction = "-- ukjent";
                console.log("-- ukjent");
        }

        switch (stop.substring(4,6)) {
            case "20":
                direction = "-- mot Stjørdal";
                break;
            case "83":
                direction = "-- mot Trondheim";
                break;
            case "40":
                direction = "-- vestover";
                break;
            case "87":
                direction = "-- østover";
                break;
            default:
                console.log("-- ukjent");
        }

        return direction;
   }
    
    return {
        setBusToStop:setBusToStop,
        searchStopsByName:searchStopsByName,   
        searchStopsByLocationId:searchStopsByLocationId,
        setDirection:setDirection,
        addStopsToList:addStopsToList
    }

})(jQuery);
