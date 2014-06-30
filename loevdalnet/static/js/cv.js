function loadPage(href) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", href, false);
    xmlhttp.send();
    return xmlhttp.responseText;
}

function replacePage() {
    document.querySelector('.active').className = "";
    document.querySelector('#cv').className = "active";
    var stateObject = {};
    var title = "CV";
    var newUrl = "/cv/";
    history.pushState(stateObject, title, newUrl);
    document.querySelector('.maincontainer').innerHTML = loadPage('/static/public/cv.html');
}
