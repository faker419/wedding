import os
from flask import Flask, render_template, jsonify, request,  redirect,  url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import random
import datetime

'''

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/wedding'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ihsdtrh4545yh45645t3gfr'


db = SQLAlchemy(app)

STATIC_ROOT = 'static'
TEMPLATES_ROOT = 'templates'
IMG_ROOT =  os.path.join(STATIC_ROOT, "img")


'''

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="issafares",
    password="arawaterpass",
    hostname="issafares.mysql.pythonanywhere-services.com",
    databasename="issafares$wedding",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'ihsdtrh4545yh45645t3gfr'



db = SQLAlchemy(app)


BASE_DIR = '/home/issafares/wedding/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
IMG_ROOT =  os.path.join(STATIC_ROOT, "img")






class Couples(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    male_name = db.Column(db.String(20), nullable=False)
    male_response = db.Column(db.Boolean, nullable=False, default=False)
    female_name = db.Column(db.String(20), nullable=False)
    female_response = db.Column(db.Boolean, nullable=False, default=False)
    family_name = db.Column(db.String(20), nullable=False)
    comment = db.Column(db.Text, nullable=True)
    is_answered = db.Column(db.Boolean, nullable=False, default=False)
    identification = db.Column(db.Integer, nullable=False, unique=True)

    def __init__(self, male_name, female_name, family_name, comment=None):
        self.male_name = male_name
        self.female_name = female_name
        self.family_name = family_name
        self.comment = comment
        self.identification = random.randint(100000, 999999)  # Generate random identification value

    def to_dict(self):
        return {
            'id': self.id,
            'male_name': self.male_name,
            'male_response': self.male_response,
            'female_name': self.female_name,
            'female_response': self.female_response,
            'family_name': self.family_name,
            'comment': self.comment,
            'is_answered': self.is_answered,
            'identification': self.identification
        }
    
class Singles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    response = db.Column(db.Boolean, nullable=False, default=False)
    family_name = db.Column(db.String(20), nullable=False)
    comment = db.Column(db.Text, nullable=True)
    is_answered = db.Column(db.Boolean, nullable=False, default=False)
    identification = db.Column(db.Integer, nullable=False, unique=True)
    prefix = db.Column(db.String(20), nullable=False)

    def __init__(self, prefix, name, family_name, comment=None):
        self.name = name
        self.family_name = family_name
        self.prefix = prefix
        self.comment = comment
        self.identification = random.randint(100000, 999999)  # Generate random identification value

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'response': self.response,
            'family_name': self.family_name,
            'prefix': self.prefix,
            'comment': self.comment,
            'is_answered': self.is_answered,
            'identification': self.identification
        }


def insertRecords():
    with app.app_context():


        singles =  db.session.query(Singles).filter(Singles.id == 99).first()
        if not singles:  
            singles_to_import = [
                                    {'prefix': 'Mr', 'name': 'Youssef', 'family_name': 'Attar'},
                                    {'prefix': 'Mr', 'name': 'Haidar', 'family_name': 'Attar'},
                                    {'prefix': 'Miss', 'name': 'Hadeel', 'family_name': 'Tahir'},
                                    {'prefix': 'Mr', 'name': 'Ahmad', 'family_name': 'Kidami'},
                                ]

            singles_imports = [Singles(**single) for single in singles_to_import]
            db.session.add_all(singles_imports)
            db.session.commit()

insertRecords()





@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')



@app.route('/couples_invitation')
def couples_invitation():
    guest_id = request.args.get('id')
    code = request.args.get('code')
    # Validate guest_id and code
    if check_identification(guest_id, code, 'couples'):
        return render_template('couple_invitations.html')
    else:
        return redirect(url_for('index'))

@app.route('/couples_data', methods=['GET'])
def get_couple_data():
    guest_id = request.args.get('id')
    couple = db.session.query(Couples).filter(Couples.id == int(guest_id)).first()
    if couple:
        couple_data = couple.to_dict()
        couple_data['couple_id'] = guest_id
        return jsonify(couple_data)
    else:
        return jsonify({'error': 'Couple not found'}), 404
    
