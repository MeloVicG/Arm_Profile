<template lang="pug">
//- link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous")
//- link(type="text/css" rel="stylesheet" href="https://unpkg.com/bootstrap/dist/css/bootstrap.min.css")
//- link(type="text/css" rel="stylesheet" href="https://unpkg.com/bootstrap-vue@latest/dist/bootstrap-vue.min.css")
//- script(src="https://unpkg.com/vue@latest/dist/vue.min.js")
//- script(src="https://unpkg.com/bootstrap-vue@latest/dist/bootstrap-vue.min.js")
//- script(src="https://unpkg.com/bootstrap-vue@latest/dist/bootstrap-vue-icons.min.js")

body
    button(@click="getShooters()") this to show list of shooters
    |
    |
    .container
        //- table.table-dark.table-hover
        h1.ShootersTitle Shooters Table  
        table.table.table-dark.table-striped
            thead
                tr.table-dark
                    th Id
                    th First Name
                    th Last Name
                    th FireArm Preference
                    th Description
            tbody
                tr(v-for="shooter, _id in getShooters()" :key="shooter._id")
                    td {{shooter._id}}
                    td {{shooter.first_name}}
                    td {{shooter.last_name}}
                    td {{shooter.firearm_preference}}
                    td {{shooter.description}}
                        //- td.a( href=url_for('KumaArms/shooter_profile', id=shooter._id,) ) {{ shooter.first_name }}
                    //- td.router-link(:to="{ name:"ShooterProfile" , params: {id:shooter._id}}")
                    //- <!-- <form action="/delete/<int:id>"></form> -->
                        //- <!-- delete button -->
                    //- form.action( url_for('delete_shooter', id=shooter._id) method='POST')
                        td.button Delete

</template>

<script>

import axios from "axios"
export default {
    name: 'Shooters',
    data(){
        return{
            shooters:[],
        }
    },
    
//   mounted(){
//     axios.get('http://127.0.0.1:5000/KumaArms/shooters')
//         .then(res => {
//             this.shooters = res.data
//             // this.shooters.push(...res.data)
//             console.log(this.shooters);
//         })
//         .catch(err =>{
//             console.log("you have an error: ", err);
//         })
//   },

    methods:{
        getShooters(){
            axios.get('http://127.0.0.1:5000/KumaArms/shooters')
            .then(res => {
                this.shooters = res.data
                console.log("this is the response: ", res);
            })
            .catch(err =>{
                console.log(err);
            })
        }
    },

    created(){
        // axios.get('http://localhost:5000/KumaArms/shooters')
        // .then(res => ("this is the res.json", res.json))
        // .then(data => this.shotters = data)
        // .catch(err => console.log("this is the error", err))
        this.getShooters()
    }
    
} // export default


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