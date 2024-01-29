import axios from 'axios';
import authHeader from './auth-header';

let API_URI = process.env.VUE_APP_API_URI;
if (!API_URI) {
    API_URI = "app-service.default.svc.cluster.local:8081"
}
const API_URL = '//' + API_URI;
const REMINDERS_ENDPOINT = '/reminders';

class ReminderService {
    getReminders() {
        return axios.get(API_URL + REMINDERS_ENDPOINT, { headers: authHeader() });

    }

    createReminder(reminder) {
        return axios.post(API_URL + REMINDERS_ENDPOINT, reminder, { headers: authHeader() });

    }

    deleteReminder(reminderId) {
        return axios.delete(API_URL + REMINDERS_ENDPOINT + '/' + reminderId, { headers: authHeader() });
    }
}

export default new ReminderService();