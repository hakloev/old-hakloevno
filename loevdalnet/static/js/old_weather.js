
var weather = function () { 
    
    var url = "/static/files/varsel.xml";

    return {    
        loadXML: function () {
                var xmlhttp;
                
                if (window.XMLHttpRequest) {
                    xmlhttp = new XMLHttpRequest();
                }

                xmlhttp.onreadystatechange = function () {
                    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                        var doc = xmlhttp.responseXML;
                    }
                }
                
                xmlhttp.open("GET", url, true);
                xmlhttp.send();
        },
        init: function () {
            console.log('init');
        }
        
    }
};

window.onload = function () {
    weather.init();
};