@app.route('/api/update_responses', methods=["POST" , "GET"])
def coupeles_response():
    if request.method == "POST" :
        try:

            target_date = datetime.datetime(2024, 3, 18)
            current_date = datetime.datetime.now()

            if current_date <= target_date:
                jsonData = request.get_json()
                male_response = jsonData['male_response']
                female_response = jsonData['female_response']
                couple_id = jsonData['couple_id']
                comment = jsonData['comment']

                couple = db.session.query(Couples).filter(Couples.id == int(couple_id)).first()

                if couple.is_answered:
                    message = 'Dear Mr and Mrs {}, your response has been Re-submitted'.format(couple.family_name)
                else:
                    message = 'Dear Mr and Mrs {}, your response has been submitted'.format(couple.family_name)

                setattr(couple,'male_response',male_response)
                setattr(couple,'female_response',female_response)
                setattr(couple,'comment',comment)
                setattr(couple,'is_answered',True)
                db.session.commit()
            else:
                message = 'The form was closed on the 18th of March, We ask for your understanding.'

            json_response = {'message' : message}
            return jsonify(json_response)

        except Exception as e:
            message = '{}'.format(e)
        
            json_response = {'message' : message}
            return jsonify(json_response)
    


@app.route('/singles_invitation')
def singles_invitation():
    guest_id = request.args.get('id')
    code = request.args.get('code')

    if check_identification(guest_id, code, 'singles'):
        return render_template('single_invitations.html')
    else:
        return redirect(url_for('index'))
    
@app.route('/singles_data', methods=['GET'])
def get_single_data():
    try:
        guest_id = request.args.get('id')
        single = db.session.query(Singles).filter(Singles.id == int(guest_id)).first()
        
        if single:
            single_data = single.to_dict()
            single_data['single_id'] = guest_id
            return jsonify(single_data)
        else:
            return jsonify({'error': 'Individual not found'}), 404
    except Exception as e:

        print(f"The singles error: {str(e)}")
    
@app.route('/api/update_responses_singles', methods=["POST" , "GET"])
def singles_response():
    if request.method == "POST" :

        try:

            target_date = datetime.datetime(2024, 3, 18)
            current_date = datetime.datetime.now()

            if current_date <= target_date:
                jsonData = request.get_json()
                response = jsonData['response']
                single_id = jsonData['single_id']
                comment = jsonData['comment']

                single = db.session.query(Singles).filter(Singles.id == int(single_id)).first()

                full_name = single.prefix + ' ' + single.family_name
                if single.is_answered:
                    message = 'Dear {}, your response has been Re-submitted'.format(full_name)
                else:
                    message = 'Dear {}, your response has been submitted'.format(full_name)

                setattr(single,'response',response)
                setattr(single,'comment',comment)
                setattr(single,'is_answered',True)
                db.session.commit()
            else:
                message = 'The form was closed on the 18th of March, We ask for your understanding.'

            json_response = {'message' : message}
            return jsonify(json_response)

        except Exception as e:
            message = '{}'.format(e)
        
            json_response = {'message' : message}
            return jsonify(json_response)



def check_identification(guest_id, identification, guest_type):
    if guest_type == 'couples':
        couple = Couples.query.filter_by(id=guest_id, identification=identification).first()
        return couple is not None
    if guest_type == 'singles':
        single = Singles.query.filter_by(id=guest_id, identification=identification).first()
        return single is not None
    return None



@app.route('/attendance')
def attendance():
    return render_template('attendance.html')

@app.route('/api/attendance', methods=["POST" , "GET"])
def attendance_data():
    if request.method == "POST" :

        jsonData = request.get_json()
        guest_type = jsonData['type']  

        list_of_dicts = []
        no_response = 0
        attending = 0
        unable = 0
        if guest_type == 'couples':
            couples = db.session.query(Couples).all()
            for couple in couples:
                if not couple.is_answered:
                    no_response += 2 
                    response_male = 1
                    response_female = 1
                else:
                    if couple.male_response:
                        attending += 1
                        response_male = 2
                    else:
                        unable += 1
                        response_male = 3
                    if couple.female_response:
                        attending += 1
                        response_female = 2
                    else:
                        unable += 1
                        response_female = 3
     
                dic1 = {"first_name":couple.male_name,"family_name":couple.family_name,"attendance":response_male,"memo":couple.comment}
                dic2 = {"first_name":couple.female_name,"family_name":couple.family_name,"attendance":response_female,"memo":couple.comment}
                list_of_dicts.append(dic1)
                list_of_dicts.append(dic2)
        else:
            singles = db.session.query(Singles).all()
            for single in singles:
                if not single.is_answered:
                    no_response += 1
                    response = 1
                else:
                    if single.response:
                        attending += 1
                        response = 2
                    else:
                        unable += 1
                        response = 3
     
                dic = {"first_name":single.name,"family_name":single.family_name,"attendance":response,"memo":single.comment}
                list_of_dicts.append(dic)

        json_response = {'data_response': list_of_dicts, 'pending':no_response,'attending':attending,'unable':unable}
        return jsonify(json_response) 



if __name__ == "__main__":
   app.run(debug=True)

