import { defineStore } from 'pinia';
import { type Chat } from '@/interfaces/ChatSchema';
import { ref, computed } from 'vue';

export const useChatStore = defineStore(
  'chatstore', 
  () => {
    const chats = ref<Chat[]>([])
    function AddChat(content: string, response: string) {
      const chat_content: Chat = {
        content,
        response
      };
      chats.value.push(chat_content);
    }
    const getChats = computed(() => chats.value)
    return { chats, AddChat, getChats }
  }, 
  {
    persist: {
      storage: piniaPluginPersistedstate.sessionStorage(),
      pick: ['chats']
    },
  }
)