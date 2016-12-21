# coding: utf-8
from flask import render_template, Blueprint, redirect, request, url_for, g, flash, abort
from ..utils.account import signin_user, signout_user
from ..utils.permissions import VisitorPermission, UserPermission
from ..models import db, User, Organisation, Contact, Project, Activity, Invoice, Base
from ..forms import AddOrganisationForm, AddContactForm, AddProjectForm, AddActivityForm,AddInvoiceForm


bp = Blueprint('crm', __name__)


@bp.route('/post', methods=['GET', 'POST', 'PUT'])
@UserPermission()
def post():
    """POST page"""
    import sqlalchemy
    from sqlalchemy import inspect
    from sqlalchemy.ext.automap import automap_base
    ewqe = automap_base()
    for i in ewqe.classes:
        print(i)
    tables = list(db.metadata.tables.keys())
    url = request.form['url']
    for i in tables:
        if url.split('/')[-1].startswith(i):
            i = i.capitalize()

    return render_template('site/index/index.html')


@bp.route('/crm', methods=['GET', 'POST'])
@UserPermission()
def crm():
    """Index page"""

    return render_template('site/index/index.html')


@bp.route('/add/<keyword>', methods=['GET', 'POST'])
@UserPermission()
def add(keyword):
    """Add """
    if keyword == 'organisation':
        form = AddOrganisationForm(request.form)
        if form.validate():
            org = Organisation.create(**form.data, created_by=g.user.id)
            flash(str(keyword).capitalize() + " created successfully!")
            keyword = str(keyword)+'s'
            return redirect(url_for('crm.view', keyword=keyword))
    
    if keyword == 'contact':
        form = AddContactForm(request.form)
        if form.validate():
            form.org_id.data = form.org_id.data.id
            con = Contact.create(**form.data, created_by=g.user.id)
            flash(str(keyword).capitalize() + " created successfully!")
            keyword = str(keyword)+'s'
            return redirect(url_for('crm.view', keyword=keyword))

    if keyword == 'project':
        form = AddProjectForm(request.form)
        if form.validate():
            form.project_id.data = form.project_id.data.id
            flash(str(keyword).capitalize() + " created successfully!")
            keyword = str(keyword)+'s'
            return redirect(url_for('crm.view', keyword=keyword))

    if keyword == 'activity':
        form = AddActivityForm(request.form)
        if form.validate():
            form.project_id.data = form.project_id.data.id
            flash(str(keyword).capitalize() + " created successfully!")
            keyword = str(keyword)+'s'
            return redirect(url_for('crm.view', keyword=keyword))

    if keyword == 'invoice':
        form = AddInvoiceForm(request.form)
        if form.validate():
            form.project_id.data = form.project_id.data.id
            flash(str(keyword).capitalize() + " created successfully!")
            keyword = str(keyword)+'s'
            return redirect(url_for('crm.view', keyword=keyword))

    return render_template('crm/add/add.html', keyword=keyword, form=form)



@bp.route('/view/<keyword>', methods=['GET', 'POST'])
@UserPermission()
def view(keyword):
    """View"""
    if keyword == 'organisations':
        table = Organisation.query.filter_by(created_by=g.user.id).all()
        columns = [o.key for o in Organisation.__table__.columns]
    elif keyword == 'contacts':
        table = Contact.query.filter_by(created_by=g.user.id).all()
        columns = [o.key for o in Contact.__table__.columns]
    elif keyword == 'projects':
        table = Project.query.filter_by(created_by=g.user.id).all()
        columns = [o.key for o in Project.__table__.columns]
    elif keyword == 'activities':
        table = Activity.query.filter_by(created_by=g.user.id).all()
        columns = [o.key for o in Activity.__table__.columns]
    elif keyword == 'invoices':
        table = Invoice.query.filter_by(created_by=g.user.id).all()
        columns = [o.key for o in Invoice.__table__.columns]
    else:
        abort(404)
    return render_template('crm/view/view.html', columns=columns, table=table, keyword=keyword)

@bp.route('/update/<table>/<id>', methods=['GET', 'POST'])
@UserPermission()
def update(table, id):
    pass