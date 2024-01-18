<!-- components/AuthForm.vue -->
<template>
    <div v-if="!isAuthenticated">
        <form @submit.prevent="submitForm">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" />
            <label for="password">Password</label>
            <input type="password" id="password" name="password" />
            <button type="submit">Register</button>
            <button type="submit">Login</button>
        </form>
        <div id="error">
            <p>Error</p>
        </div>
    </div>

    <div v-else>
        <button @click="logout()">Logout</button>
    </div>
</template>
  
<script>
export default {
    props: {
        authService: {
            type: Object,
            required: true,
        },
    },
    methods: {
        // register with user data
        register(email, password) {
            let response = this.authService.register(email, password);
            console.log(response);
        },
        login(email, password) {
            let response = this.authService.login(email, password);
            console.log(response);
        },
        logout() {
            this.authService.logout();
        },
    },
    computed: {
        isAuthenticated() {
            return this.authService.isAuthenticated();
        },
    },
};
</script>
  