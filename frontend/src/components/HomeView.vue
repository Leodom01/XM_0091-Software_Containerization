<template>
    <!-- header: show not logged in: login, register, logged in: show logged out> -->
    <!-- body: show reminders if logged in, else show "USer not logged in"> -->
    <header>

        <div v-if="!loggedIn">
            <button @click="forwardToLogin">Login</button>
            <button @click="forwardToRegister">Register</button>
        </div>
        <div v-else>
            <button @click="logout">Logout</button>
        </div>
    </header>
    <main>
        <div v-if="loggedIn">
            <div>
                User: {{ this.$store.state.auth.user.email }}
            </div>
            <ReminderList />
        </div>
        <div v-else>
            <p>No user logged in.</p>
        </div>
    </main>
</template>

<script>
import ReminderList from "../components/ReminderList.vue";

export default {
    components: {
        ReminderList,
    },
    computed: {
        loggedIn() {
            return this.$store.state.auth.status.loggedIn;
        },
    },
    methods: {
        logout() {
            this.$store.dispatch("auth/logout");
        },
        forwardToLogin() {
            this.$router.push("/login");
        },
        forwardToRegister() {
            this.$router.push("/register");
        },
    },
};
</script>