import uuid

DB_NAME = 'chatapp'
DB_USER = 'postgres'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_PORT = 5432

MYSQL_DB_NAME = ''
MYSQL_DB_USER = ''
MYSQL_DB_PASSWORD = ''
MYSQL_DB_HOST = ''
MYSQL_DB_PORT = 0

TOKEN_MINUTE = 30

ENCRYPTION_KEY = JWT_SECRET_KEY = "GenAicHatBot" + str(uuid.getnode())


GOOGLE_GEN_AI_API_KEY = ""
