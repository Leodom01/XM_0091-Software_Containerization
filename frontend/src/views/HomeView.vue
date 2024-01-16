<template>
  <div>
    <header>
      <h1>Reminders</h1>
    </header>

    <div>
      <AuthForm :authService="authService" />
    </div>

    <main>
      <div v-if="!authService.isAuthenticated()">
        <p>No user logged in.</p>
      </div>
      <div v-else>
        <RemindersList />
      </div>
    </main>


  </div>
</template>

<script>
import AuthService from '@/services/AuthService';
import RemindersList from '@/components/RemindersList.vue';
import AuthForm from '@/components/AuthForm.vue';


export default {
  setup() {
    return {
      AuthService,
    };
  },
  computed: {
    authService() {
      return AuthService;
    },
  },
  components: {
    RemindersList,
    AuthForm,
  },
};
</script>
