<template>
  <div class="alert">
    <h3>⚠ Heat Alerts</h3>

    <p>Electronic City</p>
    <span class="extreme">Extreme</span>

    <p>Whitefield</p>
    <span class="high">High</span>

    <p>Koramangala</p>
    <span class="moderate">Moderate</span>
  </div>
</template>

<style>
.alert {
  position: absolute;
    top: 620px;
    right: 20px;
    width: 250px;
  background: rgba(17,24,39,0.9);
  color: white;
  padding: 20px;
  border-radius: 15px;
  z-index: 1000;
}

.extreme {
  color: red;
}

.high {
  color: orange;
}

.moderate {
  color: yellow;
}
</style>