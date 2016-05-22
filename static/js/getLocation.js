var watchID;
var geoLoc;
var x = document.getElementById("demo");


function showLocation(position) {
  var latitude = position.coords.latitude;
  var longitude = position.coords.longitude;
  x.innerHTML = "Latitude : " + latitude + " Longitude: " + longitude;
}

function requestFood(email){

    getLocation(function(position){

      $.ajax({
        type: "POST",
        url: '/requestFood',
        data: {'email': email,
               'longitude': position.coords.longitude,
               'latitude': position.coords.latitude
             },
        success: function(){
          console.log("requested food successfully!")
        },
      });

    })  
}

function updateLocation(email){

  getLocation(function(position){

      console.log(position.coords)

      $.ajax({
        type: "POST",
        url: '/updateLocation',
        data: {'email': email,
               'longitude': position.coords.longitude,
               'latitude': position.coords.latitude
             },
        success: function(){
          console.log("sent location successfully!")
        },
      });

    }) 
}

function errorHandler(err) {
  if (err.code == 1) {
    alert("Error: Access is denied!");
  } else if (err.code == 2) {
    alert("Error: Position is unavailable!");
  }
}

function getLocation(callback) {
  if (navigator.geolocation) {
    var options = {}
    geoLoc = navigator.geolocation;
    watchID = geoLoc.watchPosition(callback, errorHandler, options);
  } else {
    alert("Sorry, browser does not support geolocation!");
  }
}
