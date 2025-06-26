<script lang="ts" setup>
import { ArrowLeft, Settings2 } from 'lucide-vue-next';


const router = useRouter();

function backToChat() {
  router.push('/')
}
</script>

<template>
  <section class="bc-container">
    <nav class="back-to-chat-nav">
      <button class="back-to-chat-button" @click="backToChat">
        <ArrowLeft :size="16" absoluteStrokeWidth />
        <span class="back-to-chat-text geist-medium">Back to chat</span>
      </button>
      <div class="theme-signin-container">
        <button class="theme-icon transparent-button-white">
          <Settings2 :size="16" absoluteStrokeWidth />
        </button>
        <button class="transparent-button-white">
          <span class="geist-regular">Sign up</span>
        </button>
      </div>
    </nav>
    <main>
      <slot />
    </main>
  </section>
</template>

<style lang="scss" scoped>
.bc-container {
  background: #121212;
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: start;
  padding-top: 30px;
  nav {
    //border: 1px solid white;
    display: flex;
    width: stretch;
    padding: 10px 30px;
    height: 28px;
    align-items: center;
    justify-content: space-between;
    .back-to-chat-button {
      display: flex;
      border: 0;
      outline: 0;
      background: inherit;
      align-items: center;
      border-radius: 7.5px;
      width: fit-content;
      height: 18px;
      padding: 20px 15px 20px 7.5px;
      column-gap: 10px;
      color: rgba(255, 255, 255, 1);
      transition: background 0.2s ease-in;
      span {
        font-size: 14px;
      }
    }
    .back-to-chat-button:hover {
      background: rgba(128, 128, 128, 0.1);
    }
    .theme-signin-container {
      display: flex;
    }
  }
  main {
    width: stretch;
    height: stretch;
    display: flex;
    align-items: center;
    justify-content: center;
  }
}
</style>