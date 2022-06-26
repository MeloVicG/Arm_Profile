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

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gun_profile.sqlite3' # needs to go before SQLAlchemy()
# app.config['SECRET_KEY'] = "SECRET_KEY"
# app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Base = declarative_base() # TODO what does this do?? -binds to a model

# engine = create_engine("postgresql://vic:gar@localhost/gun_profile")
# connection = engine.connect()
# app = Flask(__name__) # app here goes with model - no longer needed in app
# CORS(create_app)
# db = SQLAlchemy(app) 

# http://exploreflask.com/en/latest/blueprints.html
v1_firearm_profile_bp = Blueprint("v1_firearm_profile_bp", __name__, url_prefix="/KumaArms", static_folder="static")

#-----------------------------------------------------------------------------------------------    
#-----------------------------------------------------------------------------------------------    

# @app.route('/')
# @v1_firearm_profile_bp.route('/')
# def index():
#     return '<h1>this is index page! go to /register</h1>'

# @v1_firearm_profile_bp.route('/register')
# def register():
#     print("*******we are in the register page**********")
#     return render_template("Register.html")

#----------------------------------------------------------------------------------------

# TODO Have to create 2 separate routes for POST & GET
#   one for post create shooters and one for getting data
@v1_firearm_profile_bp.route('/shooters', methods=['GET'], endpoint=None)
def get_shooters():
    shooters_query = db.session.query(Shooter).all()
    print("")
    print("******************  we are in the GET show all shooters page  **********************")
    # shooters = Shooter.query.all()
    # before marshmellow to receive json
    shooter_schema = ShooterSchema(many=True) # what is this many=True? was able to see my db after this... change into list?
    output = shooter_schema.dump(shooters_query)
    return jsonify(output)


#----------------------------------------------------------------------------------------
# TODO THIS NEEDS WORK
@v1_firearm_profile_bp.route('/create_shooter', methods=['POST'])
def create_shooter():
    # shooters_query = db.session.query(Shooter).all()

    if request.method == "POST":
        print("")
        print("*******we are in the POST create_shooter page**********")
        print("++++++")
        print("++++++", request.content_type)
        shooter_data = request.get_json() # an object
        print('THIS IS THE SHOOTER_DATA================:', shooter_data) 
        # print("reqjson",request.json) # this is same as get_json()
        print("")
        # -----------------------------------------------------------------------------
        # @@@@@@@@@@@@@@@
        # TODO need to successfully add into database as of right now it works but nothing being added
        # @@@@@@@@@@@@@@@
        # adding before marshmellow
        # shooter = Shooter(
        #                   shooter_id=db.session.query.get_id(),
        #                     first_name=request.form['Fname'],
        #                     last_name=request.form['Lname'],
        #                     firearm_preference=request.form['Gpreference'],
        #                     description=request.form['Desc']
        #                     )
        # db.session.add(shooter)
        # db.session.commit()
        # -----------------------------------------------------------------------------
        # 
        # shooter_schema = ShooterSchema(many=True) # what is this many=True? was able to see my db after this... change into list?
        
        # turns into json data?
        # output = shooter_schema.dumps(shooter_data)
        # -------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------
        # TODO after receiving json data need to put into db
        #   need to figure out how to put json data into db

        # ADD to marshmellow after receiving Json
        # shooter_created = ShooterSchema('first_name': shooter_data.get('first_name'),
        #                                 'last_name': shooter_data.get('last_name'),
        #                                 'firearm_preference': shooter_data.get('firearm_preference'),
        #                                 'description': shooter_data.get('description'))
        print("")
        try:
            shooter_created = ShooterSchema() # request.get_json()?? (many=True)
            shooter_schema = shooter_created.load(shooter_data) # request.get_json()
            print("")
            print("added to db!")
            db.session.add(shooter_schema)
            db.session.commit()
            
            return ShooterSchema().dump(shooter_schema) #, many=True
        except ValidationError as e:
            print("WE HAVE A VALIDATION ERROR",)
            print(e)
            # print(e.messages)
            # print(e.valid_data)


        print("nothing happened????")
        # return shooter_created
        # print("----SHOOOTER CREATED------", shooter_created)
        # return jsonify(output)
        # -------------------------------------------------------------------------------------
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
@v1_firearm_profile_bp.route('/delete/<int:id>', methods=['GET','POST'])
def delete_shooter(id):
    print("==========Deleting Shooter===========")
    if request.method == 'POST':
        shooter_to_delete = Shooter.query.get_or_404(id)
        try:
            db.session.delete(shooter_to_delete)
            db.session.commit()
            print("shooter has been deleted id:", id)
            return redirect('/KumaArms/shooters')
        except:
            print('delete shooter error')
            return redirect('/KumaArms/shooters')
    else:
        return redirect(url_for('v1_firearm_profile_bp.show_shooters'))


#----------------------------------------------------------------------------------------
# EDIT SHOOTER
@v1_firearm_profile_bp.route('/edit/<int:id>', methods=['PUT'])
def edit_shooter(id):
    if request.method == "PUT":
        # put_shooter_data = request.get_json()
        print('==============================================================')
        print('WE ARE IN THE EDIT_SHOOTER PAGE')
        print('==============================================================')
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

# reads function but not sure how it does
# with v1_firearm_profile_bp.request_context(environ):
#     assert request.method == "POST"


# if __name__== "__main__":
#     #creates the db if it does not exist
#     db.create_all()
#     app.run(debug = True)