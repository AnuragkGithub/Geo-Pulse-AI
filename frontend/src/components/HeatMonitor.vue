<template>
  <div class="monitor">
    <h3>🔥 Heat Monitor</h3>

    <div class="metric">
      <span>Maximum</span>
      <strong>42°C</strong>
    </div>

    <div class="metric">
      <span>Average</span>
      <strong>36°C</strong>
    </div>

    <div class="metric">
      <span>Risk</span>
      <strong class="high">HIGH</strong>
    </div>

    <div class="pulse"></div>

    <p class="live">
      LIVE MONITORING
    </p>
  </div>
</template>

<style>
.monitor {
   position: absolute;
    top: 350px;
    right: 20px;
    width: 250px;
  background: rgba(17,24,39,0.9);
  color: white;
  padding: 20px;
  border-radius: 15px;
  z-index: 1000;
}

.metric {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

.high {
  color: orange;
}

.live {
  color: #22c55e;
  margin-top: 15px;
}

.pulse {
  width: 12px;
  height: 12px;
  background: red;
  border-radius: 50%;
  margin-top: 15px;
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0% {
    transform: scale(1);
    opacity: 1;
  }

  100% {
    transform: scale(2);
    opacity: 0;
  }
}
</style>