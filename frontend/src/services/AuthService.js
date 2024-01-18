// src/services/AuthService.js
import axios from 'axios';
import { reactive } from 'vue';

const API_URL = process.env.API_URL

class AuthService {
    data = reactive({
        authenticated: true,
    });

    login(user) {
        return axios.post(`${API_URL}/login`, user);
    }

    register(user) {
        return axios.post(`${API_URL}/register`, user);
    }

    logout() {
        // localStorage.removeItem('authToken');
        console.log(this.authenticated)
    }

    isAuthenticated() {
        return this.data.authenticated;
        // return !!localStorage.getItem('authToken');
    }
}

export default new AuthService();
