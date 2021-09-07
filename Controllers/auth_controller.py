from flask import jsonify, make_response, request, current_app
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta
from models.models import Empleado, Departamento, db
import jwt
import uuid


def get_all_users(current_user):
    # querying the database
    # for all the entries in it
    users = db.session.query(Empleado).all()
    # converting the query objects
    # to list of jsons
    output = []
    for user in users:
        # appending the user data json
        # to the response list
        output.append({
            'public_id': user.public_id,
            'correo' : user.correo,
            'contrasena' : user.contrasena
        })
  
    return jsonify({'users': output})

def login():
    # creates dictionary of form data
    auth = request.get_json()
    print(auth)
    if not auth or not auth.get('correo') or not auth.get('contrasena'):
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify. Login required',
            401,
            {'Authentication': 'Login required'}
        )
  
    user = db.session.query(Empleado).filter_by(correo=auth.get('correo')).first()

    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Could not verify. User does not exist',
            401,
            {'Authentication' : 'User does not exist'}
        )
  
    if check_password_hash(user.contrasena, auth.get('contrasena')):
        # Generates the JWT Token
        token = jwt.encode({
            'public_id': user.public_id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, current_app.config['SECRET_KEY'])
        # Other necessary attributes
        ci = user.ci
        nombre_completo = user.nombre_completo
        correo = user.correo
        tlf = user.tlf
        direccion = user.direccion
        departamento = db.session.query(Departamento).get(user.dept_id).nombre_dept
        rol_id = user.rol_id
        supervisor = db.session.query(Empleado).get(user.ci_s).nombre_completo

        # Response to the request
        resp = make_response(jsonify({
            'token': token, 
            'ci': ci, 
            'nombre_completo': nombre_completo, 
            'correo': correo, 
            'tlf': tlf, 
            'direccion': direccion, 
            'departamento': departamento, 
            'rol': rol_id,
            'supervisor': supervisor}), 201)
        resp.headers['Access-Controll-Allow-Origin']= '*'
        resp.headers['Content-Type']
        return resp
    # Returns 403 if password is wrong
    return make_response(
        'Could not verify',
        403,
        {'Authentication' : 'Wrong Password'}
    )

def signup(data): 
    hashed_password = generate_password_hash(data.get('contrasena'), method='sha256')#sha256

    existent_user = db.session.query(Empleado).filter_by(ci = data.get('ci')).first()
    if not existent_user:
        new_user = Empleado(
            ci = data.get('ci'),
            public_id = str(uuid.uuid4()),
            nombre_completo = data.get('nombre_completo'),
            correo = data.get('correo'),
            contrasena = hashed_password,
            tlf = data.get('tlf'),
            direccion = data.get('direccion'),
            fecha_nacimiento = data.get('fecha_nacimiento'),
            sexo = data.get('sexo'),
            estado = data.get('estado'),
            dept_id = data.get('dept_id'),
            rol_id = data.get('rol_id'),
            ci_s = data.get('ci_s')
        )
        db.session.add(new_user)
        db.session.commit(),
        return make_response('User registered successfully'
        )
    else:
        return make_response('User already exists')


  



