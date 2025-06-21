<script lang="ts" setup>
import { ref } from "vue";
const models = [
  {
    "model_parent": "Meta",
    "model": "llama-3.3-70b-versatile",
    "model_provider": "groq",
    "features": []
  },
  {
    "model_parent": "Anthropic",
    "model": "claude-sonnet-3.5",
    "model_provider": "anthropic",
    "features": ["attachments", "websearch"]
  },
  {
    "model_parent": "OpenAI",
    "model": "chatgpt-4.1",
    "model_provider": "openai", 
    "features": ["attachments", "websearch"]
  },
  {
    "model_parent": "Perplexity",
    "model": "sonar-pro",
    "model_provider": "perplexity",
    "features": ["attachments", "websearch"]
  },
];

const modelPickerContainer = ref<HTMLElement|null>(null);
const modelButton = ref<HTMLElement|null>(null); 

const selectModel = (model: string) => {}
</script>

<template>
  <div class="model-picker-container" ref="modelPickerContainer">
    <div v-for="(model, index) in models" :key="index" class="models" ref="modelButton">
      <button @click="selectModel(model['model'])">{{ model["model"] }}</button>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.model-picker-container {}
</style>