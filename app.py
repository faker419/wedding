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

with app.app_context():
    db.create_all()

def insertRecords():
    with app.app_context():

        couples = Couples.query.all()  
        if not couples:  
            couples_to_import = [
                                    {'male_name': 'Hassan', 'female_name': 'Esraa', 'family_name': 'Zein'}, {'male_name': 'Ali', 'female_name': 'Nada', 'family_name': 'Fadlallah'}, {'male_name': '3alaa', 'female_name': 'Alaa', 'family_name': 'Attar'}, {'male_name': 'Jalal', 'female_name': 'Layal', 'family_name': 'Krisht'}, {'male_name': 'Mohammad', 'female_name': 'Dali', 'family_name': 'Taher'}, {'male_name': 'Mohammad', 'female_name': 'Sukaina', 'family_name': 'Jaffar'}, {'male_name': 'Mohammad', 'female_name': 'Zainab', 'family_name': 'Kassem'}, 
                                    {'male_name': 'Nabil', 'female_name': 'Zainab', 'family_name': 'Fawaz'}, {'male_name': 'Sami', 'female_name': 'Rasha', 'family_name': 'Jaafar'}, {'male_name': 'Abbad', 'female_name': 'Adeela', 'family_name': 'Jaafar'}, {'male_name': 'Khudor', 'female_name': 'Aya', 'family_name': 'Jaafar'}, {'male_name': 'Ali', 'female_name': 'Rasha', 'family_name': 'Hammoud'}, {'male_name': 'Bilal', 'female_name': 'Mariam', 'family_name': 'Hujeiri'}, {'male_name': 'Ali', 'female_name': 'Reine', 'family_name': 'Roda'}, {'male_name': 'Ali', 'female_name': 'Loulwa', 'family_name': 'Reda'}, {'male_name': 'Abdallah', 'female_name': 'Dalal', 'family_name': 'Hashim'}, {'male_name': 'Abbas', 'female_name': 'Hanan', 'family_name': 'Hashim'}, {'male_name': 'Hassan', 'female_name': 'Taghrid', 'family_name': 'Ghaddar'},
                                    {'male_name': 'Ali', 'female_name': 'Mallak', 'family_name': 'Fawaz'}, {'male_name': 'Hassan', 'female_name': 'Sherin', 'family_name': 'Mansour'}, {'male_name': 'Ali', 'female_name': 'Eman', 'family_name': 'Fawaz'}, {'male_name': 'Ali', 'female_name': 'Fatme', 'family_name': 'Dakak'}, {'male_name': 'Atef', 'female_name': 'Fatme', 'family_name': 'Fawaz'}, {'male_name': 'Rabih', 'female_name': 'Zahraa', 'family_name': 'Skeiky'}, {'male_name': 'Ali', 'female_name': 'Maya', 'family_name': 'Gebara'}, {'male_name': 'Abbas', 'female_name': 'Bardies', 'family_name': 'Zein'}, {'male_name': 'Abbas', 'female_name': 'Sally', 'family_name': 'Akar'}, {'male_name': 'Abbas', 'female_name': 'Tamara', 'family_name': 'Darwich'}, {'male_name': 'Hussein', 'female_name': 'Lara', 'family_name': 'Kodami'}, 
                                    {'male_name': 'Haidar', 'female_name': 'Nouma', 'family_name': 'Mustapha'}, {'male_name': 'Mohammed', 'female_name': 'Aya', 'family_name': 'Attar'}, {'male_name': 'Hussein', 'female_name': 'Maro', 'family_name': 'Roda'}, {'male_name': 'Ali', 'female_name': 'Sara', 'family_name': 'Saleh'}, {'male_name': 'Mohammed', 'female_name': 'Mrs', 'family_name': 'Maimalari'}, {'male_name': 'Alex', 'female_name': 'Mrs', 'family_name': 'Alex'}, {'male_name': 'Chiddy', 'female_name': 'Mrs', 'family_name': 'Chiddy'}, {'male_name': 'Amin', 'female_name': 'Fatu', 'family_name': 'Hojeij'}, {'male_name': 'Mohammed', 'female_name': 'Zainab', 'family_name': 'Kasfy'}, {'male_name': 'Ali', 'female_name': 'Ghinwa', 'family_name': 'Tormos'}, {'male_name': 'Rodi', 'female_name': 'Ranwa', 'family_name': 'Jammal'}, 
                                    {'male_name': 'Mustafa', 'female_name': 'Yasmin', 'family_name': 'Mansury'}, {'male_name': 'Ali', 'female_name': 'Najla', 'family_name': 'Kassim'}, {'male_name': 'Mohammed', 'female_name': 'Raghda', 'family_name': 'Fadlallah'}, {'male_name': 'Sattar', 'female_name': 'Dalal', 'family_name': 'Mansury'}, {'male_name': 'Mushtaba', 'female_name': 'Nisreen', 'family_name': 'Zai'}, {'male_name': 'Hisham', 'female_name': 'Shereen', 'family_name': 'Saidi'}, {'male_name': 'Saed', 'female_name': 'Nisreen', 'family_name': 'Kassem'}, {'male_name': 'Fahad', 'female_name': 'Fatima', 'family_name': 'Dandawaki'}, {'male_name': 'Yamani', 'female_name': 'Shehnaz', 'family_name': 'Shema'}, {'male_name': 'Othman', 'female_name': 'Shereen', 'family_name': 'Kabir'}, {'male_name': 'Wasef', 'female_name': 'Bushra', 'family_name': 'Mdeihly'},
                                    {'male_name': 'Wasim', 'female_name': 'Yashica', 'family_name': 'Syed'},  {'male_name': 'Roda', 'female_name': 'Suad', 'family_name': 'Fawaz'}, {'male_name': 'Habib', 'female_name': 'Faiza', 'family_name': 'Mansury'}
                                ]

            couples_imports = [Couples(**couple) for couple in couples_to_import]
            db.session.add_all(couples_imports)
            db.session.commit()

        singles = Singles.query.all() 
        if not singles:  
            singles_to_import = [
                                    {'prefix': 'Mr', 'name': 'Abbas', 'family_name': 'Fadlallah'}, {'prefix': 'Mr', 'name': 'Abbas', 'family_name': 'Chaady'}, {'prefix': 'Mr', 'name': 'Abdallah', 'family_name': 'Suleiman'}, {'prefix': 'Mr', 'name': 'Ahmad', 'family_name': 'Hmede'}, 
                                    {'prefix': 'Mr', 'name': 'Ahmad', 'family_name': 'Tahir'}, {'prefix': 'Mr', 'name': 'Ali', 'family_name': 'Hammoud'}, {'prefix': 'Mr', 'name': 'Ali', 'family_name': 'Jammal'}, {'prefix': 'Mr', 'name': 'Ali', 'family_name': 'Zein'}, {'prefix': 'Mr', 'name': 'Ali', 'family_name': 'Akar'}, {'prefix': 'Mr', 'name': 'Ali', 'family_name': 'Said'}, {'prefix': 'Mr', 'name': 'Ali', 'family_name': 'Dangote'}, {'prefix': 'Mr', 'name': 'Ali', 'family_name': 'Khan'}, {'prefix': 'Mr', 'name': 'Ali', 'family_name': 'Taher'}, {'prefix': 'Miss', 'name': 'Amina', 'family_name': 'Ebonique'}, {'prefix': 'Mr', 'name': 'Anis', 'family_name': 'Makki'}, {'prefix': 'Mr', 'name': 'Aseel', 'family_name': 'Saleh'}, {'prefix': 'Miss', 'name': 'Athena', 'family_name': 'Keswani'}, {'prefix': 'Miss', 'name': 'Aya', 'family_name': 'Ghaddar'}, 
                                    {'prefix': 'Mrs', 'name': 'Dalal', 'family_name': 'Zabat'}, {'prefix': 'Mrs', 'name': 'Fatima', 'family_name': 'Babagana'}, {'prefix': 'Mrs', 'name': 'Fatima', 'family_name': 'Gawuna'}, {'prefix': 'Mrs', 'name': 'Fatima', 'family_name': 'Kyaure'}, {'prefix': 'Miss', 'name': 'Fatima', 'family_name': 'Dandawaki'}, {'prefix': 'Mr', 'name': 'Foad', 'family_name': 'Hammoud'}, {'prefix': 'Mrs', 'name': 'Fozia', 'family_name': 'Mansury'}, {'prefix': 'Mr', 'name': 'Geryes', 'family_name': 'Bejjani'}, {'prefix': 'Mr', 'name': 'Ghazi', 'family_name': 'Mansour'}, {'prefix': 'Mrs', 'name': 'Ghida', 'family_name': 'Kassem'}, {'prefix': 'Miss', 'name': 'Grizelda', 'family_name': 'Jammal'}, {'prefix': 'Mr', 'name': 'Hadi', 'family_name': 'Fawaz'}, {'prefix': 'Mr', 'name': 'Hadi', 'family_name': 'Fadlallah'}, {'prefix': 'Mr', 'name': 'Haidar', 'family_name': 'Tahtah'}, 
                                    {'prefix': 'Mr', 'name': 'Haidar', 'family_name': 'Atwi'}, {'prefix': 'Mr', 'name': 'Haidar', 'family_name': 'Fares'}, {'prefix': 'Mrs', 'name': 'Hamo', 'family_name': 'Fawaz'}, {'prefix': 'Miss', 'name': 'Hana', 'family_name': 'Mustapha'}, {'prefix': 'Mrs', 'name': 'Hanan', 'family_name': 'Mansury'}, {'prefix': 'Mr', 'name': 'Hassan', 'family_name': 'Zein'}, {'prefix': 'Mr', 'name': 'Hassan', 'family_name': 'Jammal'}, {'prefix': 'Mr', 'name': 'Hassanein', 'family_name': 'Baydoun'}, {'prefix': 'Mr', 'name': 'Hussein', 'family_name': 'Tormos'}, {'prefix': 'Mr', 'name': 'Hussein', 'family_name': 'Jaffar'}, {'prefix': 'Mr', 'name': 'Ibrahim', 'family_name': 'Akar'}, {'prefix': 'Miss', 'name': 'Inaiya', 'family_name': 'Haq'}, {'prefix': 'Mr', 'name': 'Ismail', 'family_name': 'Mansury'}, {'prefix': 'Mr', 'name': 'Issa', 'family_name': 'Fares'}, {'prefix': 'Mr', 'name': 'Jad', 'family_name': 'Haidar'}, {'prefix': 'Mrs', 'name': 'Jamila', 'family_name': 'Haq'}, {'prefix': 'Mr', 'name': 'Karim', 'family_name': 'Attar'}, {'prefix': 'Mr', 'name': 'Kassem', 'family_name': 'Saleh'}, {'prefix': 'Miss', 'name': 'Kawthar', 'family_name': 'Fadlallah'},
                                    {'prefix': 'Mr', 'name': 'Khalifa', 'family_name': 'Dangote'}, {'prefix': 'Mr', 'name': 'Khudor', 'family_name': 'Elamin'}, {'prefix': 'Miss', 'name': 'Lara', 'family_name': 'Kassem'}, {'prefix': 'Mr', 'name': 'Mahdi', 'family_name': 'Fadlallah'}, {'prefix': 'Miss', 'name': 'Mariam', 'family_name': 'Dib'}, {'prefix': 'Miss', 'name': 'Mariam', 'family_name': 'Karram'}, {'prefix': 'Mrs', 'name': 'Maryam', 'family_name': 'Zabat'}, {'prefix': 'Miss', 'name': 'Mimz', 'family_name': 'Said'}, {'prefix': 'Mr', 'name': 'Mo', 'family_name': 'Saidi'}, 
                                    {'prefix': 'Mr', 'name': 'Moe', 'family_name': 'Jaffar'}, {'prefix': 'Mr', 'name': 'Mohammad', 'family_name': 'Atwi'}, {'prefix': 'Mr', 'name': 'Mohammad', 'family_name': 'Tawbi'}, {'prefix': 'Mr', 'name': 'Mohammad', 'family_name': 'Saidi'}, {'prefix': 'Mr', 'name': 'Mohammed', 'family_name': 'Zein'}, {'prefix': 'Mr', 'name': 'Mohd', 'family_name': 'Ali'}, {'prefix': 'Mr', 'name': 'Mohd', 'family_name': 'Ali'}, {'prefix': 'Mr', 'name': 'Mustafa', 'family_name': 'Noureldeen'}, {'prefix': 'Mr', 'name': 'Musty', 'family_name': 'Akar'}, {'prefix': 'Miss', 'name': 'Nada', 'family_name': 'Kidami'}, {'prefix': 'Mr', 'name': 'Nadeem', 'family_name': 'Dandawaki'}, {'prefix': 'Miss', 'name': 'Nana', 'family_name': 'Kassem'}, {'prefix': 'Mr', 'name': 'Nehme', 'family_name': 'Dayekh'}, {'prefix': 'Mrs', 'name': 'Noory', 'family_name': 'Khan'}, {'prefix': 'Miss', 'name': 'Nour', 'family_name': 'Fadlallah'}, {'prefix': 'Mrs', 'name': 'Rayan', 'family_name': 'Salma'}, {'prefix': 'Miss', 'name': 'Reema', 'family_name': 'Kamal'}, {'prefix': 'Mrs', 'name': 'Reena', 'family_name': 'Kassem'}, 
                                    {'prefix': 'Mr', 'name': 'Roda', 'family_name': 'Berjawi'}, {'prefix': 'Mr', 'name': 'Roda', 'family_name': 'Soufan'}, {'prefix': 'Mr', 'name': 'Saed', 'family_name': 'Zein'}, {'prefix': 'Mr', 'name': 'Safi', 'family_name': 'Zai'}, {'prefix': 'Mr', 'name': 'Said', 'family_name': 'Dayekh'}, {'prefix': 'Mr', 'name': 'Saleh', 'family_name': 'Mansury'}, {'prefix': 'Mr', 'name': 'Samer', 'family_name': 'Mansour'}, {'prefix': 'Miss', 'name': 'Sara', 'family_name': 'Dib'}, {'prefix': 'Mrs', 'name': 'Shaheen', 'family_name': 'Sayed'}, {'prefix': 'Mr', 'name': 'Suleiman', 'family_name': 'Dayekh'}, {'prefix': 'Mrs', 'name': 'Taihida', 'family_name': 'Babagana'}, {'prefix': 'Mr', 'name': 'Yahya', 'family_name': 'Yahya'}, {'prefix': 'Miss', 'name': 'Yara', 'family_name': 'Yassin'}, {'prefix': 'Mr', 'name': 'Youssef', 'family_name': 'Shour'}, {'prefix': 'Mr', 'name': 'Yusef', 'family_name': 'Mansury'}, {'prefix': 'Miss', 'name': 'Zahra', 'family_name': 'Saidi'}, {'prefix': 'Mrs', 'name': 'Zainab', 'family_name': 'Khalil'}, {'prefix': 'Miss', 'name': 'Zainab', 'family_name': 'Attar'}, {'prefix': 'Miss', 'name': 'Zaza', 'family_name': 'Fayad'}, {'prefix': 'Mr', 'name': 'Uncle', 'family_name': 'Musty'}
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

