<!-- components/ReminderItem.vue -->
<template>
    <div id="item">
        <h3>{{ reminder.title }}</h3>
        <p>{{ reminder.body }}</p>
        <p>Created: {{ reminder.creation_date }} by {{ reminder.owner }}</p>
        <button @click="deleteReminder()">Delete</button>
        <div v-if="message" class="alert alert-danger" role="alert">
            {{ message }}
        </div>
    </div>
</template>
  
<script>
import ReminderService from '@/services/reminder.service';

export default {
    props: {
        reminder: Object,
    },
    setup() {
        return {
            ReminderService,
        };
    },
    data() {
        return {
            message: "",
        };
    },
    methods: {
        async deleteReminder() {
            ReminderService.getReminders().then(
                () => {
                    this.message = "";
                },
                (error) => {
                    console.log("here");
                    this.message =
                        (error.response &&
                            error.response.data &&
                            error.response.data.message) ||
                        error.message ||
                        error.toString();
                }
            );
            this.$router.go();
        }
    }
};
</script>
  
<style>
#item {
    border: 1px solid black;
    margin: 10px;
    padding: 10px;
}
</style>