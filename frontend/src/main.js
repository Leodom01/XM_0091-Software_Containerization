import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
// import dotenv from 'dotenv'

// dotenv.config()

createApp(App).use(router).use(store).mount('#app')
