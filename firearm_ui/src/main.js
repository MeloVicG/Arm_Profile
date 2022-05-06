import '@babel/polyfill'
import 'mutationobserver-shim'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
// import './plugins/bootstrap-vue'

// import 'bootstrap/dist/js/bootstrap.min.js'
// import { BootstrapVue } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css';
// import 'bootstrap-vue/dist/bootstrap-vue.css'
{/* <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script> */}

// Optionally install the BootstrapVue icon components plugin


// App.use(BootstrapVue)
// App.use(IconsPlugin)


createApp(App).use(router).mount('#app')