# coding: utf-8
from datetime import datetime
from ._base import db
from .base import Base

class Contact(Base):
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    phone_mobile = db.Column(db.String(50), nullable=False, unique=True)
    phone_work = db.Column(db.String(50))
    phone_fax = db.Column(db.String(50))
    phone_other = db.Column(db.String(50))
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
    org_id = db.Column(db.Integer, db.ForeignKey('organisation.id'), nullable=False, info={"label": "Organisation"})


    def __repr__(self):
        return '<Contact %s>' % self.name
