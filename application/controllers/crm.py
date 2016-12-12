# coding: utf-8
from flask import render_template, Blueprint, redirect, request, url_for, g, flash
from ..utils.account import signin_user, signout_user
from ..utils.permissions import VisitorPermission, UserPermission
from ..models import db, User, Organisation, Contact, Project, Activity, Invoice
from ..forms import AddOrganisationForm, AddContactForm, AddProjectForm, AddActivityForm,AddInvoiceForm


bp = Blueprint('crm', __name__)


@bp.route('/crm', methods=['GET', 'POST'])
@UserPermission()
def crm():
    """Index page"""

    return render_template('site/index/index.html')


@bp.route('/add/organisation', methods=['GET', 'POST'])
@UserPermission()
def add_organisation():
    """Add organisation"""
    OrgForm = AddOrganisationForm(request.form)
    if request.method == 'POST':
        if OrgForm.validate():
            print(OrgForm.data)
            org = Organisation.create(**OrgForm.data, user=g.user)
            flash("Organisation created successfully!")
            return redirect(url_for('crm.crm'))
    return render_template('crm/add/add_organisation.html')


@bp.route('/add/contact', methods=['GET', 'POST'])
@UserPermission()
def add_contact():
    """Add contact"""
    form = AddContactForm(request.form)
    if request.method == 'POST':
        if form.validate():
            form.org_id.data = form.org_id.data.id
            con = Contact.create(**form.data, user=g.user)
            flash("Contact created successfully!")
            return redirect(url_for('crm.crm'))
    return render_template('crm/add/add_contact.html')


@bp.route('/add/project', methods=['GET', 'POST'])
@UserPermission()
def add_project():
    """Add project"""
    form = AddProjectForm(request.form)
    if request.method == 'POST':
        if form.validate():
            form.org_id.data = form.org_id.data.id
            form.contact_id.data = form.contact_id.data.id
            pro = Project.create(**form.data, created_by=g.user.id)
            flash("Project created successfully!")
            return redirect(url_for('crm.crm'))
    return render_template('crm/add/add_project.html')


@bp.route('/add/activity', methods=['GET', 'POST'])
@UserPermission()
def add_activity():
    """Add activity"""
    form = AddActivityForm(request.form)
    if request.method == 'POST':
        if form.validate():
            form.org_id.data = form.org_id.data.id
            form.contact_id.data = form.contact_id.data.id
            form.project_id.data = form.project_id.data.id
            act = Activity.create(**form.data,
                created_by=g.user.id
                )
            flash("Activity created successfully!")
            return redirect(url_for('crm.crm'))
    return render_template('crm/add/add_activity.html')


@bp.route('/add/invoice', methods=['GET', 'POST'])
@UserPermission()
def add_invoice():
    """Add invoice"""
    form = AddInvoiceForm(request.form)
    if request.method == 'POST':
        if form.validate():
            form.project_id.data = form.project_id.data.id
            inv = Invoice.create(**form.data,
                created_by=g.user.id
                )
            flash("Invoice created successfully!")
            return redirect(url_for('crm.crm'))
    return render_template('crm/add/add_invoice.html')

