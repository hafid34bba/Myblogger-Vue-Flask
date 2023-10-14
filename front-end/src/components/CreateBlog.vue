<template lang="">
  <div>
    <b-container class="custom-container">
      <b-form @submit="onSubmit" @reset="onReset">
        <b-row class="custom-row" > <h2 class="custom-text" style= "margin-top:20px;">Add Blog</h2> </b-row>
        <b-row> <b-alert variant="success" v-if="showMessage" show> {{ message }} </b-alert>
 </b-row>
        <b-row class="custom-row">
          <b-input
            v-model="blog.title"
            placeholder="Entrer titre" required
          ></b-input>
        </b-row>

        <b-row class="custom-row">
          <b-form-textarea
            id="textarea"
            v-model="blog.Contenu"
            placeholder="Entrer text"
            rows="3"
            max-rows="6" required
          ></b-form-textarea>
        </b-row>

        <b-row class="custom-row">
          <b-button @click="onSubmit"
          type="submit"
            variant="success"
            style="width: 100px; margin-right: 10px"
            href="#"
            >Submit</b-button
          >
          <b-button @click="onReset" type="reset" variant="danger" style="width: 100px" href="#"
            >Reset</b-button
          >
        </b-row>
      </b-form>
    </b-container>
  </div>
</template>
<script>
import axios from 'axios'
export default {

  name: "create-blog-component",
  data() {
    return {
      blog: {
        title: "",
        Contenu: "",
      },
      showMessage : false,
      message : ""
    };
  },

  methods: {
    init_form() {
        console.log("init");
        this.blog.title= "Entrer un titre.";
        this.blog.Contenu= "Entrer le contenu de blog.";
        this.showMessage = false;
        this.message = "";
        console.log(this.blog)
    },

    add_blog(blog) {
      const path = "/api/create_blog"
      axios
        .post(path, blog)
        .then((resp) => {
          this.blogs = resp.data.blogs;
          console.log(this.blogs);
          this.showMessage = true;
          this.message = this.blog.title + " added successfully"
        })
        .catch((err) => {
          console.error(err);
        });
    
    
    },
    onSubmit(e) {
      e.preventDefault();
      this.add_blog(this.blog);
    },

    onReset(e) {
      e.preventDefault();
      console.log('reset');
      this.init_form();
    }


  },
}


</script>
<style>
.custom-row {
  margin: 10px;
}
.btn-success {
  width: 20px;
  flex-shrink: 0; /* Empêche le bouton de rétrécir */
  flex-grow: 0;
}
.custom-text {
    margin-top: 30px;
    text-align: left;
}
</style>
