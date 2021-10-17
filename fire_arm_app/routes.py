from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
# from models import Shooter
# from models.Shooter import Shooter, app

app = Flask(__name__)
app.secret_key = 'hello'
# # dictionary that accept new key values from me   --name of table--.db??
# app.config['SQLALCHEMy_DATABASE_URI'] = 'sqlite:///gun_profile.sqlite3'
app.config['SQLALCHEMy_DATABASE_URI'] = 'sqlite:///gun_profile.db'

# make it so were not tracking modifications to the db
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Shooter(db.Model):
    _id = db.Column("id", db.Integer(),primary_key=True)
    First_Name = db.Column(db.String(length=30), nullable=False)
    Last_Name = db.Column(db.Integer(),nullable=False)
    FireArm_Preference = db.Column(db.String(length=50), nullable=True)
    Description = db.Column(db.String(length=200), nullable=True)

    def __init__(self, First_Name, Last_Name, FireArm_Preference, Description):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.FireArm_Preference = FireArm_Preference
        self.Description = Description

@app.route('/')
def index():
    return '<h1>this is index page! go to /register</h1>'

@app.route('/register')
def register():
    print("*******we are in the register page**********")
    # if 'users' in session:
    #     print("===we have users in session===")
    #     return redirect(url_for('show_shooters'))
    return render_template("Register.html")


@app.route('/shooters', methods=['POST', 'GET'])
def show_shooters():
    print("*******we are in the show_user_profile page**********")
    if request.method == 'POST':
        shooter = Shooter(First_Name=request.form['Fname'],
                                Last_Name=request.form['Lname'],
                                FireArm_Preference=request.form['Gpreference'],
                                Description=request.form['Desc']
                                )
        shooters = Shooter.query.all()
        # pushing to db
        db.session.add(shooter)
        db.session.commit()
        print(shooters)
        return render_template("Shooters.html", shooters=shooters)
    else:
        shooters = Shooter.query.all()
        return render_template("Shooters.html", shooters=shooters)

@app.route('/shooter_profile')
def shooter_profile():
    # if request.method == 'POST':
        # shooter = Shooter(First_Name=request.form['Fname'],
        #                         Last_Name=request.form['Lname'],
        #                         FireArm_Preference=request.form['Gpreference'],
        #                         Description=request.form['Desc']
        #                         )
        return render_template('Shooter_Profile.html')

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


# LOGOUT USER
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
    #creates the db if itdoes not exist
    db.create_all()
    app.run(debug = True)