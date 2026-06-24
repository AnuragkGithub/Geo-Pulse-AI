<template>
  <div class="map-container">
    <div id="map"></div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'

onMounted(() => {
  // Bengaluru center
  const map = L.map('map').setView([12.9716, 77.5946], 12)

  // OpenStreetMap
  L.tileLayer(
    'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    {
      attribution: '© OpenStreetMap'
    }
  ).addTo(map)

  // Bengaluru marker
  L.circle([12.9716, 77.5946], {
    radius: 3500,
    color: '#ef4444',
    fillColor: '#ef4444',
    fillOpacity: 0.35
  }).addTo(map)

  // Koramangala
  L.circle([12.9352, 77.6245], {
    radius: 2500,
    color: '#f97316',
    fillColor: '#f97316',
    fillOpacity: 0.30
  }).addTo(map)

  // Whitefield
  L.circle([12.9698, 77.7500], {
    radius: 2500,
    color: '#eab308',
    fillColor: '#eab308',
    fillOpacity: 0.30
  }).addTo(map)

  // Electronic City
  L.circle([12.8456, 77.6603], {
    radius: 3000,
    color: '#dc2626',
    fillColor: '#dc2626',
    fillOpacity: 0.35
  }).addTo(map)

  // Bengaluru marker
  L.marker([12.9716, 77.5946])
    .addTo(map)
    .bindPopup(
      '<b>Bengaluru</b><br>Heat Stress: High<br>Temperature: 38°C'
    )

  setTimeout(() => {
    map.invalidateSize()
  }, 100)
})
</script>

<style>
.map-container {
  flex: 1;
}

#map {
  width: 100%;
  height: 100vh;
}
</style>