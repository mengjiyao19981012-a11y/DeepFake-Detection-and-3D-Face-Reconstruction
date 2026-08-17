<template>
  <header class="nav-header" :class="{ scrolled: isScrolled }">
    <div class="nav-inner">
      <router-link to="/" class="nav-logo">
        Deepfake
      </router-link>

      <nav class="nav-links">
      </nav>

      <div class="nav-right">
        <span class="designed-by">Designed by</span>
        <a
          href="https://github.com/PunkNinja"
          target="_blank"
          rel="noopener noreferrer"
          class="author-link"
        >@PunkNinja</a>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const isScrolled = ref(false)

function onScroll() {
  isScrolled.value = window.scrollY > 80
}

onMounted(() => window.addEventListener('scroll', onScroll))
onUnmounted(() => window.removeEventListener('scroll', onScroll))
</script>

<style scoped>
.nav-header {
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  transition: background 0.4s ease, box-shadow 0.4s ease, border-color 0.4s ease;
  background: transparent;
  border-bottom: 1px solid transparent;
}
.nav-header.scrolled {
  background: rgba(5, 30, 20, 0.95);
  border-bottom: 1px solid rgba(94, 210, 156, 0.12);
  box-shadow: 0 0 18px rgba(94, 210, 156, 0.06);
}

.nav-inner {
  padding: 14px 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-logo {
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 20px;
  font-weight: 700;
  color: #fff;
  letter-spacing: 0.04em;
  user-select: none;
  text-decoration: none;
}
.logo-icon {
  flex-shrink: 0;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 4px;
}

.nav-link {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 12px;
  font-weight: 600;
  color: rgba(255,255,255,0.45);
  letter-spacing: 0.05em;
  text-transform: uppercase;
  padding: 6px 14px;
  border-radius: 8px;
  transition: color 0.25s, background 0.25s;
  text-decoration: none;
}
.nav-link:hover {
  color: #fff;
  background: rgba(94,210,156,0.06);
}
.nav-link-active {
  color: #5ed29c !important;
  background: rgba(94,210,156,0.08);
}

.nav-right {
  display: flex;
  align-items: center;
  gap: 6px;
}

.designed-by {
  font-size: 12px;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.5);
  letter-spacing: 0.04em;
}

.author-link {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.06em;
  color: rgba(255, 255, 255, 0.75);
  transition: color 0.25s;
  text-decoration: none;
}
.author-link:hover {
  color: #5ed29c;
}

@media (max-width: 768px) {
  .nav-links { display: none; }
}
</style>
