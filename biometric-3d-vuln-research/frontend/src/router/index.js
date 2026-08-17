import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../pages/Home.vue'),
  },
  {
    path: '/detect',
    name: 'SingleDetect',
    component: () => import('../pages/SingleDetect.vue'),
  },
  {
    path: '/batch',
    name: 'BatchAnalyze',
    component: () => import('../pages/BatchAnalyze.vue'),
  },
  {
    path: '/samples',
    name: 'SampleLib',
    component: () => import('../pages/SampleLib.vue'),
  },
  {
    path: '/verify',
    name: 'VulnVerify',
    component: () => import('../pages/VulnVerify.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
