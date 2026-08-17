<template>
  <div class="app-root">
    <!-- Top decorative strip — in normal flow, above header -->
    <div class="top-strip-wrapper">
      <img src="/assets/top.png" alt="Top decorative strip" class="top-strip-img" />
    </div>

    <NavHeader />
    <router-view />
  </div>
</template>

<script setup>
import NavHeader from './components/NavHeader.vue'
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
}

.top-strip-wrapper {
  width: 100%;
  position: relative;
  z-index: 10;
}
.top-strip-img {
  width: 100%;
  height: auto;
  display: block;
}
</style>

<style scoped>
.app-root {
  min-height: 100vh;
  background: #070b0a;
  color: #fff;
  font-family: 'Inter', sans-serif;
}
</style>
