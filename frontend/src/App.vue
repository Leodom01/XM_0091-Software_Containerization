<!-- src/App.vue -->
<template>
  <h1 @click="redirectHome">Reminder App</h1>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  methods: {
    redirectHome() {
      this.$router.push("/");
    },
  }
};
</script>
