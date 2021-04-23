from flask import Blueprint, render_template , request, url_for, redirect

from reseau_social_groupe_4.extensions import mongo

main = Blueprint('main',__name__)

@main.route('/')
def index():
    todos_collection = mongo.db.USER
    todos= todos_collection.find()
    return render_template('index.html',todos= todos)

@main.route('/add', methods=['POST'])
def add_user():
    todos_collection = mongo.db.USER
    name = request.form.get('user_name')
    email= request.form.get('user_email')
    sexe= request.form.get('user_sexe')
    date= request.form.get('user_date_of_birth')
    numero= request.form.get('user_num')
    city= request.form.get('user_city')
    firm= request.form.get('user_firm')
    college= request.form.get('user_college')
    print(name,email,sexe,date,numero,city,firm,college)
    todos_collection.insert_one({'Name' : name, 'Gender': sexe,'Date_of_birth': date,'Email' : email,'Telephone':numero,'City':city, 'Firm': firm, 'College':college })
    return redirect(url_for('main.index'))

