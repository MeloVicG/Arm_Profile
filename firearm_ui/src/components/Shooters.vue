<template lang="pug">
body
    button(@click="getShooters()") this to show list of shooters
    |
    |
    div(style="color:white") fetching data is weird
    //- .container
    //-     table.table-dark.table-hover
    //-         h1#ShootersTitle Shooters Table  
    //-         thead
    //-             tr.table-secondary
    //-                 th First Name
    //-                 th Last Name
    //-                 th FireArm Preference
    //-                 th Description
    //-                 th Action
    //-             form.action("logout")
    //-                 button.logoutButton Register A Shooter
                    
    //-         tbody
    //-             .list_of_shooters(v-for="shooter in shotters", :key="shooter._id") 
    //-             //- :key="shooter._id"
    //-             //- | {% for shooter in shooters %}
    //-             tr
    //-                 //- td.a( href=url_for('shooter_profile', id=shooter._id,) ) {{ shooter.first_name }}
    //-                 //- td.router-link(:to="{ name:"ShooterProfile" , params: {id:shooter._id}}")
    //-                 td {{ shooter.last_name }}
    //-                 //- td.a( href=url_for('gun_profile', id=shooter._id, ) ) {{ shooter.firearm_preference }}
    //-                 td {{ shooter.description }}
    //-                 //- <!-- <form action="/delete/<int:id>"></form> -->
    //-                     //- <!-- delete button -->
    //-                 //- form.action( url_for('delete_shooter', id=shooter._id) method='POST')
    //-                     td.button Delete
    //-         div 
    //-             | sadsasdsddkjslkakslkfsldfsldkfjslkjflsdkjf
                //- {% endfor %}
</template>

<script>
import axios from "axios"
export default {
    name: 'Shooters',
    data(){
        return{
            shotters:[],
        }
    },
    
    methods:{
        getShooters(){
            axios.get('http://127.0.0.1:5000/KumaArms/shooters')
            .then(res => {
                console.log("this is the response: ", res);
                // console.log(res.data);
                // this.shotters = res.data
                // this.shotters.push(...data)
            })
            .catch(err =>{
                console.log(err);
            })
        }
    }
    // methods:{
    //     getShooters(){
    //         fetch('http://localhost:5000/KumaArms/shooters', {
    //             method:'GET',
    //             // headers:{
    //             //     "Content-Type":"application/json"
    //             // }
    //         })
    //         .then(res => res.json())
    //         .then(data => {
    //             console.log("this is the data!!", data);
    //             this.shotters.push(...data)
    //         })
    //         .catch(error => {
    //             console.log("this is the error!!: ",error);
    //         })
    //     }
    // },
    // mounted(){
    //     fetch('http://localhost:5000/KumaArms/shooters')
    //     .then(res => res.json())
    //     .then(data => this.shotters = data)
    //     .catch(error => console.log("this is catch error: ", error))
    // }
    // created(){
    //     axios.get('http://localhost:5000/KumaArms/shooters')
    //     .then(res => ("this is the res.json", res.json))
    //     .then(data => this.shotters = data)
    //     .catch(err => console.log("this is the error", err))
    // }
}
</script>
