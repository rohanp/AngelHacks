var watchID;
var geoLoc;
var x = document.getElementById("demo");

function showLocation(position) {
  var latitude = position.coords.latitude;
  var longitude = position.coords.longitude;
  x.innerHTML = "Latitude : " + latitude + " Longitude: " + longitude;
}

function errorHandler(err) {
  if (err.code == 1) {
    alert("Error: Access is denied!");
  } else if (err.code == 2) {
    alert("Error: Position is unavailable!");
  }
}

function getLocation() {
  if (navigator.geolocation) {
    // timeout at 60000 milliseconds (60 seconds)
    var options = {
      timeout: 60000
    };
    geoLoc = navigator.geolocation;
    watchID = geoLoc.watchPosition(showLocation, errorHandler, options);
  } else {
    alert("Sorry, browser does not support geolocation!");
  }
}
