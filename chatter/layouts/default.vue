<script lang="ts" setup>
import { PanelRight, GitBranchPlus, Trash2, LogIn, Search, Plus } from 'lucide-vue-next'
import { useRouter } from 'vue-router';
import { onMounted, ref } from 'vue';

const router = useRouter();

function moveToSignin() {
  router.push('/auth/')
}

const sidebar = ref<HTMLElement|null>(null);
const mainbody = ref<HTMLElement|null>(null);
const bodyButtonContainer = ref<HTMLElement|null>(null);

const hideSidebar = () => {
  if (!sidebar.value) return
  if (!mainbody.value) return
  if (!bodyButtonContainer.value) return
  sidebar.value.style.transform = "translateX(-30px)";
  sidebar.value.style.opacity = "0";
  sidebar.value.style.visibility = "hidden"
  sidebar.value.style.width = "0";
  sidebar.value.style.paddingLeft = "0";
  sidebar.value.style.paddingRight = "0";
  sidebar.value.style.transition = "width 0.9s ease, visibility 0.4s ease, opacity 0.4s ease, translate 0.7s ease, padding 0.9s ease";
  mainbody.value.style.width = "stretch";
  bodyButtonContainer.value.style.visibility = "visible";
  bodyButtonContainer.value.style.opacity = "1";
}
const showSidebar = () => {
  if (!sidebar.value) return
  if (!mainbody.value) return
  if (!bodyButtonContainer.value) return
  sidebar.value.style.transform = "translateX(0)";
  sidebar.value.style.opacity = "1";
  sidebar.value.style.visibility = "visible"

  if (window.innerWidth >= 1024) {
    sidebar.value.style.width = "20vw";
  } else if(window.innerWidth <= 767) {
    sidebar.value.style.width = "55vw";
  } else if (window.innerWidth >= 768 && window.innerWidth <= 1023) {
    sidebar.value.style.width = "30vw";
  }

  sidebar.value.style.paddingLeft = "20px";
  sidebar.value.style.paddingRight = "20px";
  sidebar.value.style.transition = "width 0.6s ease, visibility 1.0s ease-in, opacity 1.0s ease-in, translate 1.0s ease, padding 0.7s ease";
  mainbody.value.style.width = "stretch";
  bodyButtonContainer.value.style.visibility = "hidden";
  bodyButtonContainer.value.style.opacity = "0";
}

// onMounted(() => {
//   if (window.innerWidth <= 767) {
//     hideSidebar()
//   }
// })

</script>

<template>
  <section class="layout-section">
    <nav class="sidebar" ref="sidebar">
      <div class="logo-expand-container">
        <div class="ec-button" @click="hideSidebar">
          <PanelRight :size="18" absoluteStrokeWidth />
        </div>
        <h2 class="geist-medium">Chatter</h2>
      </div>
      <button class="new-chat geist-medium">New chat</button>
      <input type="text" placeholder="Type to search for chat..." class="search-input geist-medium" />
      <div class="chats-container">
        <span class="chat-date-group geist-light">Last 7 days</span>
        <NuxtLink to="/" class="chat-link">
          <span class="chat-link-text geist-regular">First chat</span>
          <div class="chat-options">
            <div class="chat-option-icons branch-icon">
              <GitBranchPlus :size="14" absoluteStrokeWidth />
            </div>
            <div class="chat-option-icons delete-icon">
              <Trash2 :size="14" absoluteStrokeWidth />
            </div>
          </div>
        </NuxtLink>
      </div>
      <NuxtLink to='/auth' class="signin-button">
        <LogIn :size="16" absoluteStrokeWidth />
        <span class="geist-medium">Login</span>
      </NuxtLink>
    </nav>
    <main class="body-main" ref="mainbody">
      <div class="body-button-containers" ref="bodyButtonContainer">
        <div class="transparent-icon-white" @click="showSidebar">
          <PanelRight :size="16" absoluteStrokeWidth />
        </div>
        <div class="transparent-icon-white" @click="hideSidebar">
          <Search :size="16" absoluteStrokeWidth />
        </div>
        <div class="transparent-icon-white" @click="hideSidebar">
          <Plus :size="16" absoluteStrokeWidth />
        </div>
      </div>
      <slot />
    </main>
  </section>
</template>

