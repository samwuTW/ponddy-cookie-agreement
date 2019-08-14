function cookieAgreedAJAXSent() {
    document.getElementById("cookie-policy-bar").style.display = 'none';
}

function cookieAgreedAJAXSubmit(url) {
    var req = new XMLHttpRequest();

    req.addEventListener("load", cookieAgreedAJAXSent);
    req.open("GET", url);
    req.send();
}
