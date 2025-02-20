from flask import Blueprint,request
from ..Model.user_details import User_details
from ..service.register_service import Register

register_bp = Blueprint("register_route",__name__)

@register_bp.route("/",methods=['POST'])
def register():
    data = request.get_json()
    register_obj = User_details()
    register_obj.set_full_name(data['full_name'])
    register_obj.set_mail_id(data['email'])
    register_obj.set_pswd(data['pswd'])
    register_obj.set_user_name(data['usrname'])
    register_service = Register()
    return register_service.register_user(register_obj)