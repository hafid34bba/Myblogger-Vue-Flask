<template>
  <div id="app">
    <nav>
      <router-link to="/blog">Blogs</router-link>
      <router-link to="/blog_create">CreateBlog</router-link> 
      
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
  background-color: black;
}

nav a {
  font-weight: bold;
  /* color: #2c3e50; */
  color: white;
  

  padding: 10px;

}

nav a.router-link-exact-active {
  background-color: white;
  color: black;
}


</style>
