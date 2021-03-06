from models.compound import Compound
from config import db
from werkzeug.exceptions import NotFound


def get():
    """Get all compounds"""
    return Compound.query.all()


def post(body):
    """Create new compound"""
    compound = Compound(**body)
    db.session.add(compound)
    db.session.commit()
    return compound


def put(body):
    """Update compound by id"""
    compound = Compound.query.get(body['id'])
    if compound:
        compound = Compound(**body)
        db.session.merge(compound)
        db.session.flush()
        db.session.commit()
        return compound
    raise NotFound(f'No such entity found with id={str(body["id"])}')


def delete(_id):
    """Delete compound by id"""
    compound = Compound.query.get(_id)
    if compound:
        db.session.delete(compound)
        db.session.commit()
        return {'success': True}
    raise NotFound(f'no such entity found with id={str(_id)}')
