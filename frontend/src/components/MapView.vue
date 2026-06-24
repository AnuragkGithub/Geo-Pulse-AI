<template>
  <div class="map-container">
    <div id="map"></div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'
import 'leaflet.heat'

onMounted(() => {
  // Bengaluru center
  const map = L.map('map').setView([12.9716, 77.5946], 12)

  // OpenStreetMap layer
  L.tileLayer(
    'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    {
      attribution: '© OpenStreetMap'
    }
  ).addTo(map)

  // Bengaluru marker
  L.marker([12.9716, 77.5946])
    .addTo(map)
    .bindPopup('<b>Bengaluru</b><br>Temperature: 38°C')

  // Heat points
  const heatPoints = [
    [12.9716, 77.5946, 0.8], // Central Bengaluru
    [12.9352, 77.6245, 0.9], // Koramangala
    [12.8456, 77.6603, 1.0], // Electronic City
    [12.9698, 77.7500, 0.85], // Whitefield
    [13.0827, 77.5877, 0.75], // Hebbal
    [12.9141, 77.6100, 0.7], // Jayanagar
    [12.9279, 77.6271, 0.9], // BTM Layout
  ]

  // Heat layer
 const heat = L.heatLayer(heatPoints, {
  radius: 40,
  blur: 30,
  maxZoom: 15
})

heat.addTo(map)

  // Fix rendering issue
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