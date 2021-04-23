from flask import Flask

from .main.routes import main
from .extensions import mongo

def create_app():
    app= Flask(__name__)

    app.config['MONGO_URI'] = 'mongodb+srv://groupe_4:03042021@mycluster.he2ba.mongodb.net/RESEAU_SOCIAL?retryWrites=true&w=majority'
    

    #app.config['MONGO_URI'] = 'mongodb://localhost:27017/My_Project'
    
    mongo.init_app(app)

    app.register_blueprint(main)
    
    return app