from config import GOOGLE_GEN_AI_API_KEY
import google.generativeai as GenAi
from .Promt import Promt

class Openai:
    def __init__(self):
        GenAi.configure(api_key = GOOGLE_GEN_AI_API_KEY)
        self.__Model = GenAi.GenerativeModel("gemini-pro")

    def input_text_to_data_generation(self,params,question):
        test_obj = Promt()
        promts = test_obj.get_only_prompt(params)
        sql_prompt = promts['SQL PROMPT']
        generated_queries = dict()
        for i in range(len(sql_prompt)):
            generated_queries[i] = self.__generate_response(sql_prompt[i],question)
        return generated_queries

    def __generate_response(self,promt,question):
        response = self.__Model.generate_content([promt,question])
        return response.text 