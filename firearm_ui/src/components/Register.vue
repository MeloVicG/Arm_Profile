<template lang="pug">
head
    meta(charset="UTF-8")
    meta(http-equiv="X-UA-Compatible" content="IE=edge")
    meta(name="viewport" content="width=device-width, initial-scale=1.0")
    title Document
    link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous")
    link(rel="stylesheet" href="static/RegisterStyle.css")
    link(href="https://fonts.googleapis.com/css2?family=Modak&display=swap" rel="stylesheet")
body
  .container
    h1.RegisterTitle Register Page
    .RegisterForm
      form( action="shooters" method='POST' ) 
        div
          input(placeholder="First Name" name="Fname" class="form-control" type="text")
        div  
          input(placeholder="Last Name" name="Lname" class="form-control" type="text")
        div  
          input(placeholder="Fire Arm Preference" name="Gpreference" class="form-control" type="text")
        div  
          input(placeholder="Description" name="Desc" class="form-control" type="text")
        div  
          input(type="submit")
        div
          | fix _id connection to back
    
</template>


<script>
export default {
  name: 'Register',
  props: {
    msg: String
  },

  methods:{
    submit(){
      // this.$axios.defaults.baseURL = process.env.VUE_APP_AUTHENTICATION_URL
      location.reload()
    }
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
body {
    margin: 0px;
    padding: 0px;
    background: url("https://images.fineartamerica.com/images/artworkimages/mediumlarge/3/firearm-blueprints-denny-h.jpg");
    /* background-repeat: none; */
    /* background-size: 100%; */
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}

    .container{
    align-items: center;  
    /* padding: 10px; */
    /* width: 50%; */
    }

        .RegisterForm{
            background:rgb(37,38,43, 0.9);
            padding: 5% 25%;
            color:white;
        }
        .RegisterTitle{
            font-family: 'Modak', cursive;
            text-align: center;
            color:bisque;
            font-size: 50px;
            padding: 20px;
            -webkit-text-stroke: 3px black;
            text-shadow: 4px 4px black;
            background:rgb(37,38,43, 0.9);
        }
</style>
