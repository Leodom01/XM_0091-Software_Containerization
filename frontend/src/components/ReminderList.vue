<template>
    <div>
        <div v-if="message" class="alert alert-danger" role="alert">
            {{ message }}
        </div>
        <div v-else-if="reminders.length === 0" id="message">
            <p>No reminders yet.</p>
        </div>
        <div v-else>
            <div v-for="reminder in reminders" :key="reminder.id" id="item">
                <h3>{{ reminder.title }}</h3>
                <p>{{ reminder.body }}</p>
            </div>
        </div>
    </div>
</template>
  
<script>
import ReminderService from '@/services/reminder.service';

export default {
    data() {
        return {
            message: "",
            reminders: [
                // {
                //     "title": "Solder wire 4T",
                //     "body": "Check that cable and look for bugs in the shed, they crash the machine",
                //     "creation_date": "1940-03-18T08:00:00Z",
                //     "deletion_date": "1940-03-18T18:32:00Z",
                //     "owner": "0"
                // },
                // {
                //     "title": "Beer with pals",
                //     "body": "I have a beer with my colleagues down at the pub, remember not to dance.",
                //     "creation_date": "1939-08-15T08:00:00Z",
                //     "owner": "0"
                // },
                // {
                //     "title": "Send message",
                //     "body": "Remember to send message to Bob Alicer without getting it sniffed.",
                //     "creation_date": "2000-01-01T09:30:12Z",
                //     "owner": "1"
                // },
            ],
        };
    },
    methods: {
        async fetchReminders() {
            ReminderService.getReminders().then(
                (response) => {
                    this.message = "";
                    this.reminders = response.data;
                },
                (error) => {
                    this.message =
                        (error.response &&
                            error.response.data &&
                            error.response.data.message) ||
                        error.message ||
                        error.toString();
                }
            );
        },
        // async deleteReminder(reminderId) {
        //     ReminderService.deleteReminder(reminderId).then(
        //         () => {
        //             this.message = "";
        //             this.fetchReminders();
        //         },
        //         (error) => {
        //             this.message =
        //                 (error.response &&
        //                     error.response.data &&
        //                     error.response.data.message) ||
        //                 error.message ||
        //                 error.toString();
        //         }
        //     );
        // }
    },
    created() {
        this.fetchReminders();
    },
    components: {
    },
};
</script>
  
<style>
#item {
    border: 1px solid black;
    margin: 10px;
    padding: 10px;
}

#message {
    margin: 10px;
    padding: 10px;
}
</style>