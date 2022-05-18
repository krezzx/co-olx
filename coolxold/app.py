
import json
import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager,UserMixin
from flask_restful import Api,Resource
import os
from werkzeug.utils import secure_filename

app=Flask(__name__)
api=Api(app)
app.config['SECRET_KEY']='8efde650d0e727ef697bb75adb2a114a'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///userData.db'
app.config['SQLALCHEMY_BINDS']={
    'product':'sqlite:///product.db'
}


UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))








#database model
class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(20),nullable=False)
    mobile=db.Column(db.Integer,nullable=False)
    webmail=db.Column(db.String(120),nullable=False)
    address=db.Column(db.String(500),nullable=False)
    course=db.Column(db.String,nullable=False)
    password=db.Column(db.String(60),nullable=False)
    
    def __repr__(self):
        return f"User('{self.id}','{self.username}','{self.webmail}','{self.mobile}','{self.address}','{self.course}')"


class Product(db.Model):
    __bind_key__='product'
    uid=db.Column(db.Integer)
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50))
    desc=db.Column(db.String(500))
    cat=db.Column(db.String(30))
    price=db.Column(db.Integer)
    pic=db.Column(db.String(150))
    rm=db.Column(db.Integer,default=0)




from routes import *
from category import *

if __name__=="__main__":
    app.run(debug=True)