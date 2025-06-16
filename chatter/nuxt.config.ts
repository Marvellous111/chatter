// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-05-15',
  
  devtools: {
    enabled: false
  },
  
  css: [
    "~/assets/styles/main.scss",
    "~/assets/styles/markdown.scss"
  ],

  modules: [
    //'@nuxt/eslint',
    '@nuxt/fonts',
    '@nuxt/icon',
    '@nuxt/image',
    //'@nuxt/scripts',
    //'@nuxt/content',
    '@pinia/nuxt',
  ]
})