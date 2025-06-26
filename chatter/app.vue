<script lang="ts" setup>
import { onMounted, ref } from "vue"

var uuid = ref<string|null>(null);

const generateUUID = async () => {
  if (localStorage.getItem("chatter_uuid")) {
    console.log("Local storage already set")
    return
  }
  try {
    const response = await fetch('/api/generate-uuid', {
      method: 'GET',
    })
    if (!response.ok) {
      console.log("An error occured")
      return
    }
    
    const reader = response.body?.getReader();
    const decoder = new TextDecoder();
    if (reader) {
      const { done, value } = await reader!.read();
      const uuidchunk = decoder.decode(value)
      uuid.value = uuidchunk
    }
    if (uuid.value) {
      localStorage.setItem("chatter_uuid", uuid.value);
      console.log("Localstorage uuid set")
    } else {
      console.log("Localstorage cannot be set")
      return
    }
  }catch(error) {
    console.log(error)
  }
}

onMounted(() => {
  if (!localStorage.getItem("chatter_uuid")) {
    console.log("Generating uuid")
    generateUUID()
  }
})
</script>

<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>
