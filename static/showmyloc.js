var map;

L.mapquest.key = 'RD5aTRwDtr4AfEJMzvobnwuSLqD8iAjY';

map = L.mapquest.map('map', {
    center: [51.0992, -114.0558],
    layers: L.mapquest.tileLayer('map'),
    zoom: 11
  });
  map.addControl(L.mapquest.control());
  //L.mapquest.geocodingControl().addTo(map);

function showMe(latitude, longitude) {
    latitude = geoLocStart.lat;
    longitude = geoLocStart.lon;
    if (map) {
        map.remove();
    }
    //map.remove()
    //console.log(start);
    //console.log(latitude+"/---/"+longitude);

    /*
    map = L.map('map').setView([latitude, longitude], 10);
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'pk.eyJ1IjoicmJhd2FoIiwiYSI6ImNremc1OGVjMjNuc3Uyc3R2NTl1Njl0bTMifQ.q2S3gk5XDYjS0R9sfxI4Sg'
    }).addTo(map);
    */

    map = L.mapquest.map('map', {
        center: [latitude, longitude],
        layers: L.mapquest.tileLayer('map'),
        zoom: 11
      });

    var tempIcon = new L.Icon({
        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
        });
        
    var marker = L.marker([latitude, longitude], {icon: tempIcon}).addTo(map);
    var popuptext = "<h3><b>Your Current Location: </b></h3>";
    //console.log("Current temperature: " +temperature);
    marker.bindPopup(popuptext).openPopup();

    map.addControl(L.mapquest.control());
}



var id, dest, geoLocStart;
var lat, lon, a, b;
var latitude, longitude;


function watchMe () {

    function success(position) {
    lat  = position.coords.latitude;
    lon = position.coords.longitude;
    geoLocStart = {lat, lon};
    showMe(lat, lon);
  
    document.getElementById('meLat').innerHTML = lat;
    document.getElementById('meLon').innerHTML = lon;
    
    console.log("lat: ", lat);
    console.log("lon: ", lon);
    /*

    /*
    console.log(lat+"---"+lon);
    
    console.log(start);
    a = start.lat;
    b = start.lon;
    console.log(a+"---"+b);
  */
  
    }
  
    function error(err) {
      console.warn('ERROR(' + err.code + '): ' + err.message);
      textMessage = 'Unable to retrieve your location';

    }
  
    if(!navigator.geolocation) {
      textMessage = 'Geolocation is not supported by your device';

    } else {
      textMessage = 'Locating…';
      navigator.geolocation.getCurrentPosition(success, error);
      //id = navigator.geolocation.watchPosition(success, error);
      
    }
  
    //console.log(textMessage);
    //showMe(latitude, longitude);
  }