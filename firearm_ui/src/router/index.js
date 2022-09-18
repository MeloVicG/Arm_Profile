import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import GunsList from '../views/GunsList'
import GunProfile from '@/components/GunProfile'
import Shooters from '@/components/Shooters'
import ShooterProfile from '@/components/ShooterProfile'
import Register from '@/components/Register'
import NotFound from '@/components/NotFound'

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
    path: '/KumaArms/shooter_profile/:_id',
    name: 'ShooterProfile',
    component: ShooterProfile,
    props: true
    // params: {id: shooter.id}
  },
// catch all 404
  { //this is kind of a regex form
    path: '/:catch_error_paths(.*)',
    name: 'NotFound',
    component: NotFound
  }

]

const router = createRouter({  // what does this do??
  history: createWebHistory(process.env.BASE_URL  ), // process.env.BASE_URL
  routes
})

export default router
