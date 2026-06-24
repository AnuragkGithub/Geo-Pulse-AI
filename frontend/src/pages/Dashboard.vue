<template>
  <div class="dashboard">
    <Sidebar />
    <MapView />
    <InfoCard />
    <HeatMonitor />
    <HeatAlert />
  </div>
</template>

<script setup>
import Sidebar from '../components/Sidebar.vue'
import MapView from '../components/MapView.vue'
import InfoCard from '../components/InfoCard.vue'
import HeatMonitor from '../components/HeatMonitor.vue'
import HeatAlert from '../components/HeatAlert.vue'
</script>

<style>
.dashboard {
  display: flex;
  height: 100vh;
  width: 100vw;
}
</style>