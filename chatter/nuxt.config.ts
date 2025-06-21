// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-05-15',
  
  devtools: {
    enabled: false
  },

  runtimeConfig: {
    server: {
      backend_url: process.env.NUXT_SERVER_BACKEND_URL
    }
  },
  
  css: [
    "~/assets/styles/main.scss",
    "~/assets/styles/markdown.scss"
  ],
  vite: {
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: `@use "@/assets/styles/media" as *;`,
        }
      }
    }
  },

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