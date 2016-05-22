var x = document.getElementById("demo");

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);

    } else { 
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    x.innerHTML = "Latitude: " + position.coords.latitude + 
    "<br>Longitude: " + position.coords.longitude;

    sendData(position)

}

function sendData(position){

	 $.ajax({
	  type: "POST",
	  url: '/sendData',
	  data: position.coords,
	  success: function(){
	  	console.log("sent successfully!")
	  },
	});
}