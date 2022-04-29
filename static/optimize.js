
//wpoints = [ 'Edmonton', 'Vancouver'];
L.mapquest.key = 'RD5aTRwDtr4AfEJMzvobnwuSLqD8iAjY';
var map = L.mapquest.map('map', {
  center: [51.0992, -114.0558],
  layers: L.mapquest.tileLayer('map'),
  zoom: 13
});

function optimizeRoute (start, end, waypoints) {
/*
    map = L.mapquest.map('map', {
      center: [51.0992, -114.0558],
      layers: L.mapquest.tileLayer('map'),
      zoom: 13
    });
*/
    L.mapquest.directions().route({
      start: start,
      end: end,
      waypoints: waypoints,
      optimizeWaypoints: true
    });
    
  }
  map.addControl(L.mapquest.control());


const wpoints = [];
function submitForm(event) {
  event.preventDefault();


  //map.remove();
start = document.getElementById("start").value;
end = document.getElementById("destination").value;

wp1 = document.getElementById("wp1").value;
wp2 = document.getElementById("wp2").value;
wp3 = document.getElementById("wp3").value;
wp4 = document.getElementById("wp4").value;

if (wp1 != "") {wpoints[0] = wp1;}
if (wp2 != "") {wpoints[1] = wp2;}
if (wp3 != "") {wpoints[2] = wp3;}
if (wp4 != "") {wpoints[3] = wp4;}

console.log(wpoints);

optimizeRoute(start, end, wpoints);


  //document.getElementById("form").reset();
}


const form = document.getElementById('form');


form.addEventListener('submit', submitForm);


/*
const api_url = 'http://www.mapquestapi.com/directions/v2/routematrix?key=RD5aTRwDtr4AfEJMzvobnwuSLqD8iAjYjson={"locations":["Denver,CO","Westminster,CO","Boulder,CO"],"options": {"allToAll": true}}';
//const api_url = 'http://www.mapquestapi.com/directions/v2/optimizedroute?key=RD5aTRwDtr4AfEJMzvobnwuSLqD8iAjY&json={"locations":["Denver,CO","Westminster,CO","Boulder,CO"]}'
async function getISS() {
  const response = await fetch(api_url);
  const data = await response.json();
	console.log(data);
}

getISS();
*/