import { createWebHistory, createRouter } from "vue-router";
import HomeView from "../components/HomeView.vue";
import CreateReminderView from "../components/CreateReminderView.vue";
// lazy-loaded
// const Profile = () => import("./components/Profile.vue")
// const BoardAdmin = () => import("./components/BoardAdmin.vue")
// const BoardModerator = () => import("./components/BoardModerator.vue")
// const BoardUser = () => import("./components/BoardUser.vue")

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/create",
    name: "create",
    component: CreateReminderView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;