#This is login service layer

from ..Model.user_details import User_details
from ..Utils.dbconnection import Db_connection
import bcrypt
from Query import user_details_fetch_query
from flask_jwt_extended import create_access_token

main_db_obj = Db_connection()

class loginservice:
    def __init__(self):
        self.db_connect = main_db_obj.db_connection()

    def islogin(self,ui_obj):
        curr = self.db_connect[0]
        curr.execute(user_details_fetch_query,(ui_obj.get_user_name(),))
        result = curr.fetchone()
        if result:
            db_user_details = User_details()
            db_user_details.set_userid(result[0])
            db_user_details.set_full_name(result[1])
            db_user_details.set_user_name(result[2])
            db_user_details.set_mail_id(result[3])
            db_user_details.set_pswd(result[4])
            self.db_close_connection()
            is_pswd_same = self.__check_stored_pswd_vs_ui_pswd(ui_obj.get_pswd(),db_user_details.get_pswd())
            if is_pswd_same:
                access_token = create_access_token(identity=str(db_user_details.get_userid()))
                return {"message":"Login Success","token":access_token},200
            return {"message":"Password Doesnt Match"},400
        return {"message":"No User Details"},400
    
    def __check_stored_pswd_vs_ui_pswd(self,input_pswd,stored_pswd):
        secret_key = "GenAicHatBot"
        input_pswd = input_pswd + secret_key
        return bcrypt.checkpw(input_pswd.encode('utf-8'), stored_pswd.encode('utf-8'))
    
    def db_close_connection(self):
        main_db_obj.close_connection(self.db_connect[0],self.db_connect[1])