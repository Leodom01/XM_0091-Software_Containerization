<!-- components/RemindersList.vue -->
<template>
    <div>
        <div v-if="reminders.length === 0">
            <p>No reminders yet.</p>
        </div>
        <ReminderItem v-else v-for="reminder in reminders" :key="reminder.id" :reminder="reminder" />
    </div>
</template>
  
<script>
// auth service needed?
import ReminderService from '@/services/ReminderService';
import ReminderItem from './ReminderItem.vue'; // Create ReminderItem.vue

export default {
    data() {
        return {
            reminders: [
                {
                    "title": "Solder wire 4T",
                    "body": "Check that cable and look for bugs in the shed, they crash the machine",
                    "creation_date": "1940-03-18T08:00:00Z",
                    "deletion_date": "1940-03-18T18:32:00Z",
                    "owner": "0"
                },
                {
                    "title": "Beer with pals",
                    "body": "I have a beer with my colleagues down at the pub, remember not to dance.",
                    "creation_date": "1939-08-15T08:00:00Z",
                    "owner": "0"
                },
                {
                    "title": "Send message",
                    "body": "Remember to send message to Bob Alicer without getting it sniffed.",
                    "creation_date": "2000-01-01T09:30:12Z",
                    "owner": "1"
                },
            ],
        };
    },
    methods: {
        async fetchReminders() {
            this.reminders = await ReminderService.getReminders();
        },
    },
    components: {
        ReminderItem,
    },
};
</script>
  