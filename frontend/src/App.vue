<!-- src/App.vue -->
<template>
  <div id="app">
    <router-view v-if="AuthService.isAuthenticated()" />
    <router-view v-else />
  </div>
</template>

<script>
// import { ref } from 'vue';
import AuthService from './services/AuthService';

export default {
  setup() {
    return {
      AuthService,
    };
  },
};
</script>

<style>
/* Global styles for the entire page */
body {
  font-family: 'Arial', sans-serif;
  margin: 0;
  padding: 0;
}

#app {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f8f8f8;
}
</style>