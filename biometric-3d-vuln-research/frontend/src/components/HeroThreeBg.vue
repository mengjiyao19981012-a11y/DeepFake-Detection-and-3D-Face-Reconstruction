<template>
  <canvas ref="canvas" class="hero-three-canvas"></canvas>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import * as THREE from 'three'

const canvas = ref(null)

let renderer, scene, camera
let particles, ringMesh
let animationId
let clock

onMounted(() => {
  init()
  animate()
})

onUnmounted(() => {
  if (animationId) cancelAnimationFrame(animationId)
  renderer?.dispose()
  scene?.clear()
})

function init() {
  const el = canvas.value
  const parent = el.parentElement
  const width = parent.clientWidth
  const height = parent.clientHeight

  // Renderer
  renderer = new THREE.WebGLRenderer({ canvas: el, alpha: true, antialias: true })
  renderer.setSize(width, height)
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))

  // Scene
  scene = new THREE.Scene()

  // Camera
  camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100)
  camera.position.z = 18

  clock = new THREE.Clock()

  // ── Particle field ──
  const particleCount = 600
  const positions = new Float32Array(particleCount * 3)
  const colors = new Float32Array(particleCount * 3)
  const sizes = new Float32Array(particleCount)

  const green = new THREE.Color('#5ed29c')
  const blue = new THREE.Color('#3b82f6')
  const white = new THREE.Color('#ffffff')

  for (let i = 0; i < particleCount; i++) {
    // Spherical distribution with some randomness
    const theta = Math.random() * Math.PI * 2
    const phi = Math.acos(2 * Math.random() - 1)
    const r = 5 + Math.random() * 7

    positions[i * 3] = r * Math.sin(phi) * Math.cos(theta)
    positions[i * 3 + 1] = r * Math.sin(phi) * Math.sin(theta)
    positions[i * 3 + 2] = r * Math.cos(phi)

    // Color gradient: green → blue → white
    const mix = Math.random()
    let color
    if (mix < 0.5) {
      color = green.clone().lerp(blue, mix * 2)
    } else {
      color = blue.clone().lerp(white, (mix - 0.5) * 2)
    }
    colors[i * 3] = color.r
    colors[i * 3 + 1] = color.g
    colors[i * 3 + 2] = color.b

    sizes[i] = 0.015 + Math.random() * 0.06
  }

  const particleGeo = new THREE.BufferGeometry()
  particleGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3))
  particleGeo.setAttribute('color', new THREE.BufferAttribute(colors, 3))
  particleGeo.setAttribute('size', new THREE.BufferAttribute(sizes, 1))

  const particleMat = new THREE.PointsMaterial({
    size: 0.08,
    vertexColors: true,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
    transparent: true,
    opacity: 0.7,
  })

  particles = new THREE.Points(particleGeo, particleMat)
  scene.add(particles)

  // ── Glowing ring / torus ──
  const ringGeo = new THREE.TorusGeometry(4.5, 0.03, 32, 120)
  const ringMat = new THREE.MeshBasicMaterial({
    color: '#5ed29c',
    transparent: true,
    opacity: 0.35,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
  })
  ringMesh = new THREE.Mesh(ringGeo, ringMat)
  ringMesh.rotation.x = Math.PI * 0.35
  ringMesh.rotation.y = Math.PI * 0.15
  scene.add(ringMesh)

  // ── Second ring, opposite tilt ──
  const ring2Geo = new THREE.TorusGeometry(4.2, 0.02, 32, 100)
  const ring2Mat = new THREE.MeshBasicMaterial({
    color: '#3b82f6',
    transparent: true,
    opacity: 0.25,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
  })
  const ring2 = new THREE.Mesh(ring2Geo, ring2Mat)
  ring2.rotation.x = -Math.PI * 0.3
  ring2.rotation.y = -Math.PI * 0.2
  ring2.name = 'ring2'
  scene.add(ring2)

  // ── Central subtle sphere ──
  const sphereGeo = new THREE.SphereGeometry(0.25, 32, 32)
  const sphereMat = new THREE.MeshBasicMaterial({
    color: '#5ed29c',
    transparent: true,
    opacity: 0.5,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
  })
  const sphere = new THREE.Mesh(sphereGeo, sphereMat)
  sphere.name = 'centerSphere'
  scene.add(sphere)

  // ── Wireframe icosahedron ──
  const icoGeo = new THREE.IcosahedronGeometry(3.8, 0)
  const icoMat = new THREE.MeshBasicMaterial({
    color: '#5ed29c',
    wireframe: true,
    transparent: true,
    opacity: 0.08,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
  })
  const ico = new THREE.Mesh(icoGeo, icoMat)
  ico.name = 'ico'
  scene.add(ico)

  // Resize handler
  window.addEventListener('resize', onResize)
}

function onResize() {
  const parent = canvas.value.parentElement
  const width = parent.clientWidth
  const height = parent.clientHeight
  renderer.setSize(width, height)
  camera.aspect = width / height
  camera.updateProjectionMatrix()
}

function animate() {
  animationId = requestAnimationFrame(animate)

  const t = clock.getElapsedTime()

  // Slow rotation of particles
  particles.rotation.y += 0.0006
  particles.rotation.x = Math.sin(t * 0.2) * 0.15

  // Ring rotation
  ringMesh.rotation.z += 0.003
  ringMesh.rotation.x = Math.PI * 0.35 + Math.sin(t * 0.4) * 0.12

  // Second ring
  const ring2 = scene.getObjectByName('ring2')
  if (ring2) {
    ring2.rotation.z -= 0.0025
    ring2.rotation.y += 0.002
  }

  // Icosahedron slow spin
  const ico = scene.getObjectByName('ico')
  if (ico) {
    ico.rotation.y += 0.0015
    ico.rotation.x += 0.0008
  }

  // Center sphere pulse
  const sphere = scene.getObjectByName('centerSphere')
  if (sphere) {
    const s = 1 + Math.sin(t * 2) * 0.4
    sphere.scale.setScalar(s)
  }

  renderer.render(scene, camera)
}
</script>

<style scoped>
.hero-three-canvas {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
}
</style>
