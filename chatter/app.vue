<script lang="ts" setup>
import { onMounted } from "vue"

var uuid = "";

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
    console.log(`Response is: ${reader}`)
    const decoder = new TextDecoder();
    if (reader) {
      const { done, value } = await reader!.read();
      const uuidchunk = decoder.decode(value)
      uuid = uuidchunk
    }
    console.log(uuid)
    localStorage.setItem("chatter_uuid", uuid);
    console.log("Localstorage uuid set")
  }catch(error) {
    console.log(error)
  }
}

onMounted(() => {
  generateUUID()
})
</script>

<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>
