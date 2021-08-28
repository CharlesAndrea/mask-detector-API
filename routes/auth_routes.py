from flask import Blueprint, request
from authentication.auth import token_required
from controllers.auth_controller import login, signup, get_all_users

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def user_login(): 
    return login()


@auth_bp.route('/signup', methods=['POST'])
def signup_user():
    data = request.form
    signup(data)

@auth_bp.route('/empleado', methods=['GET'])
@token_required
def get_users():
    get_all_users()
