<template lang="pug">
head
    meta(charset="UTF-8")
    meta(http-equiv="X-UA-Compatible" content="IE=edge")
    meta(name="viewport" content="width=device-width, initial-scale=1.0")
    link(rel="stylesheet" href="../static/ShooterProfileStyle.css")
    link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous")
    title Document
body
    #container
    div(v-if="shooter_id") this works properly {{$route.params._id}}
        h1#ShooterProfileTitle Hello Shooter {{this.shooter_id._id}} / {{this.shooter_id}} / {{_id}}
        form.action(@click.preventDefault="shooters")
            //- button(@click="onSubmit()") DashBoard
            button DASHBOARD
            input(type="submit")
        .top-wrapper
        img(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6ygxqVtrly1VlqB7mCiDuWky9eSpJLru3nQ&usqp=CAU" alt="sexy shooter girl")
        h2 {{this.shooter_id.first_name}} 
        .mid-wrapper
            img(src="https://www.mcmillanfirearms.com/images/MCMILLAN%20PHOTOS/RIFLE%20PHOTOS/TAC-50C.JPG" alt="mcmillan tac-50C")
            h2 {{this.shooter_id.firearm_preference}}
        .bot-wrapper
            h2 {{this.shooter_id.description}}

</template>

<script>

import axios from "axios"
export default {
    props:['_id'],    
    //data is not necessary if there is a props for data being passed down
    data(){
         return{
            shooter_id: this.$route.params._id // returns id from params
         }
    },


    mounted(){
        axios.get('http://127.0.0.1:5000/KumaArms/shooter_profile/' + this._id)
            .then(console.log('THIS IS ID!!',this._id))
            .then(res => console.log('THIS IS RESPONSE',res))
            .catch(err => console.log('you have an error: ', err.message))
        
    },

    onSubmit(){
    //   e.preventDefault();
      this.$router.push('/KumaArms/shooters')
    }


} //export default


</script>




<style scoped> 
/* @import "../node_modules/bootstrap/dist/css/bootstrap"; */

.ShootersTitle{
            font-family: 'Modak', cursive;
            text-align: center;
            color:bisque;
            font-size: 50px;
            padding: 20px;
            -webkit-text-stroke: 3px black;
            text-shadow: 4px 4px black;
            background:rgb(37,38,43, 0.9);
        }

.tablecolor{
    color:black
}

</style>