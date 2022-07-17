import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import GunsList from '../views/GunsList'
import GunProfile from '@/components/GunProfile'
import Shooters from '@/components/Shooters'
import ShooterProfile from '@/components/ShooterProfile'
import Register from '@/components/Register'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/KumaArms/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/KumaArms/guns_list',
    name: 'GunsList',
    component: GunsList
  },
  {
    path: '/KumaArms/gun_profile',
    name: 'GunProfile',
    component: GunProfile
  },
  {
    path: '/KumaArms/shooters',
    name: 'Shooters',
    component: Shooters
  },
  {
    path: '/KumaArms/shooter_profile/:id',
    name: 'ShooterProfile',
    component: ShooterProfile
  },
]

const router = createRouter({
  history: createWebHistory(), // process.env.BASE_URL
  routes
})

export default router
