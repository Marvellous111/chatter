export default defineNuxtRouteMiddleware(from => {
  const chatter_uuid = localStorage.getItem("CHATTER_UUID");
  if (!chatter_uuid) {
    console.log("Chatter uuid is not set yet, cannot process any important request");
    return
  }
})