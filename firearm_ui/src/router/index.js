import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Guns_List from '../views/Guns_List.vue'
import Gun_Profile from '../components/Gun_Profile'
import Shooters from '../components/Shooters'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/guns_list',
    name: 'Guns_List',
    component: Guns_List
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    
    // <<< WHAT IS THIS >>>
    // component: () => import(/* webpackChunkName: "about" */ '../views/Guns_List.vue')
  },
  {
    path: '/gun_profile',
    name: 'Gun_Profile',
    component: Gun_Profile
  },
  {
    path: '/Shooters',
    name: 'Shooters',
    component: Shooters
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
