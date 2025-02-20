#This Client external Db Connection service layer
from ..Utils.dbconnection import Db_connection
from Query import insert_client_db_cred_query,get_client_db_cred_query,update_client_db_cred_query

main_db_obj = Db_connection()

class clientDBservice:
    def __init__(self):
        self.db_connect = main_db_obj.db_connection()

    def save_ClientDB_details(self,ui_obj,usr_id):
        params = (ui_obj.get_ext_db_type(),ui_obj.get_ext_db_server(),ui_obj.get_ext_db_usrname(),ui_obj.get_ext_db_pswd(),ui_obj.get_ext_db_name(),ui_obj.get_ext_db_port(),ui_obj.get_service_name(),ui_obj.get_driver(),usr_id)
        curr = self.db_connect[0]
        curr.execute(get_client_db_cred_query,(usr_id,))
        result = curr.fetchone()
        if not result:
            curr.execute(insert_client_db_cred_query,params)
            self.db_connect[1].commit()
            self.db_close_connection()
            return {"message":"Database Credential Saved Successfully"},201
        self.db_close_connection()
        return {'message':'Database canot be added again'},200
    
    def get_client_db_details(self,params):
        curr = self.db_connect[0]
        curr.execute(get_client_db_cred_query,params)
        result = curr.fetchone()
        creds_dict = dict()
        if result:
            col_arr = ['id','user_id','db_type','server','user','password','database_name','port','service_name','driver']
            for i in range(len(result)):
                creds_dict[col_arr[i]] = result[i]
            self.db_close_connection()
            return creds_dict
        self.db_close_connection()
        return {'message':'No Cred There'}
    
    def update_client_DB_creds(self,ui_obj,db_id,user_id):
        curr = self.db_connect[0]
        curr.execute(get_client_db_cred_query,(user_id,))
        result = curr.fetchone()
        if result:
            params = (ui_obj.get_ext_db_type(),ui_obj.get_ext_db_server(),ui_obj.get_ext_db_usrname(),ui_obj.get_ext_db_pswd(),ui_obj.get_ext_db_name(),ui_obj.get_ext_db_port(),ui_obj.get_service_name(),ui_obj.get_driver(),db_id,user_id)
            curr.execute(update_client_db_cred_query,params)
            self.db_close_connection()
            return {'message':'Updated Database Credential'},200
        self.db_close_connection()
        return {'message':'No Cred There'},200 
    
    def db_close_connection(self):
        main_db_obj.close_connection(self.db_connect[0],self.db_connect[1])