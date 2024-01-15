<template>
    <div>
        <h2>Reminders</h2>
        <ul>
            <li v-for="reminder in reminders" :key="reminder.id">
                {{ reminder.title }} - {{ reminder.body }}
            </li>
        </ul>
    </div>
</template>
  
<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
    setup() {
        const reminders = ref([]);
        const yourAuthToken = localStorage.getItem('authToken');

        onMounted(async () => {
            try {
                const response = await axios.get('http://your-api-url/reminders', {
                    headers: {
                        Authorization: `Bearer ${yourAuthToken}`, // Include the user's authentication token
                    },
                });
                reminders.value = response.data;
            } catch (error) {
                console.error('Error fetching reminders:', error);
            }
        });

        return {
            reminders,
        };
    },
};
</script>
  