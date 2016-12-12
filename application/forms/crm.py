# coding: utf-8
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm
from ..models import Organisation, Contact

class AddOrganisationForm(ModelForm, Form):
	"""Add organisation form"""
	class Meta:
		model = Organisation
	"""
    name = StringField('Username',
                    validators=[DataRequired("Username shouldn't be empty.")])
	"""