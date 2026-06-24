<template>
  <div class="sidebar">
    <h1>GeoPulse AI</h1>

    <input
      v-model="searchCity"
      placeholder="Search city..."
      class="search"
    />

    <h2>Layers</h2>

    <button
      :class="{ active: activeLayer === 'LST' }"
      @click="activeLayer = 'LST'"
    >
      LST
    </button>

    <button
      :class="{ active: activeLayer === 'NDVI' }"
      @click="activeLayer = 'NDVI'"
    >
      NDVI
    </button>

    <button
      :class="{ active: activeLayer === 'Heat Stress' }"
      @click="activeLayer = 'Heat Stress'"
    >
      Heat Stress
    </button>

    <h2>Time</h2>

    <p class="clock">
      {{ currentTime }}
    </p>

    <input
      type="range"
      min="6"
      max="18"
      v-model="selectedTime"
    />

    <p class="time">
      {{ selectedTime }} PM
    </p>

    <div class="status-card">
      <h3>System Status</h3>

      <div class="status-item">
        <span>GIS</span>
        <span class="online">Online</span>
      </div>

      <div class="status-item">
        <span>Layers</span>
        <span class="online">Ready</span>
      </div>

      <div class="status-item">
        <span>AI Model</span>
        <span class="pending">Pending</span>
      </div>

      <div class="status-item">
        <span>Satellite</span>
        <span class="pending">Loading</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const activeLayer = ref('LST')
const searchCity = ref('')
const selectedTime = ref(12)

const currentTime = new Date().toLocaleTimeString()
</script>

<style>
.sidebar {
  width: 280px;
  background: #111827;
  color: white;
  padding: 25px;
  z-index: 1000;
  overflow-y: auto;
}

h1 {
  margin-bottom: 25px;
  font-size: 40px;
}

h2 {
  margin-top: 30px;
  margin-bottom: 15px;
}

.search {
  width: 100%;
  padding: 12px;
  border: none;
  border-radius: 8px;
  margin-bottom: 20px;
  font-size: 14px;
}

button {
  width: 100%;
  margin-bottom: 10px;
  padding: 12px;
  border: none;
  border-radius: 8px;
  background: #1f2937;
  color: white;
  cursor: pointer;
  transition: 0.2s;
}

button:hover {
  background: #374151;
}

button.active {
  background: #2563eb;
}

input[type="range"] {
  width: 100%;
  margin-top: 10px;
}

.clock {
  color: #9ca3af;
  margin-bottom: 10px;
}

.time {
  margin-top: 10px;
}

.status-card {
  margin-top: 40px;
  padding: 18px;
  background: rgba(255,255,255,0.05);
  border-radius: 14px;
  border: 1px solid rgba(255,255,255,0.08);
}

.status-card h3 {
  margin-bottom: 15px;
  font-size: 16px;
}

.status-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 12px;
  font-size: 14px;
}

.online {
  color: #22c55e;
  font-weight: bold;
}

.pending {
  color: #f59e0b;
  font-weight: bold;
}
</style>