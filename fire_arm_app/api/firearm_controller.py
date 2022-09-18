from traceback import print_tb
from flask import Flask, \
                Blueprint, \
                render_template, \
                request, \
                redirect, url_for, session
# from flask_marshmallow import Marshmallow
from flask import jsonify, request
from marshmallow import ValidationError

from models.Shooter_Models import Shooter, FireArm, Parts, db, ShooterSchema, FireArmSchema
from api.utils import create_app
app = create_app() 
import json

# http://exploreflask.com/en/latest/blueprints.html
v1_firearm_profile_bp = Blueprint("v1_firearm_profile_bp", __name__, url_prefix="/KumaArms", static_folder="static")

#-----------------------------------------------------------------------------------------------    
#----------------------------------------------------------------------------------------

@v1_firearm_profile_bp.route('/shooters', methods=['GET'], endpoint=None)
def get_shooters():
    shooters_query = db.session.query(Shooter).all()
    print("******************  we are in the GET show all shooters page  **********************")
    # shooters = Shooter.query.all()
    # before marshmellow to receive json
    shooter_schema = ShooterSchema(many=True) # many=True - if multiple data show in list
    output = shooter_schema.dump(shooters_query)
    return jsonify(output)

#----------------------------------------------------------------------------------------
#               ✔✔✔✔✔✔✔✔ COMPLETE ✔✔✔✔✔✔✔✔
@v1_firearm_profile_bp.route('/create_shooter', methods=['POST'], endpoint=None )
def create_shooter():
    # shooters_query = db.session.query(Shooter).all()

    if request.method == "POST":
        print("*******we are in the POST create_shooter page**********")
        shooter_data = request.get_json() # an object
        print("|")

        # ADD to marshmellow after receiving Json
        try:
            shooter_created = ShooterSchema() # request.get_json()?? (many=True)
            shooter_schema = shooter_created.load(shooter_data) # request.get_json()
            print("|")
            db.session.add(shooter_schema)
            db.session.commit()
            print(f"{shooter_schema} added to db!")
            
            return ShooterSchema().dump(shooter_schema) #, many=True
        except ValidationError as e:
            print("WE HAVE A VALIDATION ERROR",)
            print(e)
            # print(e.messages)s
            # print(e.valid_data)

    else:
        print("request method is not POST")
        print("*************************************************************************")
        
#----------------------------------------------------------------------------------------

# SELECTED SHOOTER PROFILE
@v1_firearm_profile_bp.route('/shooter_profile/<int:id>')
def shooter_profile(id):
    selected_shooter = Shooter.query.get(id)
    return render_template('Shooter_Profile.html', selected_shooter=selected_shooter )
    # return url_for('v1_firearm_profile_bp.Shooter_Profile', filename='ShooterProfileStyle.css')

#----------------------------------------------------------------------------------------

# SELECTED FIREARM PROFILE 
@v1_firearm_profile_bp.route('/Fire-Arm_profile/<int:id>')
def gun_profile(id):
    pistol = FireArm(
                                    gun_type = "Pistol", 
                                    gun_name = "Ebony & Ivory", 
                                    gun_parts = "gun parts here", 
                                    gun_bullet_type = "Bullet types here", 
                                    gun_description = "Dantes Favorite Guns"
                                    )
    selected_firearm = FireArm.query.get(id)
    return render_template('Gun_Profile.html', selected_firearm=selected_firearm, pistol=pistol)

#----------------------------------------------------------------------------------------
# DELETE SHOOTER
@v1_firearm_profile_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_shooter(id):
    print("|")
    print("=========================== *Deleting Shooter* ====================")
    print("|")
    # =======================================================================================
    if request.method == 'DELETE':
        d_shooter = request.get_json
        shooter_schema = ShooterSchema(many=True) 
        # shooter_to_delete = Shooter.query.all()
        shooter_to_delete = Shooter.query.get(id)
        # output = shooter_schema.dump(shooter_to_delete)        

        try:
            if shooter_to_delete:
                print(shooter_to_delete, " has been removed")
                db.session.delete(shooter_to_delete)
                db.session.commit()
                print(f"shooter {shooter_to_delete.first_name} has been successfully deleted from DB")

            else:
                raise Exception("There is something wrong with the request")

        except ValidationError as e: # if there is a Validationerror show me what that error is
            print("!!!❌❌  WE HAVE A VALIDATION ERROR  ❌❌!!!",)
            print(e)
            print(e.messages)
            print(e.valid_data)
        print("|")
    # =======================================================================================
        print("*************************************************************************")
        return "we have successfully deleted shooter from the db"

    else:
        raise Exception("request is not DELETE error") 

#----------------------------------------------------------------------------------------
# EDIT SHOOTER
@v1_firearm_profile_bp.route('/edit/<int:id>', methods=['PUT'])
def edit_shooter(id):
    print('==============================================================')
    print('WE ARE IN THE EDIT_SHOOTER PAGE')
    if request.method == "PUT":
        put_shooter = request.get_json()
        shooter_edit = ShooterSchema()

        try:
            print("we are in try")
            print(shooter_edit.load(shooter_edit))
            shooter_schema = shooter_edit.load(shooter_edit)

            db.session.put(shooter_schema)
            db.session.commit()
            print("we are in try 2")

        except ValidationError as e:
            print("WE HAVE VALIDATION ERROR")
            print(e)

        print(":")
        print('==============================================================')
        return shooter_edit.dump(shooter_schema)
    else:
        print('error: type is not PUT:', request.content_type )



#----------------------------------------------------------------------------------------

# LOGOUT USER *same as register shooter
@v1_firearm_profile_bp.route('/logout')
def logout():
    print("**************users have been deleted*****************")
    session.pop("users", None)
    print("**************returning to register page*****************")
    return redirect(url_for('v1_firearm_profile_bp.register'))






# DONE 
# - able to successfully delete and refresh page.

# TODO
# - need to learn AJAX so I can refresh page without refreshing
# - create shooter is not working again because no positional arguement _id...
# -
# - Work on EDIT next
# -