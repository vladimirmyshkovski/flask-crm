# coding: utf-8
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from ._base import db
from .base import Base
from sqlalchemy.orm import relationship

class User(Base, db.Model):
    
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    avatar = db.Column(db.String(200), default='default.png')
    password = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean, default=False)
    organisations = db.relationship('Organisation', backref="user")
    projects = db.relationship('Project', backref="user")
    contacts = db.relationship('Contact', backref="user")
    activities = db.relationship('Activity', backref="user")        
    
     

    def __setattr__(self, name, value):
        # Hash password when set it.
        if name == 'password':
            value = generate_password_hash(value)
        super(User, self).__setattr__(name, value)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %s>' % self.name
