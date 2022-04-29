L.mapquest.key = 'RD5aTRwDtr4AfEJMzvobnwuSLqD8iAjY';
var start, end, lat, lng;
var checkBox = document.getElementById("myButton");

function getDirection (start, end) {
/*  if (map) {
    map.remove();
}*/


  map = L.mapquest.map('map', {
    center: [51.0992, -114.0558],
    layers: L.mapquest.tileLayer('map'),
    zoom: 11
  });


  L.mapquest.directions().route({
    start: start,
    end: end,
    options: {
      timeOverage: 25,
      maxRoutes: 3,
    }
  });

  map.addControl(L.mapquest.control());

  /*
  function directionsCallback(error, response) {
    map = L.mapquest.map('map', {
      center: [51.0992, -114.0558],
      layers: L.mapquest.tileLayer('map'),
      zoom: 11
    });
    console.log(response.route.locations[0].displayLatLng);
    console.log(response.route.locations[0].latLng);

    //var origin = {lat: 53, lng: -113}
    //console.log(response.route.locations[0].displayLatLng);
    //console.log(response.route.locations[0].latLng);

    var directionsLayer = L.mapquest.directionsLayer({
      directionsResponse: response
    }).addTo(map);
    return map;
  }
  */
}

//map.addControl(L.mapquest.control());


var id, dest, geoLocStart;
var lat, lon, startLat, startLon;
var latitude, longitude;


/*
function startMe () {

    function success(position) {
    lat  = position.coords.latitude;
    lon = position.coords.longitude;
    geoLocStart = {lat, lon};
    end = document.getElementById("destination").value;
  
    if (checkBox.checked == true) {
        getDirection(geoLocStart, end);   
    }
  
    }

    function error(err) {
      console.warn('ERROR(' + err.code + '): ' + err.message);
      textMessage = 'Unable to retrieve your location';
    }
  
    if(!navigator.geolocation) {
      textMessage = 'Geolocation is not supported by your device';
      //console.log(textMessage);
    } else {
      textMessage = 'Locating…';
      navigator.geolocation.getCurrentPosition(success, error);
      //id = navigator.geolocation.watchPosition(success, error); 
    }
  }
*/


    // function that runs when form submitted
function submitForm(event, start, end) {
  event.preventDefault();

  // delete current map layer
  map.remove();

  // getting form data
  //var checkBox = document.getElementById("myButton");
  end = document.getElementById("destination").value;

  if (checkBox.checked == true) {
    startLat = document.getElementById("meLat").value;
    startLon = document.getElementById("meLon").value;
    geoLocStart = {lat, lon};
    getDirection(geoLocStart, end); 
  } else {
      start = document.getElementById("origin").value;
      // run directions function
      getDirection(start, end);
  }
  // reset form
  //document.getElementById("form").reset();
}

// asign the form to form variable
const form = document.getElementById('form');

// call the submitForm() function when submitting the form
form.addEventListener('submit', submitForm);
