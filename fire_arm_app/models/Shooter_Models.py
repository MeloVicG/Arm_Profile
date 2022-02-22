# from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from api import db
from api import create_app, db
# db = create_app().db
app = create_app()

# app = Flask(__name__) # app here goes with model - no longer needed in app
# app.config['SECRET_KEY'] = "SECRET_KEY"
    
# # dictionary that accept new key values from me   --name of table--.db??
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gun_profile.sqlite3'
# app.config['SQLALCHEMY_ECHO'] = True

# make it so were not tracking modifications to the db
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# this is also takes care of our declaritive base and session -Megan Amendola (youtube)
# https://www.youtube.com/watch?v=hek9vsW8oKs&ab_channel=Treehouse
# db = SQLAlchemy(app)



class Shooter(db.Model):
    # __table__ = "user" # we dont have to do this is flask sqlalchemy

    _id = db.Column("id", db.Integer(),primary_key=True)
    first_name = db.Column(db.String(length=30), nullable=False)
    last_name = db.Column(db.Integer(),nullable=False)
    firearm_preference = db.Column(db.String(length=50), nullable=True)
    description = db.Column(db.String(length=200), nullable=True)
    # FireArms = relationship("FireArm", backref="shooters")

    def __init__(self, first_name, last_name, firearm_preference, description):
        self.first_name = first_name
        self.last_name = last_name
        self.firearm_preference = firearm_preference
        self.description = description


class FireArm(db.Model):
    _id = db.Column("id", db.Integer(),primary_key=True)
    gun_type = db.Column(db.String(length=50), nullable=False)
    gun_name = db.Column(db.String(length=50), nullable=False)
    gun_parts = db.Column(db.String(length=50), nullable=True)
    gun_bullet_type = db.Column(db.String(length=100), nullable=True)
    gun_description = db.Column(db.String(length=100), nullable=True)
    # Shooters = relationship("Shooters", backref='fiream_preference')
    
    def __init__(self, gun_type, gun_name, gun_parts, gun_bullet_type, gun_description):
        self.gun_type = gun_type
        self.gun_name = gun_name
        self.gun_parts = gun_parts
        self.gun_bullet_type = gun_bullet_type
        self.gun_description = gun_description


class Parts(db.Model):
    _id = db.Column("id", db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    # FireArm = db.Column(db.String(length=50), relationship('FireArm',
    #                                         backref('parts'), nullable=False))

    def __init__(self, _id, name, FireArm):
        self._id = _id
        self.name = name
        # self.FireArm = FireArm


