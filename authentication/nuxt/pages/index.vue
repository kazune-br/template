<template>
  <v-row justify="center">
    <v-col cols="12">
      <div class="text-center">
        <logo/>
      </div>
    </v-col>
    <v-col cols="12">
      <v-card>
      <v-card-title class="headline">
        Welcome to the Vuetify + Nuxt.js template
      </v-card-title>
      <v-card-actions>
        <v-spacer/>
        <v-btn
          nuxt
          to="/inspire"
          icon
        >
          <v-icon>star</v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
    </v-col>
  </v-row>
</template>

<script>
  import Logo from '~/components/Logo.vue'

  export default {
    components: {
      Logo,
    }
  }
</script>
