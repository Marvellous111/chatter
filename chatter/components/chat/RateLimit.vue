<script lang="ts" setup>
var rate = 10;
</script>

<template>
  <div class="rate-limit-container">
    <span class="rate-limit-text geist-regular">You have <text class="geist-medium"> {{ rate }} </text> messages left <NuxtLink to="/auth" class="rate-limit-strong geist-medium">Sign in</NuxtLink> to increase the message limit</span>
  </div>
</template>

<style lang="scss" scoped>
.rate-limit-container {
  display: flex;
  align-items: center;
  justify-content: left;
  background: #FEE2E2;
  border: 1px solid #B91C1C;
  color: #7F1D1D;
  border-radius: 5px;
  width: stretch;
  height: 32px;
  padding: 5px 10px;
  column-gap: 10px;
  .rate-limit-text {
    margin-left: 5px;
    font-size: 14px;
    .rate-limit-strong {
      color: #7F1D1D;
    }
  }
}
</style>