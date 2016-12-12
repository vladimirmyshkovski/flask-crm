# coding: utf-8
from datetime import datetime
from ._base import db
from .base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.exc import IntegrityError

class Organisation(Base):

    name = db.Column(db.String(50), unique=True, nullable=False)
    city = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50))
    contacts = db.relationship('Contact', backref="organisation", lazy='dynamic')
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 

    @staticmethod
    def create(**kwargs):
        o = Organisation(**kwargs)
        db.session.add(o)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return o

    def __repr__(self):
        return '<Organisation %s>' % self.name
