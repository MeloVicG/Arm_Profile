<template lang="pug">
head
    meta(charset="UTF-8")
    meta(http-equiv="X-UA-Compatible" content="IE=edge")
    meta(name="viewport" content="width=device-width, initial-scale=1.0")
    link(rel="stylesheet" href="../static/ShooterProfileStyle.css")
    link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous")
    title Document
</head>
body
    #container
        h1#ShooterProfileTitle Hello Shooter {{selected_shooter.first_name}} {{selected_shooter.last_name}}
        form.action("/shooters")
            button DashBoard
            .top-wrapper
            img(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6ygxqVtrly1VlqB7mCiDuWky9eSpJLru3nQ&usqp=CAU" alt="sexy shooter girl")
            h2 {{selected_shooter.first_name}} 
        .mid-wrapper
            img(src="https://www.mcmillanfirearms.com/images/MCMILLAN%20PHOTOS/RIFLE%20PHOTOS/TAC-50C.JPG" alt="mcmillan tac-50C")
            h2 {{selected_shooter.firearm_preference}}
        .bot-wrapper
            h2 {{selected_shooter.description}}

</template>