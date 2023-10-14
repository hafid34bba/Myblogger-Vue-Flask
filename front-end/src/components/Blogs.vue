<template lang="">
  <div>
    <b-container class="custom-container">
      <b-row class="custom-row"> <h2>All Blogs</h2> </b-row>

      <b-row class="custom-row">
        <b-input-group size="lg">
          <b-form-input placeholder="Entrer blog name"></b-form-input>
        </b-input-group>
      </b-row>

      <b-row v-for="(blog, index) in blogs" :key="index" class="custom-row">


        <b-jumbotron
          class="jumbotron-custom"
          :header="blog.title"
          :lead="truncateContent(blog)"
        >
          <b-button @click="toggleContent(blog, index)" v-if="!blog.showFullContent" variant="dark" >
            More Info
          </b-button>
          <b-button @click="toggleContent(blog, index)" v-else variant="dark" >
            Show less
          </b-button>

        </b-jumbotron>
      </b-row>


    </b-container>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "blogs-component",

  data() {
    return {
      blogs: [],
      maxContentLength: 50,
    };
  },

  methods: {
    get_blogs() {
      const path = "/api/blogs";
      axios
        .get(path)
        .then((resp) => {
          this.blogs = resp.data.blogs.map((blog) => {
            return {
              ...blog,
              showFullContent: false, // Ensure showFullContent is properly initialized
            };
          });


          console.log(this.blogs);
        })
        .catch((err) => {
          console.error(err);
        });
    },

    truncateContent(blog) {
      console.log("truncate called", blog);
      if (blog.showFullContent) {
        return blog.Contenu;
      }
      return `${blog.Contenu.slice(0, this.maxContentLength)}...`;
    },
    toggleContent(blog, index) {
        console.log(this.blogs[index].showFullContent, index);

        
        blog.showFullContent = ! blog.showFullContent

        this.blogs[index] = blog
        
        console.log(this.blogs[index].showFullContent);

    
        
        
     
    },
  },
  created() {
    this.get_blogs();
  },
};
</script>

<style scoped>


.custom-row {
  margin: 15px;
  text-align: left;
  padding-left: 5px;
}

.jumbotron-custom {
  /* margin: 60px; */
  background-color: rgb(213, 225, 226);
  width: 100%;
  padding-bottom: 10px;
}
</style>
