<script lang="ts" setup>
import { ArrowUp, GitBranchPlus, StopCircle } from 'lucide-vue-next'
import { nextTick, onMounted, ref, watch } from 'vue';
import { query, type Query, chat, type Chat } from '../interfaces/ChatSchema';
import { useFetch } from '#app';

useSeoMeta({
  title: 'Chatter'
})

const query_input = ref("");

const streamingResponse = ref(``);
const isStreaming = ref(false);
const error = ref<string|any>(null);

var chats = ref<Chat[]>([]);

async function send() {

  if (query_input.value.length < 2) {
    console.log("Please type in a query");
    return
  } 

  streamingResponse.value = '';
  isStreaming.value = true;
  error.value = null;

  const body = query.safeParse({
    content: query_input.value,
    model_used: "gemini-2.5-flash",
    model_provider: "Google",
    attachment_status: false,
    websearch: false,
    deepreasoning: false
  });

  try {
    console.log("Sending to backend");
    const response = await fetch('/api/chat-stream', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body.data),
    })
    isStreaming.value = true
    if (!response.ok) {
      error.value = response
      return
    }
    const reader = response.body?.getReader();
    const decoder = new TextDecoder();
    if (reader) {
      while (true) {
        const { done, value } = await reader!.read()
        if (done) {
          const newchat: Chat = {
            content: query_input.value,
            response: streamingResponse.value
          }
          chats.value.push(newchat)
          break
        }
        const chunk = decoder.decode(value, {
          stream: true
        })
        streamingResponse.value += chunk
      }
    }
  }catch(error: any) {
    console.log(error)
    error.value = error
  } finally {
    isStreaming.value = false;
    if (error.value) return
    query_input.value = "";
  }
  const clearResponse = () => {
    streamingResponse.value = ''
    error.value = null
  }
}

const chatContainer = ref<HTMLElement|null>(null);
watch(chats, async () => {
  await nextTick()
  if (chatContainer.value) {
    chatContainer.value.scrollTo({
      top: chatContainer.value.scrollHeight,
      behavior: 'smooth'
    })
  }
})
const textarea = ref<HTMLElement|null>(null);
const outerField = ref<HTMLElement|null>(null);
const ratelimit = ref(42);
const textareaHeightPercent = ref(20)
var gapHeight = ref(textarea.value?.scrollHeight + 75);
const ratelimitDistance = ref();
const outerWidth = ref();
const outerHeight = ref();
const resizeTextArea = () => {
  if (!textarea.value) return
  if (!outerField.value) return
  
  
  textarea.value.style.height = 'auto';
  const newHeight = textarea.value.scrollHeight
  textarea.value.style.height = `${newHeight}px`;
  textarea.value.style.transition = "height 0.2s ease-in";
  const viewportheight = window.innerHeight;
  textareaHeightPercent.value = newHeight;
  gapHeight.value = newHeight + 75;
  outerWidth.value = outerField.value.clientWidth;
}

onMounted(() => {
  resizeTextArea()
})
</script>

<template>
  <section class="chat-section">
    <div class="chat-container" ref="chatContainer" :style="{ width: `${outerWidth}px` }">
      <div class="query-response" v-for="(chats, index) in chats" :key="index">
        <div class="user geist-regular">
          {{ chats.content }}
        </div>
        <ChatResponse :content="chats.response" />
      </div>
      <div class="query-response" v-if="isStreaming">
        <div class="user geist-regular">
          {{ query_input }}
        </div>
        <ChatResponse :content="streamingResponse" />
      </div>
    </div>
    <div class="outer-input-field" ref="outerField">
      <div class="rate-limit" ref="ratelimit" :style="{ bottom: `${gapHeight}px`, width: `${outerWidth-15}px` }">
        <ChatRateLimit />
      </div>
      <div class="inner-input-field">
        <textarea class="input-area geist-regular" ref="textarea" @input="resizeTextArea" placeholder="Type your message here..." v-model="query_input" :disabled="isStreaming"></textarea>
        <section class="model-send-section">
          <ChatModels /> 
          <button class="send-button" @click="send" :disabled="isStreaming || query_input.length < 2" v-if="isStreaming == false">
            <ArrowUp :size="24" absoluteStrokeWidth />
          </button>
          <button class="send-button" @click="send" :disabled="isStreaming || query_input.length < 2" v-if="isStreaming == true">
            <StopCircle :size="24" absoluteStrokeWidth />
          </button>
        </section>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
.chat-section::-webkit-scrollbar{
  width: 5px;
}
.chat-section::-webkit-scrollbar-track{
  background: transparent;
}
.chat-section::-webkit-scrollbar-thumb{
  background-color: #888;
  border-radius: 4px;
}
.chat-section::-webkit-scrollbar-thumb:hover{
  background-color: #555;
  border-radius: 4px;
}
.chat-section {
  scrollbar-width: thin;
  scrollbar-color: #888 transparent;
  scroll-behavior: smooth;
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
  overflow-y: auto;
  padding: 0px 20px 20px 20px;
  .chat-container {
    color: #fafafa;
    // max-width: 60%;
    // width: 75%;
    // min-width: 75%;
    display: flex;
    position: absolute;
    flex-direction: column;
    padding-top: 40px;
    overflow-x: hidden;
    overflow-y: hidden;
    height: fit-content;
    padding-bottom: 20%;
    row-gap: 20px;
    .query-response {
      position: relative;
      display: flex;
      flex-direction: column;
      gap: 20px;
      height:fit-content;
      width:stretch;
      z-index: 0;
      //margin-top: 0;
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
    
  }
  .outer-input-field {
    z-index: 10;
    width: 60%;
    position: fixed;
    bottom: 0px;
    display: flex;
    min-height: 18%;
    max-height: auto;
    height: auto;
    padding: 7.5px 7.5px 0px 7.5px;
    border-radius: 15px 15px 0px 0px;
    background-color: rgba(18, 18, 18, 0.4);
    border: 1px solid rgba(136, 136, 136, 0.1);
    border-bottom: 0;
    @include responsive(mobile) {
      min-height: 120px;
      max-height:auto;
      height:120px;
      width: 93%;
    }
    @include responsive(tablet) {
      min-height: 120px;
      max-height:auto;
      height:120px;
      width: 93%;
    }
    .rate-limit {
      width: 60%;
      display: flex;
      position: fixed;
      // bottom: 22%;
    }
    .inner-input-field {
      display: flex;
      flex-direction: column;
      row-gap: 0;
      height: stretch;
      min-height: stretch;
      // max-height: fit-content;
      width: stretch;
      border-radius: 7.5px 7.5px 0px 0px;
      background-color: rgba(18, 18, 18, 1);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-bottom: 0;
      padding-bottom: 10px;
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
        transition: height 0.3s;
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
          cursor: pointer;
        }
      }
    }
  }
}
</style>

