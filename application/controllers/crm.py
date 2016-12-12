# coding: utf-8
from flask import render_template, Blueprint, redirect, request, url_for, g
from ..forms import SigninForm, SignupForm, AddOrganisationForm
from ..utils.account import signin_user, signout_user
from ..utils.permissions import VisitorPermission, UserPermission
from ..models import db, User, Organisation
bp = Blueprint('crm', __name__)

@bp.route('/add/organisation', methods=['GET', 'POST'])
@UserPermission()
def add_organisation():
    """Add organisation"""

    db.create_all()
    form = AddOrganisationForm(request.form)
    if request.method == 'POST':
        if form.validate():
            contact = Organisation(**form.data, user=g.user)
            db.session.add(contact)
            db.session.commit()
            return redirect(url_for('site.index'))
    return render_template('crm/add/add_organisation.html', form=form)