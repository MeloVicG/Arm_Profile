from flask import Flask, render_template, request, redirect, url_for, session
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'hello'
# # dictionary that accept new key values from me
# app.config['SQLALCHEMy_DATABASE_URI'] = 'sqlite:///gun_profile.db'
# db = SQLAlchemy(app)

# class Item(db.model):
#     id = db.Column(db.Integer(),primary_key=True)
#     First_Name = db.Column(db.String(length=30), nullable=False)
#     Last_Name = db.Column(db.Integer(),nullable=False)
#     FireArm_Preference = db.Column(db.String(length=50), nullable=True)
#     Description = db.Column(db.String(length=200), nullable=True)

@app.route('/')
def index():
    return '<h1>this is index page! go to /register</h1>'

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        context = {'first_name': request.form['Fname'],
                   'last_name': request.form['Lname'],
                   'gun_preference': request.form['Gpreference'],
                   'description': request.form['Desc']}
        session["users"] = context
        return redirect(url_for('show_user_profile'))
    else:
        if 'user' in session:
            return redirect(url_for('show_user_profile'))
        return render_template("Register.html")

@app.route('/users')
def show_user_profile():
    if "users" in session:
        users = session["users"]
        print(users)
        return render_template("Users.html", users=users)
    else:
        print("failed session")
    return render_template("Users.html")

# reads function but not sure how it does
# with app.request_context(environ):
#     assert request.method == "POST"


if __name__== "__main__":
    app.run(debug = True)