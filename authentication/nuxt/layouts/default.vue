<template>
  <v-app dark>
    <v-app-bar app height="48">
      <v-app-bar-nav-icon />
      <v-btn icon>
        <v-icon>search</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>apps</v-icon>
      </v-btn>
      <v-toolbar-title v-text="title" />
      <v-spacer />
      <v-toolbar-items>
        <template v-if="$auth.loggedIn">
          <v-btn text> {{ $auth.user }} </v-btn>
          <v-btn text>Logout</v-btn>
        </template>
        <template v-else>
          <v-btn text to="login">Login</v-btn>
          <v-btn text to="register">Register</v-btn>
        </template>
      </v-toolbar-items>
    </v-app-bar>

    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>

    <v-footer app>
      <span>&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data () {
    return {
      title: 'Vuetify.js'
    }
  }
}
</script>
