<script lang="ts" setup>
import { PanelRight, GitBranchPlus, Trash2 } from 'lucide-vue-next'
</script>

<template>
  <section class="layout-section">
    <nav class="sidebar">
      <div class="logo-expand-container">
        <div class="ec-button">
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
    </nav>
    <main class="body-main">
      <slot />
    </main>
  </section>
</template>

<style lang="scss" scoped>
.layout-section {
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
      height: fit-content;
      max-height: stretch;
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
  }
  .body-main {
    max-width: 97vw;
    max-height: 99vh;
    width: stretch;
    height: 98vh;
    margin-right: 1vw;
    border-radius: 7.5px 7.5px 0px 0px;
    background: #1a1a1a;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    //border: 1px solid white;
  }
}
</style>