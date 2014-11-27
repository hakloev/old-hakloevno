var url = "/static/files/varsel.xml";

var weather = { 
    loadXML: function () {
        var xmlhttp;
        if (window.XMLHttpRequest) {
            xmlhttp = new XMLHttpRequest();
        }
        xmlhttp.onreadystatechange = function () {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                data = xmlhttp.responseXML;
                weather.parseXML(data);
            }    
        }
        xmlhttp.open("GET", url, true);
        xmlhttp.send();
    },
    parseXML: function (xml) {
        var place = xml.getElementsByTagName("name")[0].childNodes[0].nodeValue; 
        var temp = xml.getElementsByTagName("temperature")[0].getAttribute('value');
        var rain = xml.getElementsByTagName("precipitation")[0].getAttribute('value');
        var windspeed = xml.getElementsByTagName('windSpeed')[0].attributes;
        var winddir = xml.getElementsByTagName("windDirection")[0].attributes;
        var icon = xml.getElementsByTagName("symbol")[0].attributes;
        var copyrightUrl = xml.getElementsByTagName("link")[0].getAttributeNode("url");

        var forecasttype = xml.getElementsByTagName("time")[0].getAttribute('type');
        if (forecasttype === "obsforecast") {
            console.log("obsforecast");
            var gislefoss = xml.getElementsByTagName("body")[0].childNodes[0].data;
            var gislefoss2 = xml.getElementsByTagName("body")[1].childNodes[0].data;
            document.getElementById("weather-forecast").innerHTML = '<h4 class="obsforecast"><i class="fa fa-exclamation-triangle"></i>&nbsp;<b>OBS-varsel:</b></h4>' + "<p>" + gislefoss + "</p><br>" + "<p>" + gislefoss2 + "</p>";
        } else {
            var gislefoss =  xml.getElementsByTagName("body")[0].childNodes[0].data;
            document.getElementById("weather-forecast").innerHTML = "<p>" + gislefoss + "</p>";
        }

        document.getElementById("weather-location").innerHTML = 'Forecast for ' + place;

        document.getElementById("weather-info").innerHTML = windspeed[0].value + " m/s<br>" + winddir[2].value + "<br>" + windspeed[1].value + "<br>";
        document.getElementById("weather-rain").innerHTML = rain;
        document.getElementById("weather-degrees").innerHTML = temp + "&deg;";
        document.getElementById("weather-icon-cube").src = "/static/images/weather/" + icon[0].value + ".png";
        document.getElementById("weather-update").innerHTML = '<small><a href="' + copyrightUrl.value + '">data from yr.no</a></small>';
    }
};

$(document).ready(function () {
    //$('#weatherpanel').hide();
    $('#weatherbutton').on('click', function() {
        $('#weatherpanel').slideToggle(350);
        //$('.weatherwidget').slideToggle(350);
    });
    weather.loadXML();
});
