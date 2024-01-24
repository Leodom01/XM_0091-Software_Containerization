import axios from 'axios';
import authHeader from './auth-header';

const API_URL = process.env.VUE_APP_API_URL;
const REMINDERS_ENDPOINT = '/reminders';

class ReminderService {
    // throw errors if the response is not 200
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