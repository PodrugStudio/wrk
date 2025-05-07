import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '../views/DashboardView.vue'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: DashboardView
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView
    },
    {
      path: '/homes',
      name: 'homes',
      component: () => import('../views/HomesView.vue')
    },
    {
      path: '/admin',
      name: 'admin',
      component: () => import('../views/AdminMain.vue')
    }
  ]
})

export default router
