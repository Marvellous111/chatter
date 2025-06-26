import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAuthStore = defineStore(
  'authstore',
  () => {
    const user_uuid = ref<string|null>(null);
    const userData = ref<string|null>(null);
    // We want to save the user_uuid for redis.
    // Auth works by collecting the jwt token saved as something like this
    /*
    {
      "user_uuid": user_uuid,
      "username": username
      "password": password(hashed)
    } 
    The user uuid will be stored in the database and redis. bad advice to have this on uuid but it will do.
    */

    function saveUser(user_jwt_token: string) {
      userData.value = user_jwt_token
    }


    return { user_uuid, userData }
  },
  {
    persist: {
      storage: piniaPluginPersistedstate.cookies(
        {
          secure: true,
        }
      ),
      pick: ['userData', 'user_uuid']
    }
  },
)