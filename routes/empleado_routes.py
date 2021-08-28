from flask import Blueprint, request
from controllers.empleado_controller import create_employee

empleado_bp = Blueprint('empleado_bp', __name__)

@empleado_bp.route('/create', methods=['POST'])
def crear_empleado():
    data = request.get_json()
    create_employee(data.get("empleado"))