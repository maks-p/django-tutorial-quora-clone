<template>
  <div id="app">
    <NavbarComponent />
    <router-view />
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js"
import NavbarComponent from "@/components/Navbar.vue"
export default {
    name: "App",
    components: {
        NavbarComponent
    },
    methods: {
        async setUserInfo() {
            const data = await apiService("/api/user/");
            const requestUser = data['username'];
            window.localStorage.setItem('username', requestUser);
        }
    },
    created() {
        this.setUserInfo();
    }
}
</script>

<style>
    html, body {
        height: 100%;
        font-family: 'Roboto Mono', monospace;
    }
</style>
