<template>
    <nav class="navbar navbar-expand-sm navbar-light bg-light justify-content-between my-navbar">
        
        <div class="navbar-brand active">
            <router-link
                :to="{ name: 'home' }"
                class="title-home"
            >Quora Clone
            </router-link>
        </div>

        <div class="collapse navbar-collapse">
            <div class="navbar-nav">
                <div class="nav-item nav-link">
                    <router-link
                        :to="{ name: 'about' }"
                        class="other-links"
                    >About
                    </router-link>
                </div>
                 <div class="nav-item nav-link">
                    <a class="other-links" href="/accounts/logout/"
                    >Logout
                    </a>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
  name: "NavbarComponent"
};
</script>

<style>
    .my-navbar {
        border-bottom: 1px solid #DDD
    }

    .title-home {
        font-size: 125%;
        color: #42b983;
    }

    .other-links {
        font-size: 125%;
        color: grey;
    }
</style>