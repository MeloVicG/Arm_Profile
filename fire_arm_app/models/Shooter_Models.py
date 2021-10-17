from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, relationship
app = Flask(__name__)
# app.secret_key = 'hello'
# # dictionary that accept new key values from me   --name of table--.db??
# app.config['SQLALCHEMy_DATABASE_URI'] = 'sqlite:///gun_profile.sqlite3'
# app.config['SQLALCHEMy_DATABASE_URI'] = 'sqlite:///gun_profile.db'

# make it so were not tracking modifications to the db
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Shooter(db.Model):
    _id = db.Column("id", db.Integer(), primary_key=True)
    First_Name = db.Column(db.String(length=30), nullable=False)
    Last_Name = db.Column(db.Integer(), nullable=False)
    FireArm_Preference = db.Column(db.String(length=50), nullable=True)
    Description = db.Column(db.String(length=200), nullable=True)

    def __init__(self, _id, First_Name, Last_Name, FireArm_Preference, Description):
        self._id = _id
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.FireArm_Preference = FireArm_Preference
        self.Description = Description


class FireArm(db.Model):
    _id = db.Column("id",db.Integer(), primary_key=True)
    Name = db.Column(db.String(length=50), nullable=False)
    Type = db.Column(db.String(length=50), nullable=False)
    Owner = db.Column(db.String(length=100), relationship("Shooter",
                                            backref('firearm'), nullable=True))

    def __init__(self, _id, Name, Type, Owner):
        self._id = _id
        self.Name = Name
        self.Type = Type
        self.Owner = Owner


class Parts(db.Model):
    _id = db.Column("id", db.Integer(), primary_key=True)
    Name = db.Column(db.String(length=50), nullable=False)
    FireArm = db.Column(db.String(length=50), relationship('FireArm',
                                            backref('parts'), nullable=False))

    def __init__(self, _id, Name, FireArm):
        self._id = _id
        self.Name = Name
        self.FireArm = FireArm


