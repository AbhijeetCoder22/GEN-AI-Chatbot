#This class is to establish database connection returns cursor 

import psycopg2
import mysql.connector
from config import *

class Db_connection:
    def __init__(self):
        self.__dbhost = MYSQL_DB_HOST if MYSQL_DB_USER else DB_HOST
        self.__dbname = MYSQL_DB_NAME if MYSQL_DB_USER else DB_NAME
        self.__dbuser = MYSQL_DB_USER if MYSQL_DB_USER else DB_USER
        self.__dbpswd = MYSQL_DB_PASSWORD if MYSQL_DB_USER else DB_PASSWORD
        self.__dbport = MYSQL_DB_PORT if MYSQL_DB_USER else DB_PORT if DB_PORT else ""
        self.__db_type = 'mysql' if MYSQL_DB_USER else 'postgresql'
            
    def __mysql_connection(self):
        #Establish a connection to MySQL database
        try:
            connection = mysql.connector.connect(
                host=self.__dbhost,
                database=self.__dbname,
                port=self.__dbport,
                user=self.__dbuser,
                password=self.__dbpswd
            )
            if connection.is_connected():
                cursor = connection.cursor()
                return cursor, connection
        except mysql.connector.Error as e:
            print(f"MySQL Error: {e}")
            return None, None
        
    def __postgresql_connection(self):
        #Establish a connection to PostgreSQL database
        try:
            connection = psycopg2.connect(
                host=self.__dbhost,
                database=self.__dbname,
                port=self.__dbport,
                user=self.__dbuser,
                password=self.__dbpswd
            )
            cursor = connection.cursor()
            return cursor, connection
        except psycopg2.Error as e:
            return None, None

    def db_connection(self):
        #Establish a database connection based on the configured database type.
        #Returns the cursor and connection if successful, otherwise None.
        if self.__db_type == 'mysql':
            return self.__mysql_connection()
        elif self.__db_type == 'postgresql':
            return self.__postgresql_connection()
        
    def close_connection(self,cursor,connection):
        try:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        except Exception as e:
            print(f"Error while closing connection: {e}")