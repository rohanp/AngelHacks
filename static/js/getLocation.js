var x = document.getElementById("demo");


function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
        setTimeout(getLocation(), 1000);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    var xcoord = [];
    var ycoord = [];

    xcoord.push(position.coords.latitude);
    ycoord.push(position.coords.longitude);

    x.innerHTML = "Latitude: " + xcoord +
    "<br>Longitude: " + ycoord;
}
