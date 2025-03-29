import psycopg2

class Database:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        
        self.conn = psycopg2.connect(host = host, database = database, user = user, password = password)
        
        self.cursor = self.conn.cursor()
        self.conn.autocommit = True
        
    def post(self, query):
        try:
            self.cursor.execute(query)
        except Exception as err:
            print(err)