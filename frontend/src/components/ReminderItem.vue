<!-- components/ReminderItem.vue -->
<template>
    <div id="item">
        <h3>{{ reminder.title }}</h3>
        <p>{{ reminder.body }}</p>
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