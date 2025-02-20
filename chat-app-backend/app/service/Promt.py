#This is Promt Layer

from ..Utils.dbconnection import Db_connection
from Query import add_promt_query,get_promt_query,delete_prompt_query,update_prompt_query,get_only_prompt_query

main_db_obj = Db_connection()

class Promt:
    def __init__(self):
        self.db_connect = main_db_obj.db_connection()

    def add_promt_to_tbl(self,params):
        curr = self.db_connect[0]
        curr.execute(add_promt_query,params)
        self.db_connect[1].commit()
        self.__close_connection()
        return {"message":"Prompt Added"},201

    def get_prompt_from_tbl(self,params):
        curr = self.db_connect[0]
        curr.execute(get_promt_query,params)
        result = curr.fetchall()
        self.__close_connection()
        if result:
            return result
        return {"message":"No Prompts"},400

    def update_promt(self,param):
        curr = self.db_connect[0]
        curr.execute(update_prompt_query,param)
        self.db_connect[1].commit()
        self.__close_connection()
        return {"message":"Prompt Updated"},200

    def delete_promt(self,param):
        curr = self.db_connect[0]
        curr.execute(delete_prompt_query,param)
        self.db_connect[1].commit()
        self.__close_connection()
        return {"message":"Prompt Deleted"},200

    def get_only_prompt(self,params):
        curr = self.db_connect[0]
        curr.execute(get_only_prompt_query,params)
        result = curr.fetchall()
        self.__close_connection()
        if result:
            type_to_prompt_map = dict()
            for i in result:
                if i[1] not in type_to_prompt_map:
                    type_to_prompt_map[i[1]] = []
                type_to_prompt_map[i[1]].append(i[0])
            return type_to_prompt_map
        return {"message":"No Prompts"},400

    def __close_connection(self):
        main_db_obj.close_connection(self.db_connect[0],self.db_connect[1])     