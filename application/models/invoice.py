# coding: utf-8
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from ._base import db
from .base import Base
from sqlalchemy.orm import relationship


class Invoice(Base):

	issue_date = db.Column(db.Date)
	amount = db.Column(db.Integer, nullable=False)
	paid = db.Column(db.Boolean, default=False)

	created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
	project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

	@staticmethod
	def create(**kwargs):
		i = Invoice(**kwargs)
		db.session.add(i)
		try:
			db.session.commit()
		except IntegrityError:
			db.session.rollback()
		return i


	def __repr__(self):
		return '<Invoice %s>' % self.amount
