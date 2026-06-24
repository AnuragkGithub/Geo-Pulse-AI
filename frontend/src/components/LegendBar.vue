<template>
  <div class="legend">
    <span>20°</span>
    <div class="gradient"></div>
    <span>50°</span>
  </div>
</template>

<style>
.legend {
  position: absolute;
  bottom: 30px;
  left: 350px;
  width: 400px;
  background: rgba(255,255,255,0.95);
  padding: 12px;
  border-radius: 10px;
  z-index: 1000;
}

.gradient {
  height: 20px;
  border-radius: 10px;
  background: linear-gradient(
    to right,
    blue,
    cyan,
    green,
    yellow,
    orange,
    red
  );
}
</style>