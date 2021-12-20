<template lang="pug">
.container
  h1.RegisterTitle Register Page
  .RegisterForm.form(action="/shooters" method='POST')
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
      | have to use wsgi to connect backend and frontend
    
</template>


<script>
export default {
  name: 'Register',
  props: {
    msg: String
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

    min-height: 500px;
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}

    .container{
    align-items: center;  
    padding: 50px;
    width: 50%;
    }

        .RegisterForm{
            background:rgb(37,38,43, 0.9);
            padding: 50px;
        }
        .RegisterTitle{
            font-family: 'Modak', cursive;
            text-align: center;
            color:bisque;
            font-size: 50px;
            padding: 0px 20px;
            -webkit-text-stroke: 3px black;
            text-shadow: 4px 4px black;
            background:rgb(37,38,43, 0.9);
        }
</style>
