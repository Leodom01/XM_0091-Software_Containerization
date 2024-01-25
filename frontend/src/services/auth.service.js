import axios from 'axios';

let API_URI = process.env.VUE_APP_API_URI;
if (!API_URI) {
    API_URI = process.env.VUE_APP_API_URL_DEFAULT;
}
const API_URL = 'http://' + process.env.API_URI;

const REGISTER = '/register';
const LOGIN = '/login';

class AuthService {
    login(user) {
        return axios
            .post(API_URL + REGISTER, {
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
        return axios.post(API_URL + LOGIN, {
            username: user.username,
            email: user.email,
            password: user.password
        });
    }
}

export default new AuthService();