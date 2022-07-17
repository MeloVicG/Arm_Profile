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
        h1#ShooterProfileTitle Hello Shooter {{this.shooters[4].first_name}}
        form.action("shooters")
            button DashBoard
            .top-wrapper
            img(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6ygxqVtrly1VlqB7mCiDuWky9eSpJLru3nQ&usqp=CAU" alt="sexy shooter girl")
            h2 {{this.shooters.first_name}} 
        .mid-wrapper
            img(src="https://www.mcmillanfirearms.com/images/MCMILLAN%20PHOTOS/RIFLE%20PHOTOS/TAC-50C.JPG" alt="mcmillan tac-50C")
            h2 {{this.shooters.firearm_preference}}
        .bot-wrapper
            h2 {{this.shooters.description}}

</template>

<script>

import axios from "axios"
export default {
    name: 'ShooterProfile',
    data(){
        return{
            shooters:[],
        }
    },

    methods:{
        getShooters(){
            axios.get('http://127.0.0.1:5000/KumaArms/shooters')
                .then(res => {
                    this.shooters = res.data
                    console.log(res.data);
                })
                .catch(err =>{
                    console.log(err);
                })
            }
        },

    created(){
        this.getShooters()
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