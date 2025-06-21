<script lang="ts" setup>
import { ArrowUp } from 'lucide-vue-next'
import { ref } from 'vue';
definePageMeta({
  layout: 'backtochat'
})

var username = ref("");
var password = ref("");

var signing = ref(false);

function signin() {
  if (username.value.length < 3 || password.value.length < 6) {
    return
  }
  try {
    console.log("heyy")
  }catch (error) {
    console.log(error)
  }
}


</script>

<template>
  <!-- Authentication via other platforms should be added soon (like x?) -->
  <body class="auth-page">
    <div class="google-auth-form">
      <h2 class="geist-semibold">Welcome to <strong>chatter</strong></h2>
      <span class="geist-regular google-span">Sign in and enjoy higher message limits</span>
      <form>
        <div class="form-input-container">
          <label class="form-label geist-regular">Username</label>
          <input type="text" placeholder="Username" v-model="username" pattern="[A-Za-z0-9]+" title="Only letters and numbers are allowed" required class="form-input geist-medium" />
        </div>
        <div class="form-input-container">
          <label class="form-label geist-regular">Password</label>
          <input type="password" placeholder="Password" v-model="password" class="form-input geist-medium" required />
        </div>
      </form>
      <button class="google-button">
        <span class="button-text geist-medium">Sign in</span>
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
    row-gap: 20px;
    width: 350px;
    height: 200px;
    padding: 7.5px;
    border-radius: 12.5px;
    align-items: center;
    margin-top: -10%;
    .google-span {
      color: #fafafa;
      text-align: center;
    }
    h2 {
      font-size: 20px;
      color: #fafafa;
      margin: 0;
      width: stretch;
      text-align: center;
    }
    form {
      display: flex;
      flex-direction: column;
      row-gap: 20px;
      width: fit-content;
      height: fit-content;
      padding: 10px 20px;
      .form-input-container {
        display: flex;
        flex-direction: column;
        align-items: left;
        row-gap: 10px;
        label {
          color: #fafafa;
        }
        input {
          background: inherit;
          height: 32px;
          border: 0;
          font-size: 14px;
          border-bottom: 1px solid rgba(80,80,80, 0.5);
          outline: 0;
          color: #fafafa;
        }
        input::placeholder {
          color: rgba(250, 250, 250, 0.6);
          font-family: "geist-regular";
        }
      }
    }
    button {
      width: 200px;
      height: 28px;
      display: flex;
      border: 0;
      outline: 0;
      text-decoration: none;
      background: #FAFAFA;
      align-items: center;
      justify-content: center;
      border-radius: 7.5px;
      padding: 15px 15px 15px 15px;
      column-gap: 10px;
      color: #121212;
      transition: background 0.2s ease-in;
      span {
        font-size: 14px;
      }
    }

  }
}
</style>