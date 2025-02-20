#client database are stored and fetched from this class getter and setter method

class ClientDb:
    def __init__(self):
        self.__database_type = ''
        self.__server = ''
        self.__server_port = ''
        self.__database_name = ''
        self.__user_name = ''
        self.__pswd = ''
        self.__service_name = ''
        self.__driver = ''

    def set_service_name(self,service_name):
        self.__service_name = service_name

    def get_service_name(self):
        return self.__service_name
    
    def set_driver_name(self,driver):
        self.__driver = driver

    def get_driver(self):
        return self.__driver

    def set_ext_db_type(self,type):
        self.__database_type = type

    def set_ext_db_server(self,server):
        self.__server = server
    
    def set_ext_db_port(self,port):
        self.__server_port = port

    def set_ext_db_name(self,database):
        self.__database_name = database

    def set_ext_db_user_name(self,user):
        self.__user_name = user

    def set_ext_db_pswd(self,pswd):
        self.__pswd = pswd

    def get_ext_db_type(self):
        return self.__database_type
    
    def get_ext_db_server(self):
        return self.__server
    
    def get_ext_db_port(self):
        return self.__server_port
    
    def get_ext_db_name(self):
        return self.__database_name
    
    def get_ext_db_usrname(self):
        return self.__user_name
    
    def get_ext_db_pswd(self):
        return self.__pswd