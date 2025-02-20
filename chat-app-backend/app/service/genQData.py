from .openai import Openai
from .clientDBservie import clientDBservice
from ..Utils.ext_DBConnection import ext_database_connection
import re

class GenQData:
    def __init__(self,user_id=None,question=None):
        self.__user_id = user_id
        self.__question = question

    def __get_prompt_query(self):
        Gen_Ai_Obj = Openai()
        param = (self.__user_id,)
        return Gen_Ai_Obj.input_text_to_data_generation(param,self.__question)
        
    def __get_ext_db_creds(self):
        client_db_service_obj = clientDBservice()
        params = (self.__user_id,)
        return client_db_service_obj.get_client_db_details(params)

    def get_client_data(self):
        try:
            generated_sql_query = self.__get_prompt_query()
            get_client_db_cred = self.__get_ext_db_creds()
            ext_db_connect = ext_database_connection(get_client_db_cred['db_type'],get_client_db_cred['server'],get_client_db_cred['user'],get_client_db_cred['password'],get_client_db_cred['database_name'],get_client_db_cred['port'])
            ext_db_connect.connect()
            clean_query = re.sub(r"```sql|```", "", generated_sql_query[0]).strip()
            result = ext_db_connect.execute_ext_db_query(clean_query)
            if result:
                return result
            return {'message':'No Result Found'}
        except Exception as e:
            if 'column' in str(e) and 'exist' in str(e):
                return {'message':"Column " + str(e).split('"')[1] +" doesnot Exist"}
            return {'message':'Error in connecting client Database'}
