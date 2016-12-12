# coding: utf-8
from flask import render_template, Blueprint, redirect, request, url_for, g
from ..utils.account import signin_user, signout_user
from ..utils.permissions import VisitorPermission, UserPermission
from ..models import db, User, Organisation, Contact
from ..forms import AddOrganisationForm, AddContactForm
bp = Blueprint('crm', __name__)

@bp.route('/crm', methods=['GET', 'POST'])
@UserPermission()
def crm():
    """Index page"""

    #form = AddOrganisationForm(request.form)
    return render_template('site/index/index.html')

@bp.route('/add/organisation', methods=['GET', 'POST'])
@UserPermission()
def add_organisation():
    """Add organisation"""
    form = AddOrganisationForm(request.form)
    if request.method == 'POST':
        if form.validate():
            org = Organisation.create(**form.data, user=g.user)
            return redirect(url_for('crm.crm'))
    return render_template('crm/add/add_organisation.html')

@bp.route('/add/contact', methods=['GET', 'POST'])
@UserPermission()
def add_contact():
    """Add contact"""
    form = AddContactForm(request.form)
    if request.method == 'POST':
        if form.validate():
            con = Contact.create(**form.data, user=g.user)
            return redirect(url_for('crm.crm'))
    return render_template('crm/add/add_contact.html')
