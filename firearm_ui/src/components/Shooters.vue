<template lang="pug">
body
    .container
        table.table-dark.table-hover
            h1#ShootersTitle Shooters Table  
            thead
                tr.table-secondary
                    th First Name
                    th Last Name
                    th FireArm Preference
                    th Description
                    th Action
                form.action("/logout")
                    button.logoutButton Register A Shooter
                    
            tbody
                | {% for shooter in shooters %}
                tr
                    td.a( href=url_for('shooter_profile', id=shooter._id,) ) {{ shooter.first_name }}
                    td {{ shooter.last_name }}
                    td.a( href=url_for('gun_profile', id=shooter._id, ) ) {{ shooter.firearm_preference }}
                    td {{ shooter.description }}
                    //- <!-- <form action="/delete/<int:id>"></form> -->
                        <!-- delete button -->
                    //- form.action( url_for('delete_shooter', id=shooter._id) method='POST')
                    //-     td.button Delete
                //- {% endfor %}
</template>