<template>
    <header id="header">
        <button @click="forwardToCreate" class="btn btn-primary">Create Reminder</button>
    </header>
    <main>
        <ReminderList />
    </main>
</template>

<script>
import ReminderList from "../components/ReminderList.vue";

export default {
    components: {
        ReminderList,
    },
    methods: {
        forwardToCreate() {
            this.$router.push("/create");
        },
    },
};
</script>

<style>
#header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
}
</style>