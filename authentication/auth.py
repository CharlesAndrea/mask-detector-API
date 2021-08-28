from flask import jsonify, request
from functools import wraps
from models.models import Empleado, db
import jwt
import app

def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):
       token = None
       if 'x-access-token' in request.headers:
           token = request.headers['x-access-token']
 
       if not token:
           return jsonify({'message': 'a valid token is missing'}), 401
       try:
           data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
           current_user = db.session.query(Empleado).filter_by(public_id=data['public_id']).first()
       except:
           return jsonify({'message': 'token is invalid'
           }), 401
 
       return f(current_user, *args, **kwargs)
   return decorator