<style lang="scss" scoped>
.layout-section {
  position: relative;
  height: 100vh;
  background: #121212;
  display: flex;
  align-items: end;
  justify-content: space-between;
  nav {
    height: stretch;
    width: 20vw;
    display: flex;
    flex-direction: column;
    padding: 20px;
    row-gap: 15px;
    color: white;
    transition: width 0.9s ease, visibility 0.4s ease, opacity 0.4s ease, translate 0.7s ease, padding 0.9s ease; 
    @include responsive(mobile) {
      position: fixed;
      top: 0;
      z-index: 80;
      width: 0;
      visibility: hidden;
      opacity: 0;
      transform: translateX(-30px);
      padding-left: 0;
      padding-right: 0;
      background: #121212;
    }
    @include responsive(tablet) {
      position: fixed;
      top: 0;
      z-index: 80;
      width: 0;
      visibility: hidden;
      opacity: 0;
      transform: translateX(-30px);
      padding-left: 0;
      padding-right: 0;
      background: #121212;
    }
    .logo-expand-container {
      display: flex;
      //border: 1px solid white;
      align-items: start;
      justify-content: center;
      position: relative;
      .ec-button {
        position: absolute;
        z-index: 20;
        left: -5px;
        //border: 1px solid white;
        width: 28px;
        height: 28px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: inherit;
        border-radius: 7.5px;
        cursor: pointer;
      }
      h2 {
        margin: 0;
      }
    }
    .new-chat {
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(250, 250, 250, 0.9);
      color: #121212;
      border: 1px solid rgba(128, 128, 128, 0.5);
      outline: 0;
      border-radius: 7.5px;
      height: 32px;
      padding: 0px 10px;
      font-size: 14px;
    }
    .search-input {
      background: inherit;
      height: 32px;
      border: 0;
      font-size: 14px;
      border-bottom: 1px solid rgba(80,80,80, 0.5);
      outline: 0;
      color: #fafafa;
    }
    .search-input::placeholder {
      color: rgba(250, 250, 250, 0.6);
      font-family: "geist-regular";
    }
    .chats-container::-webkit-scrollbar {
      display: none;
    }
    .chats-container {
      display: flex;
      flex-direction: column;
      width: stretch;
      flex-grow: 1;
      //max-height: 100%;
      overflow-y: visible;
      overflow-x: hidden;
      scrollbar-width: 0px;
      row-gap: 10px;
      -ms-overflow-style: none;
      .chat-date-group {
        width: stretch;
        height:fit-content;
        display: flex;
        align-items: center;
        text-align: left;
        font-size: 12px;
        color: rgba(250, 250, 250, 0.6);
      }
      .chat-link {
        text-decoration: none;
        color: #fafafa;
        width: stretch;
        height: 28px;
        padding: 5px 6px 5px 10px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-radius: 7.5px;
        background: rgba(128, 128, 128, 0.1);
        .chat-link-text {
          font-size: 14px;
        }
        .chat-options {
          opacity: 0;
          visibility: hidden;
          transform: translateX(15px);
          display: flex;
          align-items: center;
          column-gap: 5px;
          transition: transform 0.2s ease-in, opacity 0.2s ease-in, visibility 0.2s ease-in;
          .chat-option-icons {
            display: flex;
            color: rgba(128, 128, 128, 1);
            align-items: center;
            justify-content: center;
            border-radius: 5px;
            width: 16px;
            height: 16px;
            padding: 6px;
            background: inherit;
            transition: 0.2s ease-in;
          }
          .chat-option-icons:hover {
            background: rgba(128, 128, 128, 0.1);
            color: #fafafa;
          }
        }
      }
      .chat-link:hover {
        .chat-options {
          opacity: 1;
          visibility: visible;
          transform: translateX(0);
        }
      }
    }
    .signin-button {
      width: stretch;
      height: 22px;
      display: flex;
      border: 0;
      outline: 0;
      text-decoration: none;
      background: inherit;
      align-items: center;
      justify-content: left;
      border-radius: 7.5px;
      padding: 15px 15px 15px 15px;
      column-gap: 10px;
      color: #fafafa;
      transition: background 0.2s ease-in;
      span {
        font-size: 16px;
      }
    }
    .signin-button:hover {
      background: rgba(128, 128, 128, 0.1);
    }
  }
  .body-main {
    //max-height: 98vh;
    width: stretch;
    height: stretch;
    margin-top: 2vh;
    margin-right: 1vw;
    margin-left: 1vw;
    border-radius: 7.5px 7.5px 0px 0px;
    background: #1a1a1a;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    transition: all 0.5s ease;
    @include responsive(tablet) {
      margin-top: 1vh;
    }
    .body-button-containers {
      opacity: 0;
      visibility: hidden;
      position: absolute;
      top: 15px;
      left: 15px;
      display: flex;
      border-radius: 10px;
      background: #121212;
      z-index: 78;
      padding: 5px;
      transition: all 0.5s ease;
      @include responsive(mobile) {
        opacity: 1;
        visibility: visible;
      }
      @include responsive(tablet) {
        opacity: 1;
        visibility: visible;
      }
    }
  }
}
</style>