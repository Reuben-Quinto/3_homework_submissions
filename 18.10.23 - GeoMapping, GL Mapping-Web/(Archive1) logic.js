//instantiate leaflet map; its just blank
var map = L.map('mapContainer',{
    center: [34.0522, -118.2437],
    zoom: 3,
    minZoom: 2,
    maxZoom: 18
});

// 
var layer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'})
.addTo(map);

// L.marker([34.0522, -118.2437])
// .addTo(map)
// // Will have a pop up marker
// .bindPopup('Hess\' Triangle - A tiny peice of land leftover after 7th ave ext in 1913.')
// // Will be opened by default
// // .openPopup();


// Notes: https://leafletjs.com/reference-1.3.4.html#geojson
L.geoJson(earthquakes, {
     
})
.addTo(map)