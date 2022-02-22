# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import backref, relationship

# # from routes import db, app

# # binds instance to flask app 
# app = Flask(__name__) # app here goes with model - no longer needed in app
# # app.secret_key = 'hello'
# app.config['SECRET_KEY'] = "SECRET_KEY"

# # engine = create_engine("postgresql://vic:gar@localhost.com/")
# # engine = create_engine("sqlite:///gun_profile.db",)

# # engine = create_engine("postgresql://vic:gar@localhost/gun_profile")
# # connection = engine.connect()
# # with Session() as session:
# #     session.add(Shooter)

# # checks the engine
# # from pdb import set_trace; set_trace()
# # print(engine.table_names())

# # # dictionary that accept new key values from me   --name of table--.db??
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gun_profile.sqlite3'
# # app.config['SQLALCHEMy_DATABASE_UexRI'] = 'sqlite:///gun_profile.db'
# app.config['SQLALCHEMY_ECHO'] = True

# # make it so were not tracking modifications to the db
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # this is also takes care of our declaritive base and session -Megan Amendola (youtube)
# db = SQLAlchemy(app) 

# # NOTES
# # notes for model eventually put in __init__

# # ----------------------------------------------------------------------------------------