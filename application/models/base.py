from ._base import db
from sqlalchemy.exc import IntegrityError, InterfaceError
from flask import flash

class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    @classmethod
    def create(cls,**kwargs):
        c = cls(**kwargs)
        db.session.add(c)
        try:
            db.session.commit()
            flash((c.__tablename__).capitalize() + u' created successfully!', 'success')
        except IntegrityError:
            db.session.rollback()
            flash((c.__tablename__).capitalize() + u' created failed!' + u' IntegrityError', 'error')
        except InterfaceError:
            db.session.rollback()
            flash((c.__tablename__).capitalize() + u' created failed!' + u' InterfaceError', 'error')
        return c