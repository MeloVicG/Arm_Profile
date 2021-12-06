from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker

from models.Shooter_Models import app, db, Shooter, FireArm, Parts

# Base = declarative_base() # TODO what does this do?? -binds to a model

# engine = create_engine("postgresql://vic:gar@localhost/gun_profile")
# connection = engine.connect()

#-----------------------------------------------------------------------------------------------    
#-----------------------------------------------------------------------------------------------    
@app.route('/')
def index():
    return '<h1>this is index page! go to /register</h1>'

@app.route('/register')
def register():
    print("*******we are in the register page**********")
    return render_template("Register.html")


@app.route('/shooters', methods=['POST', 'GET'])
def show_shooters():
    print("*******we are in the show all shooters page**********")
    if request.method == 'POST':
        # adding from form into db
        shooter = Shooter(First_Name=request.form['Fname'],
                        Last_Name=request.form['Lname'],
                        FireArm_Preference=request.form['Gpreference'],
                        Description=request.form['Desc']
                        )
        shooters = Shooter.query.all()
        db.session.add(shooter)
        db.session.commit()
        return render_template("Shooters.html", shooters=shooters)
    else:
        shooters = Shooter.query.all()
        return render_template("Shooters.html", shooters=shooters)

#----------------------------------------------------------------------------------------

# SELECTED SHOOTER PROFILE
@app.route('/shooter_profile/<int:id>')
def shooter_profile(id):
    selected_shooter = Shooter.query.get(id)
    return render_template('Shooter_Profile.html', selected_shooter=selected_shooter)

#----------------------------------------------------------------------------------------

# SELECTED FIREARM PROFILE
@app.route('/Fire-Arm_profile/<int:id>')
def gun_profile(id):
    pistol = FireArm(
                                    Gun_Type = "Pistol", 
                                    Gun_Name = "Ebony & Ivory", 
                                    Gun_Parts = "gun parts here", 
                                    Gun_Bullet_Type = "Bullet types here", 
                                    Gun_Description = "Dantes Favorite Guns"
                                    )
    selected_firearm = FireArm.query.get(id)
    return render_template('Gun_Profile.html', selected_firearm=selected_firearm, pistol=pistol)


#----------------------------------------------------------------------------------------

# DELETE SHOOTER
@app.route('/delete/<int:id>', methods=['GET','POST'])
def delete_shooter(id):
    print("==========Deleting Shooter===========")
    if request.method == 'POST':
        shooter_to_delete = Shooter.query.get_or_404(id)
        try:
            db.session.delete(shooter_to_delete)
            db.session.commit()
            print("shooter has been deleted id:", id)
            return redirect('/shooters')
        except:
            print('delete shooter error')
            return redirect('/shooters')
    else:
        return redirect(url_for('show_shooters'))


#----------------------------------------------------------------------------------------

# LOGOUT USER *same as register shooter
@app.route('/logout')
def logout():
    print("**************users have been deleted*****************")
    session.pop("users", None)
    print("**************returning to register page*****************")
    return redirect(url_for('register'))

# reads function but not sure how it does
# with app.request_context(environ):
#     assert request.method == "POST"


if __name__== "__main__":
    #creates the db if it does not exist
    db.create_all()
    app.run(debug = True)