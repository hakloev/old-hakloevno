var busInfoUrl = "/bus";

var xmlReq = function(url, type, callback) {
    var xhr = new XMLHttpRequest();
    xhr.onload = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            console.log('Callback in xhr');
            callback(this.responseText);
        } else {
            console.log('Error with xhr');
        }
    }
    xhr.open(type, url, true);
    xhr.send();
}

function parseInfo(place) {
    var bergInfo = place.berg;
    var ilaInfo = place.ila;
    var stopList = [];
    for (var i = 0; i < bergInfo.next.length; i++) {
        if (bergInfo.next[i].l == "5") {
            stopList.push(bergInfo.next[i]);
        }
        if (stopList.length == 4) {
            break;
        }
    }
    printInfo(stopList, "busberglist");
    stopList = [];
    for (var i = 0; i < ilaInfo.next.length; i++) {
        if (ilaInfo.next[i].l == "5") {
            stopList.push(ilaInfo.next[i]);
        }
         if (stopList.length == 4) {
            break;
        }
    } 
    printInfo(stopList, "busilalist");
}

function printInfo(times, type) {
    for (var i = 0; i <times.length; i++) {
        console.log(times[i].t.substring(11,16) + ' til ' + times[i].d)
        var ul = document.getElementById(type);
        var li = document.createElement("li");
        li.appendChild(document.createTextNode(times[i].t.substring(11, 16) + ' (' + times[i].rt + ')' ));
        ul.appendChild(li);
    }
}

function getBusTimes() {
    xmlReq(busInfoUrl, 'GET', 
        function(responseText) {
            var stopTimes = JSON.parse(responseText);
            parseInfo(stopTimes);
        }
    );
}

$(document).ready(function () {
    getBusTimes();
});
