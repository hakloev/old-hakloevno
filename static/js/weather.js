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
        var copyright = xml.getElementsByTagName("link")[0].getAttributeNode("text");
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

        document.getElementById("weather-location").innerHTML = '<i class="fa fa-sun-o"> Forecast for ' + place + '</i>';
        document.getElementById("weather-temperature").innerHTML = "&deg; " + temp;
        document.getElementById("weather-windspeed").innerHTML = "<strong>Wind:</strong> " + windspeed[0].value + " m/s &ndash; " + winddir[2].value;
        document.getElementById("weather-windstrength").innerHTML = "<strong>Strength:</strong> " + windspeed[1].value;
        document.getElementById("weather-rain").innerHTML = "<strong>Rain: </strong>" + rain + " mm";
        document.getElementById("weather-icon").src = "/static/images/weather/" + icon[0].value + ".png";
        document.getElementById("weather-copyright").innerHTML = '<small><a href="' + copyrightUrl.value + '">' + copyright.value + "</a></small>";
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
