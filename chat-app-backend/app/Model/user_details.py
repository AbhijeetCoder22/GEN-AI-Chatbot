#user details are stored and fetched in this class getter and setter methord 

class User_details:
    def __init__(self):
        self.__user_name = ""
        self.__mail_id = ""
        self.__full_name = ""
        self.__password = ""
        self.__userid = ""
        
    def set_user_name(self,name):
        self.__user_name = name

    def get_user_name(self):
        return self.__user_name
    
    def set_mail_id(self,mailid):
        self.__mail_id = mailid

    def get_mail_id(self):
        return self.__mail_id

    def set_full_name(self,fullname):
        self.__full_name = fullname

    def get_full_name(self):
        return self.__full_name

    def set_pswd(self,pswd):
        self.__password = pswd

    def get_pswd(self):
        return self.__password
    
    def set_userid(self,userid):
        self.__userid = userid

    def get_userid(self):
        return self.__userid