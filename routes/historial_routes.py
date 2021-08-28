from flask import Blueprint, request
from controllers.historial_controller import create_record

historial_bp = Blueprint('historial_bp', __name__)

@historial_bp.route('/create', methods=['POST'])
def createH():
    data = request.get_json()
    create_record(data.get("historial"))