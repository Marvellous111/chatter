<script lang="ts" setup>
definePageMeta({
  layout: 'backtochat'
})
</script>

<template>
  <body class="settings-body">
    <SettingsAccountInfo />
    <div class="subscription-container">
      Subscription
    </div>
  </body>
</template>

<style lang="scss" scoped>
.settings-body {
  width: stretch;
  height: stretch;
  display: flex;
  border: 1px solid white;
}
</style>