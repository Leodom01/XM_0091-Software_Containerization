<!-- src/views/Login.vue -->
<template>
    <div>
        <h2>Login</h2>
        <form @submit.prevent="login">
            <label>Email:</label>
            <input v-model="email" type="email" required />

            <label>Password:</label>
            <input v-model="password" type="password" required />

            <button type="submit">Login</button>
        </form>
    </div>
</template>
  
<script>
import AuthService from '../services/AuthService';
import { ref } from 'vue';

export default {
    setup() {
        const email = ref('');
        const password = ref('');

        const login = async () => {
            try {
                const response = await AuthService.login({
                    email: email.value,
                    password: password.value,
                });
                const authToken = response.data.token;

                // Store the authentication token
                localStorage.setItem('authToken', authToken);

                // Redirect to the home page or update the state to reflect the logged-in status
                // For simplicity, let's redirect to the home page
                this.$router.push('/');
            } catch (error) {
                console.error('Login error:', error);
            }
        };

        return {
            email,
            password,
            login,
        };
    },
};
</script>
  