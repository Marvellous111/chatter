<script lang="ts" setup>
import { Copy, GitBranchPlus, RotateCcw, Zap, Cpu, Clock2 } from 'lucide-vue-next';
import { computed, defineComponent } from 'vue';
import { Marked } from 'marked';
import { markedHighlight } from 'marked-highlight';
import hljs from 'highlight.js';
import DOMPurify from 'dompurify'

const marked = new Marked(
  markedHighlight({
	emptyLangClass: 'hljs',
    langPrefix: 'hljs language-',
    highlight(code, lang, info) {
      const language = hljs.getLanguage(lang) ? lang : 'plaintext';
      return hljs.highlight(code, { language }).value;
    }
  })
);

const props = defineProps({
  content: {
    type: String,
    required: true,
  }
});

const renderedMarkdown = computed(() => marked.parse(props.content))
</script>

<template>
  <div class="chatter geist-regular">
    <div class="chatter-response-text" v-html="renderedMarkdown"></div>
    <div class="chatter-response-details">
      <button class="response-icon">
        <Copy :size="16" absoluteStrokeWidth />
      </button>
      <button class="response-icon">
        <GitBranchPlus :size="16" absoluteStrokeWidth />  
      </button>
      <button class="response-icon">
        <RotateCcw :size="16" absoluteStrokeWidth />  
      </button>
      <div class="chatter-response-model-details">
        <span class="response-model-text geist-regular">Gemini 2.5 flash</span>
        <div class="response-model response-model-speed">
          <Zap :size="13" absoluteStrokeWidth />
          <span class="response-model-text geist-regular">112 tok/sec</span>
        </div>
        <div class="response-model response-model-token-count">
          <Cpu :size="13" absoluteStrokeWidth />
          <span class="response-model-text geist-regular">228 tokens</span>
        </div>
        <div class="response-model response-model-token-time">
          <Clock2 :size="13" absoluteStrokeWidth />
          <span class="response-model-text geist-regular">0.52 sec</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.chatter {
  text-align: left;
  font-size: 15px;
  //margin-bottom: 26%;
  display: flex;
  flex-direction: column;
  row-gap: 20px;
  .chatter-response-text {
    //font-weight: normal;
    letter-spacing: 0.4px;
    word-break: break-word;
  }
  .chatter-response-details {
    transition: opacity 0.2s ease-in-out, visibility 0.2s ease-in-out;
    opacity: 0;
    visibility: hidden;
    display: flex;
    column-gap: 5px;
    align-items: center;
    height: 28px;
    .response-icon {
      outline: 0;
      border: 0;
      background: inherit;
      border-radius: 7.5px;
      width: fit-content;
      height: fit-content;
      align-items: center;
      justify-content: center;
      padding: 7.5px 7.5px 5px 7.5px;
      color: #fafafa;
      transition: background 0.2s ease-in;
    }
    .response-icon:hover {
      background: rgba(128, 128, 128, 0.1);
    }
    .chatter-response-model-details {
      display: flex;
      column-gap: 7.5px;
      align-items: center;
      height: 24px;
      color: rgba(128, 128, 128, 1);
      .response-model-text {
        font-size: 12px;
        letter-spacing: 0.2px;
      }
      .response-model {
        display: flex;
        column-gap: 5px;
        align-items: center;
      }
    }
  }
}
.chatter:hover {
  .chatter-response-details {
    opacity: 1;
    visibility: visible;
  }
}
</style>