# coding: utf-8
from datetime import datetime
from ._base import db
from .base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.exc import IntegrityError
from sqlalchemy_utils import EmailType, ChoiceType

class Project(Base):
	
    STATUS_CHOICE = [
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]

    start_date = db.Column(db.Date, default=db.func.current_date())
    end_date = db.Column(db.Date, default=db.func.current_date())
    status = db.Column(ChoiceType(STATUS_CHOICE), nullable=False)

    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    org_id = db.Column(db.Integer, db.ForeignKey('organisation.id'))
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))

    activities = db.relationship('Activity', backref='project')
    invoices = db.relationship('Invoice', backref='project')


    def __repr__(self):
        return str(self.id)
