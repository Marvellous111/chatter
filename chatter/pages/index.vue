<script lang="ts" setup>
import { ArrowUp, GitBranchPlus } from 'lucide-vue-next'
import { ref } from 'vue';

interface Response {
  content: string;

}

const responses = ref<Response>
const test_md=`# Welcome to docs4.dev

Paragraphs can but should not contain inline code \`const codeInline: string = 'highlighted code inline'\`{lang="ts"} with language prop.

Code block:
\`\`\` typescript [index.js] {1, 3 - 5} additional meta data
import {parseMarkdown} from '@nuxtjs/mdc/runtime'

async function main(mdc: string) {
  const ast = await parseMarkdown(mdc)

  return ast
}
\`\`\`

> This is a quote in response.\n\nHere's some **bold** text and a list:\n- Item 1\n- Item 2
`
function send() {
  return
}

</script>

<template>
  <section class="chat-section">
    <div class="chat-container">
      <div class="user geist-regular">
        Are black holes real?
      </div>
      <ChatResponse :content="test_md" />
    </div>
    <div class="outer-input-field">
      <div class="inner-input-field">
        <textarea class="input-area geist-regular" placeholder="Type your message here..."></textarea>
        <section class="model-send-section">
          <ChatModels />
          <button class="send-button" @click="send">
            <ArrowUp :size="24" absoluteStrokeWidth />
          </button>
        </section>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
.chat-section::-webkit-scrollbar{
  display: none;
  background: none;
  border: 1px solid white;
  scrollbar-width: 5px;
  color: rgba(18, 18, 18, 0.4);
}
.chat-section {
  scrollbar-width: 0px;
  -ms-overflow-style: none;
}

.chat-container::-webkit-scrollbar {
  display: none;
}
.chat-container {
    scrollbar-width: 0px;
  -ms-overflow-style: none;
}

.chat-section {
  width: stretch;
  height: stretch;
  position: relative;
  border-radius: inherit;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow: hidden;
  overflow-y: visible;
  padding: 0px 20px 20px 20px;
  .chat-container {
    color: #fafafa;
    width: 75%;
    display: flex;
    position: absolute;
    flex-direction: column;
    row-gap: 40px;
    padding-top: 40px;
    overflow-x: hidden;
    overflow-y: hidden;
    height: fit-content;
    //border: 1px solid;
    .user {
      align-self: flex-end;
      display: flex;
      width: fit-content;
      min-height: 18px;
      justify-content: left;
      align-items: center;
      padding: 10px 15px;
      border-radius: 10px;
      background: rgba(128, 128, 128, 0.2);
      border: 1px solid rgba(128, 128, 128, 0.1);
      color: #fafafa;
      font-size: 15px;
    }
    
  }
  .outer-input-field {
    z-index: 10;
    width: 60%;
    position: fixed;
    bottom: 0px;
    display: flex;
    min-height: 20%;
    max-height: fit-content;
    height: 20%;
    padding: 7.5px 7.5px 0px 7.5px;
    border-radius: 15px 15px 0px 0px;
    background-color: rgba(18, 18, 18, 0.4);
    border: 1px solid rgba(136, 136, 136, 0.1);
    border-bottom: 0;
    .inner-input-field {
      display: flex;
      flex-direction: column;
      row-gap: 0;
      height: stretch;
      min-height: stretch;
      max-height: fit-content;
      width: stretch;
      border-radius: 7.5px 7.5px 0px 0px;
      background-color: rgba(18, 18, 18, 1);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-bottom: 0;
      textarea {
        display: flex;
        border-radius: inherit;
        width: stretch;
        background: inherit;
        height: 60%;
        resize: none;
        outline: 0;
        padding: 15px 15px 0px 15px;
        font-size: 16px;
        //font-weight: normal;
        border: 0;
        color: #fafafa;
      }
      textarea::placeholder {
        color: rgba(250, 250, 250, 0.6);
        font-family: "geist-light";
      }
      .model-send-section {
        display: flex;
        //border: 1px solid white;
        width: stretch;
        height: 40%;
        justify-content: space-between;
        padding-left: 7.5px;
        padding-right: 15px;
        //margin-top: 5px;
        .send-button {
          border-radius: 7.5px;
          outline: 0;
          border: 0;
          width: 38px;
          height: 38px;
          display: flex;
          align-items: center;
          justify-content: center;
        }
      }
    }
  }
}
</style>

