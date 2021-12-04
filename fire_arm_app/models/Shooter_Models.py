from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, relationship
from sqlalchemy import create_engine

app = Flask(__name__)
app.secret_key = 'hello'

engine = create_engine("sqlite:///gun_profile.db",
                            encoding='latin1', echo=True)
# engine = create_engine("postgresql://vic:gar@localhost/gun_profile")
connection = engine.connect()

# checks the engine
# from pdb import set_trace; set_trace()
# print(engine.table_names())

# # dictionary that accept new key values from me   --name of table--.db??
# app.config['SQLALCHEMy_DATABASE_URI'] = 'sqlite:///gun_profile.sqlite3'
# app.config['SQLALCHEMy_DATABASE_UexRI'] = 'sqlite:///gun_profile.db'

# make it so were not tracking modifications to the db
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Shooter(db.Model):
    _id = db.Column("id", db.Integer(),primary_key=True)
    First_Name = db.Column(db.String(length=30), nullable=False)
    Last_Name = db.Column(db.Integer(),nullable=False)
    FireArm_Preference = db.Column(db.String(length=50), nullable=True)
    Description = db.Column(db.String(length=200), nullable=True)
    # FireArms = relationship("FireArm", backref="shooters")

    def __init__(self, First_Name, Last_Name, FireArm_Preference, Description):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.FireArm_Preference = FireArm_Preference
        self.Description = Description


class FireArm(db.Model):
    _id = db.Column("id", db.Integer(),primary_key=True)
    Gun_Type = db.Column(db.String(length=50), nullable=False)
    Gun_Name = db.Column(db.String(length=50), nullable=False)
    Gun_Parts = db.Column(db.String(length=50), nullable=True)
    Gun_Bullet_Type = db.Column(db.String(length=100), nullable=True)
    Gun_Description = db.Column(db.String(length=100), nullable=True)
    # Shooters = relationship("Shooters", backref='fiream_preference')
    
    def __init__(self, Gun_Type, Gun_Name, Gun_Parts, Gun_Bullet_Type, Gun_Description):
        self.Gun_Type = Gun_Type
        self.Gun_Name = Gun_Name
        self.Gun_Parts = Gun_Parts
        self.Gun_Bullet_Type = Gun_Bullet_Type
        self.Gun_Description = Gun_Description


class Parts(db.Model):
    _id = db.Column("id", db.Integer(), primary_key=True)
    Name = db.Column(db.String(length=50), nullable=False)
    # FireArm = db.Column(db.String(length=50), relationship('FireArm',
    #                                         backref('parts'), nullable=False))

    def __init__(self, _id, Name, FireArm):
        self._id = _id
        self.Name = Name
        self.FireArm = FireArm


