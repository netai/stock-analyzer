import uuid
import datetime
from app import db
from app.models import User
from ..schema.error_schema import ErrorSchema

def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            name=data['name'].title(),
            mobile=data['mobile'],
            email=data['email'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'User successfully registered.'
        }
        return response_object, 201
    else:
        return ErrorSchema.get_response('UserExistError')

def get_all_users():
    return User.query.all()

def get_a_user(public_id):
    try:
        return User.query.filter_by(public_id=public_id).first()
    except Exception as e:
        return ErrorSchema.get_response('InternalServerError', e)

def save_changes(data):
    db.session.add(data)
    db.session.commit()