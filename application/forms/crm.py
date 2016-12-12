# coding: utf-8
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm
from ..models import Organisation, Contact, User
from wtforms.ext.sqlalchemy.fields import QuerySelectField

def available_organisations():
	return Organisation.query.all()


class AddOrganisationForm(ModelForm, Form):
	"""Add organisation form"""
	class Meta:
		model = Organisation


class AddContactForm(ModelForm, Form):
	"""Add contact form"""
	org_id = QuerySelectField('Organisation', query_factory=available_organisations, get_label='name')
	class Meta:
		model = Contact
