import re

class InputValidator:
    def __init__(self, fullname, username, mailid, password):
        self.__fullname = fullname
        self.__username = username
        self.__mailid = mailid
        self.__password = password
        self.errors = []

    def __validate_fullname(self):
        if not self.__fullname or not re.match(r"^[A-Za-z\s\-']+$", self.__fullname):
            self.errors.append("Full name must contain only letters, spaces, or hyphens.")

    def __validate_username(self):
        if not re.match(r"^[A-Za-z0-9_.]{3,30}$", self.__username):
            self.errors.append("Username must be 3-30 characters and can contain letters, numbers, underscores, or periods.")

    def __validate_mailid(self):
        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", self.__mailid):
            self.errors.append("Invalid email address.")

    def __validate_password(self):
        if len(self.__password) < 8:
            self.errors.append("Password must be at least 8 characters long.")
        if not re.search(r"[A-Z]", self.__password):
            self.errors.append("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", self.__password):
            self.errors.append("Password must contain at least one lowercase letter.")
        if not re.search(r"\d", self.__password):
            self.errors.append("Password must contain at least one number.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", self.__password):
            self.errors.append("Password must contain at least one special character.")

    def validate_all(self):
        self.errors = []
        self.__validate_fullname()
        self.__validate_username()
        self.__validate_mailid()
        self.__validate_password()
        return self.errors
    
    def validate_null_values(self,data):
        for key, value in data.items():
            if value is None:
                return True
        return False