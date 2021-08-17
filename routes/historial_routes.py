from flask import Blueprint, request
from controllers.historial_controller import create

historial_bp = Blueprint('historial_bp', __name__)

@historial_bp.route('/create', methods=['POST'])
def createH():
    data = request.get_json()
    create(data.get("historial"))