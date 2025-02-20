#This is api route layer

from flask import Blueprint,request
from flask_jwt_extended import jwt_required,get_jwt_identity
from ..service.Promt import Promt
from ..Model.client_db_details import ClientDb
from ..service.clientDBservie import clientDBservice
from ..service.inputvalidation import InputValidator
from ..service.genQData import GenQData

api_bp = Blueprint("api_route",__name__)

@api_bp.route("/get-client-data", methods=['POST'])
@jwt_required()
def api_end_point():
    print("api route")
    auth_header = request.headers.get('Authorization')
    if request.method == 'POST' and auth_header:
        data = request.get_json()
        curr_usr_id = get_jwt_identity()
        get_client_data_obj = GenQData(curr_usr_id,data['question'])
        return get_client_data_obj.get_client_data()


@api_bp.route("/promt", methods=['POST','GET','PUT','DELETE'])
@jwt_required()
def api_add_example_for_promt():
    print("Prompt Route")
    if request.method == 'GET':
        curr_usr_id = get_jwt_identity()
        params = (curr_usr_id,)
        get_prompt_obj = Promt()
        return get_prompt_obj.get_prompt_from_tbl(params)
    if request.method == 'POST':
        data = request.get_json()
        curr_usr_id = get_jwt_identity()
        params = (data['prompt_name'],data['prompt_text'],data['prompt_type'],curr_usr_id)
        add_promt_obj = Promt()
        return add_promt_obj.add_promt_to_tbl(params)
    if request.method == 'PUT':
        curr_usr_id = get_jwt_identity()
        data = request.get_json()
        update_promt_obj = Promt()
        params = (data['promt_text'],data['promt_id'],curr_usr_id)
        return update_promt_obj.update_promt(params)
    if request.method == 'DELETE':
        curr_usr_id = get_jwt_identity()
        data = request.get_json()
        delete_promt_obj = Promt()
        params = (data['promt_id'],curr_usr_id)
        return delete_promt_obj.delete_promt(params)
    
@api_bp.route("/client-db", methods=['POST','GET','PUT','DELETE'])
@jwt_required()
def client_db():
    if request.method == 'GET':
        curr_usr_id = get_jwt_identity()
        client_db_service_obj = clientDBservice()
        params = (curr_usr_id,)
        return client_db_service_obj.get_client_db_details(params)
    elif request.method == 'POST':
        data = request.get_json()
        client_db_obj = ClientDb()
        client_db_obj.set_ext_db_type(data['type'])
        client_db_obj.set_ext_db_server(data['server'])
        client_db_obj.set_ext_db_port(data['port'])
        client_db_obj.set_ext_db_name(data['database'])
        client_db_obj.set_ext_db_user_name(data['user'])
        client_db_obj.set_ext_db_pswd(data['pswd'])
        client_db_obj.set_driver_name(data['driver'])
        client_db_obj.set_service_name(data['service_name'])
        curr_usr_id = get_jwt_identity()
        client_db_service_obj = clientDBservice()
        return client_db_service_obj.save_ClientDB_details(client_db_obj,curr_usr_id)
    elif request.method == 'PUT':
        data = request.get_json()
        client_db_obj = ClientDb()
        client_db_obj.set_ext_db_type(data['type'])
        client_db_obj.set_ext_db_server(data['server'])
        client_db_obj.set_ext_db_port(data['port'])
        client_db_obj.set_ext_db_name(data['database'])
        client_db_obj.set_ext_db_user_name(data['user'])
        client_db_obj.set_ext_db_pswd(data['pswd'])
        client_db_obj.set_driver_name(data['driver'])
        client_db_obj.set_service_name(data['service_name'])
        curr_usr_id = get_jwt_identity()
        client_ui_service_obj = clientDBservice()
        return client_ui_service_obj.update_client_DB_creds(client_db_obj,data['id'],curr_usr_id)