# coding: utf-8
from datetime import datetime
from ._base import db
from .base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.exc import IntegrityError
from sqlalchemy_utils import EmailType, ChoiceType

class Activity(Base):
	
	subject = db.Column(db.String(100), nullable=False)
	detail = db.Column(db.Text)

	contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
	org_id = db.Column(db.Integer, db.ForeignKey('organisation.id'))
	project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
	created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 

	@staticmethod
	def create(**kwargs):
		a = Activity(**kwargs)
		db.session.add(a)
		try:
			db.session.commit()
		except IntegrityError: 
			db.session.rollback()
			print('session rollback')
		return a

	def __repr__(self):
		return self.id
