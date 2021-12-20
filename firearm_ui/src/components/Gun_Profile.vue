<template lang="pug">
head
    //- //- meta(charset="UTF-8")
    //- //- meta(http-equiv="X-UA-Compatible" content="IE=edge")
    //- //- meta(name="viewport" content="width=device-width, initial-scale=1.0")
    //- link rel="stylesheet" href="../static/GunProfileStyle.css"
    //- title Gun Profile

body
    .container
        .GunTitle
            h1 Gun Profile Page
        form(action="/shooters")
        button Go Back
        .mid-wrapper
            h1(style="color:white") {{pistol.gun_name}}
            .mid-mid-wrapper
                img(src="https://i.pinimg.com/originals/35/62/0a/35620a365890fd496f5ed9efe874723f.jpg" alt="pistol prints")
                h2(style="color:white") description here
        
</template>