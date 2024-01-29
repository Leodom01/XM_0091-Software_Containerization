import axios from 'axios';

let API_URI = process.env.VUE_APP_API_URI;
if (!API_URI) {
    API_URI = "app-svc.default.svc.cluster.local.:8081"
}
const API_URL = '//' + API_URI;

const REGISTER = '/register';
const LOGIN = '/login';

class AuthService {
    login(user) {

        return axios
            .post(API_URL + LOGIN, {
                username: user.username,
                password: user.password
            })
            .then(response => {
                if (response.data.accessToken) {
                    localStorage.setItem('user', JSON.stringify(response.data));
                }

                return response.data;
            });

    }

    logout() {
        localStorage.removeItem('user');
    }

    register(user) {
        return axios.post(API_URL + REGISTER, {
            username: user.username,
            password: user.password
        });
    }
}

export default new AuthService();