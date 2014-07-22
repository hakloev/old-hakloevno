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
        var place = xml.getElementsByTagName("location")[0].childNodes[1].childNodes[0].nodeValue; 
        var gislefoss = xml.getElementsByTagName("body")[0].childNodes[0].data;
        var temp = xml.getElementsByTagName("temperature")[0].attributes[1].value;
        var rain = xml.getElementsByTagName("precipitation")[0].attributes[0].value;
        var windspeed = xml.getElementsByTagName('windSpeed')[0].attributes;
        var winddir = xml.getElementsByTagName("windDirection")[0].attributes;
        var icon = xml.getElementsByTagName("symbol")[0].attributes;
        document.getElementById("weatherlocation").innerHTML = " på " + place;
        document.getElementById("temp").innerHTML = "&deg; " + temp;
        document.getElementById("windspeed").innerHTML = "<strong>Vind:</strong> " + windspeed[0].value + " m/s &ndash; " + winddir[2].value;
        document.getElementById("windstrength").innerHTML = "<strong>Styrke:</strong> " + windspeed[1].value;
        document.getElementById("rain").innerHTML = "<strong>Nedbør: </strong>" + rain + " mm";
        document.getElementById("forecast").innerHTML = "<p>" + gislefoss + "</p>";
        document.getElementById("weathericon").src = "http://symbol.yr.no/grafikk/sym/b100/0" + icon[0].value + "d.png";
    }
};

$(document).ready(function () {
    $('.weatherwidget').hide();
    $('#weatherbutton').on('click', function() {
        $('.weatherwidget').slideToggle(350);
    });
    weather.loadXML();
});
