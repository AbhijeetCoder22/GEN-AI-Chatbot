from flask import Blueprint,request
from ..service.login_service import loginservice
from ..Model.user_details import User_details

login_bp = Blueprint("login_routes",__name__)

@login_bp.route("/", methods=['POST'])
def ind():
    data = request.get_json()
    ui_login_details = loginservice()
    ui_user_cred = User_details()
    ui_user_cred.set_user_name(data['usrname'])
    ui_user_cred.set_pswd(data['pswd'])
    return ui_login_details.islogin(ui_user_cred)