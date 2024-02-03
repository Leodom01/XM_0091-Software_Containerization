<template>
    <div id="create">
        <h2>Create Reminder</h2>
        <Form @submit="handleCreate">
            <Field name="title" type="text" placeholder="Title" v-model="formData.title" />
            <ErrorMessage name="title" />
            <Field name="body" type="text" placeholder="Body" v-model="formData.body" />
            <ErrorMessage name="body" />
            <button type="submit" class="btn btn-primary">Create</button>
            <div v-if="message" class="alert alert-danger" role="alert">
                {{ message }}
            </div>
        </Form>
    </div>
</template>

<script>
import { Form, Field, ErrorMessage } from "vee-validate";
import * as yup from "yup";
import ReminderService from '@/services/reminder.service';

export default {
    name: "CreateReminderView",
    components: {
        Form,
        Field,
        ErrorMessage,
    },
    data() {
        const schema = yup.object().shape({
            title: yup.string().required("Title is required!"),
            body: yup.string().required("Body is required!"),
        });

        return {
            formData: {
                title: "",
                body: "",
            },
            message: "",
            schema,
        };
    },
    methods: {
        async handleCreate() {
            ReminderService.createReminder(this.formData).then(
                () => {
                    this.$router.push("/");
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
        }
    }
};
</script>

<style>
#create {
    border: 1px solid black;
    margin: 10px;
    padding: 10px;
}
</style>