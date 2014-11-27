var Bus = ( function () {
    
    var busInfoUrl = "/bustimes/";
    var parsed = false;
    var runnedBefore = false;

    var resetInfo = function() {
            parsed = false;
            runnedBefore = false;
    }
    var xmlReq = function(url, type, callback) {
        var xhr = new XMLHttpRequest();
        xhr.onload = function () {
            if (xhr.readyState == 4 && xhr.status == 200) {
                //console.log('INFO: Callback in XMLHttpRequest');
                callback(this.responseText);
            } else {
                console.log('ERROR: XMLHttpRequest failed, nothing to display in DOM');
            }
        }
        xhr.open(type, url, true);
        xhr.send();
    }
    var parseInfo = function(place) {
        //console.log("INFO: parseInfo called");
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
        //console.log("INFO: printInfo called");
        var place = "bus-berg";
        if (parsed) {
            place = "bus-ila";
        }
        document.getElementById(place).innerHTML = "";
        var rows = document.getElementById(place);
        var row = "";
        for (var i = 0; i < list.length; i++) {
            row += "<strong>" + list[i].t.substring(11, 16) + "</strong><small> &ndash; " + calcTime(list[i].t, list[i].rt) + "</small><br>"
        } 
        rows.innerHTML = row;
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
        getBusInfo: function() {
            xmlReq(busInfoUrl, "GET", 
                function(responseText) {
                    if (runnedBefore) {
                        resetInfo();
                    } else {
                        document.getElementById("busloading").innerHTML = "route 5, to the city center";
                    }
                    var json = JSON.parse(responseText);
                    parseInfo(json.berg);
                    parsed = true;
                    parseInfo(json.ila);
                    runnedBefore = true; 
                }
            );
        }
           }  
})();

$(document).ready(function () {
    Bus.getBusInfo();
    setInterval( function() {
        Bus.getBusInfo();
    }, 30000);
});
