function replaceNavbar() {
    var css = document.createElement("style");
    css.type = "text/css";
    css.innerHTML = ".container { width: 900px }";
    document.body.appendChild(css);
}
