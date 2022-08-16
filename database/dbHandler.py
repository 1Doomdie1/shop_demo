import mysql.connector

class DBHandler():
    '''Database connection handler'''
    def __init__(self, user:str ='root', password:str='', host:str='localhost', database:str=''):
        self.__user = user
        self.__password = password
        self.__host = host
        self.__database_name = database
        self.cnx = None
        self.cursor = None

    def get_user(self):
        '''Returns the username used to connect to db'''
        return self.__user

    def get_password(self):
        '''Returns the password used to connect to db'''
        return self.__password
    
    def get_host(self):
        '''Returns the hostname used to connect to db'''
        return self.__host
    
    def get_database_name(self):
        '''Returns the database name'''
        return self.__database_name

    def connect(self):
        '''Connects to database and creates a cursor'''
        self.cnx = mysql.connector.connect(user=self.__user, password=self.__password, host=self.__host, database=self.__database_name)
        self.cursor = self.cnx.cursor()
    
    def disconect(self):
        '''Disconnects form database and distroyes cursor'''
        self.cnx.close()
        self.cursor.close()

