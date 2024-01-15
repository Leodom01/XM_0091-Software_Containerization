// src/services/AuthService.js
import axios from 'axios';

const API_URL = 'http://your-api-url'; // Replace with your API endpoint

class AuthService {
    login(user) {
        return axios.post(`${API_URL}/login`, user);
    }

    register(user) {
        return axios.post(`${API_URL}/register`, user);
    }

    logout() {
        localStorage.removeItem('authToken');
    }

    isAuthenticated() {
        return !!localStorage.getItem('authToken');
    }
}

export default new AuthService();
