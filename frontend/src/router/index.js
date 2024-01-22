import { createWebHistory, createRouter } from "vue-router";
import HomeView from "../components/HomeView.vue";
import UserLogin from "../components/UserLogin.vue";
import UserRegistration from "../components/UserRegistration.vue";
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
    path: "/login",
    component: UserLogin,
  },
  {
    path: "/register",
    component: UserRegistration,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;