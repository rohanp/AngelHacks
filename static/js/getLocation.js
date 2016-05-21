var x = document.getElementById("demo");


function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.watchPosition(showPosition, handleLocationError, {timeout: 1000});

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

function handleLocationError(error) {
  switch(error.code){
  case 0:
    updateStatus("There was an error while retrieving your location: " +
                                 error.message);
  break;
  case 1:
  updateStatus("The user prevented this page from retrieving a location.");
  break;
  case 2:
  updateStatus("The browser was unable to determine your location: " +
                               error.message);
  break;
  case 3:
  updateStatus("The browser timed out before retrieving the location.");
  break;
  }
}
