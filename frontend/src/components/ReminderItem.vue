<!-- components/ReminderItem.vue -->
<template>
    <div id="item">
        <h3>{{ reminder.title }}</h3>
        <p>{{ reminder.body }}</p>
        <p>Created: {{ reminder.creation_date }} by {{ reminder.owner }}</p>
        <p v-if="AuthService.isAdmin">Owner: {{ reminder.owner }}</p>
        <button @click="deleteReminder()">Delete</button>
    </div>
</template>
  
<script>
import AuthService from '@/services/AuthService';
import ReminderService from '@/services/ReminderService';

export default {
    props: {
        reminder: Object,
    },
    setup() {
        return {
            AuthService,
            ReminderService,
        };
    },
    computed: {
        authService() {
            return AuthService;
        },
    },
    methods: {
        async deleteReminder() {
            await ReminderService.deleteReminder(this.reminder.id);
        },
    },
};
</script>
  
<style>
#item {
    border: 1px solid black;
    margin: 10px;
    padding: 10px;
}
</style>