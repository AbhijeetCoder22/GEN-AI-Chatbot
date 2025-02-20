import pyodbc
import cx_Oracle
import mysql.connector
import psycopg2

class ext_database_connection:
    def __init__(self,db_type,host=None,user_name=None,pswd=None,database=None,port=None,service_name=None,driver=None):
        self.__db_type = db_type.lower()
        self.conn = None
        self.cursor = None
        self.__host_name = host
        self.__user = user_name
        self.__password = pswd
        self.__database = database
        self.__port = port
        self.__service_name = service_name
        self.__driver = driver

    def __validation_input(self):
        if self.__db_type in ['mysql','postgresql','oracle','mssql']:
            for property in [self.__host_name,self.__user,self.__password,self.__port]:
                if not property:
                    return False
        else:
            return False
        return True

    def __mysql_ext_connection(self):
        if self.__validation_input():
            self.conn = mysql.connector.connect(
                host=self.__host_name,
                database=self.__database,
                port=self.__port,
                user=self.__user,
                password=self.__password
                )
            self.cursor = self.conn.cursor()

    def __postgresql_ext_connection(self):
        if self.__validation_input():
            self.conn = psycopg2.connect(
                host=self.__host_name,
                database=self.__database,
                port=self.__port,
                user=self.__user,
                password=self.__password
            )
            self.cursor = self.conn.cursor()

    def __mssql_ext_connection(self):
        if self.__validation_input():
            if self.__driver:
                conn_str = f"DRIVER={self.__driver};SERVER={self.__host_name},{self.__port};DATABASE={self.__database};UID={self.__user};PWD={self.__password}"
                self.conn = pyodbc.connect(conn_str)
                self.cursor = self.conn.cursor()

    def __oracle_ext_connection(self):
        if self.__validation_input():
            if self.__service_name:
                dsn = cx_Oracle.makedsn(self.__host_name,self.__port,self.__service_name)
                self.conn = cx_Oracle.connect(self.__user,self.__password,dsn)
                self.cursor = self.conn.cursor()

    def connect(self):
        try:
            if self.__db_type == 'mysql':
                self.__mysql_ext_connection()
            elif self.__db_type == 'oracle':
                self.__oracle_ext_connection()
            elif self.__db_type == 'mssql':
                self.__mssql_ext_connection()
            elif self.__db_type == 'postgresql':
                self.__postgresql_ext_connection()
            else:
                raise ValueError(f"Unsupported {self.__db_type} database")
            
            self.cursor = self.conn.cursor()

        except Exception as e:
            print(e)
            return {'message':f'Cannot connect external {self.__db_type} Database'}
        
    def __close_ext_db_connection(self):
        self.cursor.close()
        self.conn.close()
        
    def execute_ext_db_query(self,query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.__close_ext_db_connection()
        return result