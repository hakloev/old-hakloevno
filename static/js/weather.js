var Weather = (function($) { 
   
    var parseXML =function (xml) {
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
            document.getElementById("weather-forecast").innerHTML = '<h3><i class="fa fa-exclamation-triangle"></i>&nbsp;<b>OBS-varsel:</b></h3><br><small>' + gislefoss + "<br><br>" + gislefoss2 + "</small>";
        } else {
            var gislefoss =  xml.getElementsByTagName("body")[0].childNodes[0].data;
            document.getElementById("weather-forecast").innerHTML = "<small>" + gislefoss + "</small>";
        }

        document.getElementById("weather-location").innerHTML = 'Forecast for ' + place + '&nbsp; <i class="fa fa-chevron-up"></i>';
        document.getElementById("weather-info").innerHTML = windspeed[0].value + " m/s<br>" + winddir[2].value + "<br>" + windspeed[1].value + "<br>";
        document.getElementById("weather-rain").innerHTML = rain;
        document.getElementById("weather-degrees").innerHTML = temp + "&deg;";
        document.getElementById("weather-icon-cube").src = "/static/images/weather/" + icon[0].value + ".png";
        document.getElementById("weather-update").innerHTML = '<small><a href="' + copyrightUrl.value + '">data from yr.no</a></small>';
    }
    
    return {
        init: function() {
            $.ajax({
                type: "GET",
                url: "/static/files/varsel.xml",
                dataType: "xml",
                success: function(data) {
                    parseXML(data);
                },
                error: function(xhr, options, error) {
                    console.log('Failed fetching weather data!');
                }
            }); 
        }
    }

})(jQuery);

$(document).ready(function () {
    Weather.init();
    var showing = false;
    $('.weather-toggle').on('click', function() {
        if (showing) {
            showing = !showing;
            $('#weather-location').find('i').attr('class', 'fa fa-chevron-up');
        } else {
            showing = !showing;
            $('#weather-location').find('i').attr('class', 'fa fa-chevron-down');
        }
        $('#weather-widget').slideToggle(350);
    });
});
