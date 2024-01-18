// src/services/AuthService.js
import axios from 'axios';
import { reactive } from 'vue';

const API_URL = process.env.API_URL

class ReminderService {
    data = reactive({
        authenticated: true,
    });

    getReminders() {
        return axios.get(`${API_URL}/reminders`);
    }

    createReminder(reminder) {
        return axios.post(`${API_URL}/reminders`, reminder);
    }

    deleteReminder(id) {
        return axios.delete(`${API_URL}/reminders/${id}`);
    }
}

export default new ReminderService();
