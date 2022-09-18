<template lang="pug">
body
    button(@click="getShooters()") this to show list of shooters
    |
    |
    .container
        //- table.table-dark.table-hover
        //- this.shooter is not needed in the html
        h1.ShootersTitle Shooters Table  
        table.table.table-dark.table-striped
            thead
                tr.table-dark
                    th Id
                    th First Name
                    th Last Name
                    th FireArm Preference
                    th Description
                    th Action
            tbody
                tr(v-for="(shooter) in shooters" :key='shooter._id') 
                    td {{shooter._id}}
                    td {{shooter.first_name}}
                    td {{shooter.last_name}}
                    td {{shooter.firearm_preference}}
                    td {{shooter.description}}
                    button.btn.btn-danger(@click='deleteShooter(shooter._id)') Delete
                    //- CORRECT (not really)
                    //- button.btn.btn-info(@click="$router.push(`/KumaArms/shooter_profile/${shooter._id}`)") Edit
                    //- this is better
                    //- button.btn.btn-info(@click="$router.push({ name:'ShooterProfile', params:{id:shooter._id} })") Edit
                    //- TODO this is suppose to be correct
                    //- button.btn.btn-info.router-link(:to="{ name:'ShooterProfile', params:{_id:shooter._id} }") Edit
                    router-link.button.btn.btn-info(:to="{ name:'ShooterProfile', params:{_id:shooter._id} }") Edit
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
        },

        // editShooter(id){ // parameter is automatic?
        //     axios.put(`http://127.0.0.1:5000/KumaArms/edit/${id}` ) 
        //     .then(() => {
        //         this.getShooters()
        //     })
        //     .catch(err =>{
        //         console.log('this is your createShooter error: ',err);
        //         this.getShooters()
        //     })
        // },
        
        deleteShooter(id){ // parameter is automatic?
            axios.delete(`http://127.0.0.1:5000/KumaArms/delete/${id}`) 
            .then(() => {
                console.log(`Shooter has been ${id} deleted`)
                // this.$router.push('/KumaArms/shooters')
                this.$router.go()
            })
            .catch(err =>{
                console.log('deleteShooter error: ',err);
            });
        },

    },

    created(){
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