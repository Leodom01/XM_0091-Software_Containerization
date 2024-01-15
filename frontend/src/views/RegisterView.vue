<template>
    <div>
        <h2>Register</h2>
        <form @submit.prevent="register">
            <label>Name:</label>
            <input v-model="name" type="text" required />

            <label>Email:</label>
            <input v-model="email" type="email" required />

            <label>Password:</label>
            <input v-model="password" type="password" required />

            <button type="submit">Register</button>
        </form>
    </div>
</template>
  
<script>
import AuthService from '../services/AuthService';
import { ref } from 'vue';

export default {
    setup() {
        const name = ref('');
        const email = ref('');
        const password = ref('');

        const register = async () => {
            try {
                const response = await AuthService.register({
                    name: name.value,
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
                console.error('Registration error:', error);
            }
        };

        return {
            name,
            email,
            password,
            register,
        };
    },
};
</script>
  