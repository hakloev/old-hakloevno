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
        document.getElementById("weatherlocation").innerHTML = "Været for " + place;
        document.getElementById("temp").innerHTML = "<strong>&deg; " + temp + "</strong>";
        document.getElementById("forecast").innerHTML = "<p>" + gislefoss + "</p>";
    }
};

window.onload = function () {
    weather.loadXML();
};
