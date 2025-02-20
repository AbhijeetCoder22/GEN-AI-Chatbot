#This is User Registration service layer
from ..Utils.dbconnection import Db_connection
import bcrypt
from .inputvalidation import InputValidator
from Query import user_creation_query,duplicate_check_query

main_db_obj = Db_connection()

class Register:
    def __init__(self):
        self.db_connect = main_db_obj.db_connection()

    def register_user(self,user_details):
        errors = self.__validate(user_details)
        if errors:
            return errors
        is_duplicate = self.__check_duplicate(user_details)
        if is_duplicate:
            self.__close_connection()
            return {"message":"Duplicate User Name or Email"},400
        hashed_pswd = self.__generate_hash_password(user_details.get_pswd())
        user_details.set_pswd(hashed_pswd.decode('utf-8'))
        curr = self.db_connect[0]
        curr.execute(user_creation_query,(user_details.get_full_name(),user_details.get_user_name(),user_details.get_mail_id(),user_details.get_pswd()))
        self.db_connect[1].commit()
        self.__close_connection()
        return {"message":"User Created"},201
    
    def __generate_hash_password(self,input_pswd):
        secret_key = "GenAicHatBot"
        input_pswd = input_pswd + secret_key
        salt = bcrypt.gensalt()
        hashed_pswd = bcrypt.hashpw(input_pswd.encode('utf-8'),salt)
        return hashed_pswd
    
    def __validate(self,user_details_obj):
        validation_obj = InputValidator(user_details_obj.get_full_name(),user_details_obj.get_user_name(),user_details_obj.get_mail_id(),user_details_obj.get_pswd())
        errors = validation_obj.validate_all()
        return errors 
    
    def __check_duplicate(self,user_details_obj):
        curr = self.db_connect[0]
        curr.execute(duplicate_check_query,(user_details_obj.get_user_name(),user_details_obj.get_mail_id()))
        result = curr.fetchone()
        if result[0]>0:
            return True
        return False
    
    def __close_connection(self):
        main_db_obj.close_connection(self.db_connect[0],self.db_connect[1])