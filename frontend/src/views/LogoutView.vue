<template>
    <div>
        <h2>Logout</h2>
        <button @click="logout">Logout</button>
    </div>
</template>
  
<script>
import AuthService from '../services/AuthService';

export default {
    methods: {
        logout() {
            AuthService.logout();

            // Redirect to the login page or update the state to reflect the logged-out status
            // For simplicity, let's redirect to the login page
            this.$router.push('/login');
        },
    },
};
</script>
  