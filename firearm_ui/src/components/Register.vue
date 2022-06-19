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
      //- form( action=createShooters() method='POST' ) 
      //- form( @submit.preventDefault="onSubmit" method='POST' ) 
      form( @submit.preventDefault="onSubmit" ) 
        //- TODO need to fix this to localhost: 500 
        div
          input(placeholder="First Name" v-model="addShooterForm.first_name" name="Fname" class="form-control" type="text")
          | message is: {{addShooterForm.first_name}}
        div  
          input(placeholder="Last Name" v-model="addShooterForm.last_name" name="Lname" class="form-control" type="text")
        div  
          input(placeholder="Fire Arm Preference" v-model="addShooterForm.FireArm" name="Gpreference" class="form-control" type="text")
        div  
          input(placeholder="Description" v-model="addShooterForm.Description" name="Desc" class="form-control" type="text")
        div  
          input(type="submit")
      button(@click="getShooters()") show list of shooters

</template>


<script>
import axios from 'axios'
export default {
  name: 'Register',
  props: {
    msg: String
  },

  data(){
    return {
      shooters: [],
      addShooterForm:{
        first_name:"",
        Last_name:"",
        FireArm:"",
        Description:"",
      }
    };
  },

// when the DOM (template is loaded) mounted() will attach itself to the DOM and load the method
  // mounted(){
    // axios.get('http://127.0.0.1:5000/KumaArms/shooters')
    //   .then(res => {
    //     this.shooters = res.data
    //     console.log(res);
    //   })
    //   .catch(err =>{
    //       console.log("you have an error", err);
    // })
  // },


  methods:{

    getShooters(){
      axios.get('http://127.0.0.1:5000/KumaArms/shooters')
      .then(res => {
          console.log('list of shooters',res.data);
      })
      .catch(err =>{
          console.log("you have an error", err);
      })
    },


    // TODO PROBLEM IS SENDING 2 api requests need to figure out how to redirect
    // 6/7/2022
    createShooter(payload){ // parameter is automatic?
      axios.post('http://127.0.0.1:5000/KumaArms/create_shooter', payload) //THIS SENDS AS A application/json
      .then(() => {
        // console.log("this is the payload: ", payload);
        this.getShooters()
        // this.shooters = [...payload]
        // console.log('Shooters AFTER------',this.shooters);

      })
      .catch(err =>{
        console.log(err);
        this.getShooters()
      })
    },

    initForm(){ // changes form back to original.
      console.log("this is init------ ")
      console.log("changed back to '' ")
      // console.log("this is the payload: ", payload)
      this.addShooterForm.first_name = "",
      this.addShooterForm.Last_name = "",
      this.addShooterForm.FireArm = "",
      this.addShooterForm.Description = ""
      },

    // onSubmit(){
    onSubmit(){
      // e.preventDefault();
      const payload = {
        first_name: this.addShooterForm.first_name,
        last_name: this.addShooterForm.last_name,
        fire_arm: this.addShooterForm.FireArm,
        description: this.addShooterForm.Description 
      }
      this.createShooter(payload);
      this.initForm;
      this.$router.push('/KumaArms/shooters')
    }
  }, // this is methods

  // this is similar to mounted???
  created(){
    this.getShooters()
  }

} // this is export default
// TODO need to redirect to html with the data fetched from backend 4/17/22
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
