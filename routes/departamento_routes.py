from flask import Blueprint, request
from controllers.departamento_controller import get_all_deps

departamento_bp = Blueprint('departamento_bp', __name__)

@departamento_bp.route('/deps', methods=['GET'])
def get_departamentos():
    return get_all_deps()
