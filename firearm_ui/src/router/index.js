import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import GunsList from '../views/GunsList'
import GunProfile from '@/components/GunProfile'
import Shooters from '@/components/Shooters'
import Register from '@/components/Register'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/guns_list',
    name: 'GunsList',
    component: GunsList
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    
    // <<< WHAT IS THIS >>>
    // component: () => import(/* webpackChunkName: "about" */ '../views/Guns_List.vue')
  },
  {
    path: '/gun_profile',
    name: 'GunProfile',
    component: GunProfile
  },
  {
    path: '/shooters',
    name: 'Shooters',
    component: Shooters
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
