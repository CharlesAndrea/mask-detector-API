from flask import jsonify
from models.models import Departamento, DepartamentoSchema, db

def get_all_deps():
    departamento_schema = DepartamentoSchema(many=True)
    departamentos = db.session.query(Departamento).all()
    return jsonify(departamento_schema.dump(departamentos))