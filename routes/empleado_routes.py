from flask import Blueprint, request
from controllers.empleado_controller import create

empleado_bp = Blueprint('empleado_bp', __name__)

@empleado_bp.route('/create', methods=['POST'])
def createE():
    data = request.get_json()
    create(data.get("empleado"))