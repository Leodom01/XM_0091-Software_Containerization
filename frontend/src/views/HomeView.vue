<!-- src/views/Home.vue -->
<template>
  <div>
    <h1>Home</h1>
    <router-link to="/login">Login</router-link>
    <router-link to="/register">Register</router-link>

    <!-- Add a condition to show the reminders only if the user is authenticated -->
    <div v-if="authenticated">
      <Reminders />
    </div>
  </div>
</template>

<script>
import Reminders from './RemindersView.vue';

export default {
  components: {
    Reminders,
  },
  computed: {
    authenticated() {
      // Implement a check to determine if the user is authenticated
      // You can use Vuex or another state management solution for this
      // For simplicity, you can use a local variable or local storage
      return localStorage.getItem('authToken') !== null;
    },
  },
};
</script>
