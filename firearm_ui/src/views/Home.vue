<template>
  <div class="home">
    <Register msg="Welcome to Your Vue.js App"/>
    <Guns_List/>
  </div>
</template>

<script>
// @ is an alias to /src
import Register from '@/components/Register.vue'

export default {
  name: 'Home',
  components: {
    Register
  }
}
</script>
