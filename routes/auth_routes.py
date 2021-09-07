from flask import Blueprint, request
#from flask.helpers import make_response
from authentication.auth import token_required
from controllers.auth_controller import login, signup, get_all_users
from flask_cors import cross_origin

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('login', methods=['POST'])
@cross_origin(origins='*',
    allow_headers='Content-Type',
    methods="POST",
    supports_credentials=True
)
def user_login(): 
    return login()


@auth_bp.route('signup', methods=['POST'])
def signup_user():
    data = request.form
    return signup(data)

@auth_bp.route('empleado', methods=['GET'])
@token_required
def get_users(current_user):
    get_all_users(current_user)

