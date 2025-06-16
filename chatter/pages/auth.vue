<script lang="ts" setup>
import { ArrowUp } from 'lucide-vue-next'
definePageMeta({
  layout: 'backtochat'
})
</script>

<template>
  <!-- Authentication via other platforms should be added soon (like x?) -->
  <body class="auth-page">
    <div class="google-auth-form">
      <h2 class="geist-semibold">Sign in</h2>
      <button class="google-button">
        <span class="button-text geist-medium">Sign in using google</span>
      </button>
    </div>
  </body>
</template>

<style lang="scss" scoped>
.auth-page {
  width: stretch;
  height: stretch;
  display: flex;
  justify-content: center;
  align-items: center;
  //border: 1px solid white;
  .google-auth-form {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    row-gap: 20px;
    width: 250px;
    height: fit-content;
    padding: 7.5px;
    background: #1a1a1a;
    border-radius: 12.5px;
    h2 {
      font-size: 20px;
      color: #fafafa;
      margin: 0;
      width: stretch;
      text-align: center;
    }
    button {
      width: stretch;
      height: 28px;
      padding: 5px;
      display: flex;
      justify-content: center;
      align-items: center;
      outline: 0;
      border: 0;
      border-radius: 5px;
      span {
        font-size: 14px;
      }
    }

  }
}
</style>