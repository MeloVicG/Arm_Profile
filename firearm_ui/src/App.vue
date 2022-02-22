<template>
  <div id="nav">
    <router-link to="/KumaArms/register">Home</router-link> |
    <router-link to="/KumaArms/guns_list">List of Guns</router-link> |
    <router-link to="/KumaArms/shooters">Shooters</router-link>
  </div>
  <router-view/>
</template> 





<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
  margin: 5% 30%;
  background: black;
  opacity: 90%;
}

#nav a {
  font-weight: bold;
  color: white;
}

#nav a.router-link-exact-active {
  color: yellow;
}
</style>
