var Bus = ( function () {
    
    var busInfoUrl = "/bus/";
    var parsed = false;
    var runnedBefore = false;

    return {
        getBusInfo: function() {
            var self = this; // Needed to access parseInfo in callback function
            this.xmlReq(busInfoUrl, "GET", 
                function(responseText) {
                    if (runnedBefore) {
                        self.resetInfo();
                    } else {
                        document.getElementById("busloading").innerHTML = "";
                        document.getElementById("bergname").innerHTML = "Østre Berg:";
                        document.getElementById("ilaname").innerHTML = "Ila:";
                    }
                    var json = JSON.parse(responseText);
                    self.parseInfo(json.berg);
                    parsed = true;
                    self.parseInfo(json.ila);
                    runnedBefore = true; 
                }
            );
        },
        resetInfo: function() {
            parsed = false;
            runnedBefore = false;
        },
        xmlReq:  function(url, type, callback) {
            var xhr = new XMLHttpRequest();
            xhr.onload = function () {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    console.log('INFO: Callback in XMLHttpRequest');
                    callback(this.responseText);
                } else {
                    console.log('ERROR: XMLHttpRequest failed, nothing to display in DOM');
                }
            }
            xhr.open(type, url, true);
            xhr.send();
        }, 
        parseInfo: function(place) {
            console.log("INFO: parseInfo called");
            var departureList = [];
            for (var i = 0; i < place.next.length; i++) {
                if (place.next[i].l == "5") {
                    departureList.push(place.next[i]);
                }
                if (departureList.length == 3) {
                    break;
                }
            }
            this.printInfo(departureList);
        }, 
        printInfo: function(list) {
            console.log("INFO: printInfo called");
            var place = "busberglist";
            if (parsed) {
                place = "busilalist";
            }
            document.getElementById(place).innerHTML = "";
            var rows = document.getElementById(place);
            var row = "";
            for (var i = 0; i < list.length; i++) {
                console.log(list[i]);
                row += "<li><p><b>" + list[i].t.substring(11, 16) + "</b><small> &ndash; " + this.calcTime(list[i].t) + "</small></p></li>"
            } 
            rows.innerHTML = row;
        },
        calcTime: function(time) {
            console.log("INFO: calcTime called");
            var d = time.match(/^(\d{2}).(\d{2}).(\d{4}) (\d{2}):(\d{2})$/);
            var today = new Date();
            var departure = new Date(d[3], d[2] - 1, d[1], d[4], d[5]);
            var diff = Math.floor((departure.getTime() - today.getTime()) / (1000 * 60));
            if (diff <= -1 || diff <= 0) {
                return '<b style="color:red">ca nå</b>';
            } else {
                return "ca " + diff + " min";
            }   
        }
    }  
}());

$(document).ready(function () {
    Bus.getBusInfo();
    setInterval( function() {
        Bus.getBusInfo();
    }, 30000);
});
