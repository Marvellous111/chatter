<script lang="ts" setup>
import { Globe, ChevronDown } from 'lucide-vue-next';
</script>

<template>
  <section class="model-features-container">
    <div class="model-dropdown">
      <span class="geist-regular">Gemini 2.5 Flash</span>
      <ChevronDown :size="16" absoluteStrokeWidth />
    </div>
    <div class="features">
      <button class="feature-button">
        <Globe :size="18" absoluteStrokeWidth class="icon" />
        <span class="geist-regular">Search</span>
      </button>
    </div>
  </section>
</template>

<style lang="scss" scoped>
.model-features-container {
  //border: 1px solid white;
  display: flex;
  column-gap: 10px;
  align-items: center;
  .model-dropdown {
    border-radius: 7.5px;
    color: rgba(255, 255, 255, 0.5);
    min-width: 70px;
    display: flex;
    align-items: center;
    column-gap: 10px;
    width: fit-content;
    height: 13px;
    padding: 10px 10px 10px 7.5px;
    transition: 0.2s ease-in;
    span {
      font-size: 14px;
    }
  }
  .model-dropdown:hover {
    background: rgba(128, 128, 128, 0.1);
    color: #FFFFFF;
  }
  .features {
    display: flex;
    align-items: center;
    height: 38px;
    button {
      background: inherit;
      outline: 0;
      border: 1px solid rgba(136, 136, 136, 0.5);
      width: fit-content;
      height: 13px;
      padding: 15px 10px 15px 7.5px;
      column-gap: 7.5px;
      border-radius: 25px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      span {
        color: rgba(250, 250, 250, 0.6);
        font-size: 13px;
        display: flex;
        align-items: center;
      }
      .icon {
        color: rgba(250, 250, 250, 0.6);
      }
    }
  }
}
</style>