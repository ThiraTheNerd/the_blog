from . import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))


    def __repr__(self):
        return f'User {self.name}'

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    pass_secure = db.Column(db.String(255))
    blogs = db.relationship('Blog',backref = 'user',lazy = "dynamic")
    
    def __init__(self,username,email,pass_secure):
        self.username = username
        self.email = email
        self.pass_secure = pass_secure

    def save_user(self):
        d.session.add(self)
        db.session.commit()
    
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password) 
       
    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    '''
    Pitch class to define Pitch Objects
    '''
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    content =  db.Column(db.String(1000))
    date = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_blog(self):
        '''
        Function that saves pitches
        '''
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_all_blogs(cls):
        '''
        Function that queries the databse and returns all the pitches
        '''
        return Blog.query.all()

    @classmethod
    def delete_blog(cls,id):
        '''
        '''
        db.session.delete()
