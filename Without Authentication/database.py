import sqlite3
from query import table_list # Define the database table list
from query import queries # Define the database queries

class DatabaseManager:
    def __init__(self, db_source, table_list, queries):
        self.db_source = db_source
        self.table_list = table_list
        self.queries = queries
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_source)
            print('Connected to SQLite Database')
            return self.connection.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to SQLite Database: {e}")
            return None

    def check_table_existence(self, cursor, table_name):
        try:
            check_query = f"SELECT EXISTS (SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}') AS result"
            cursor.execute(check_query)
            row = cursor.fetchone()
            return row[0] == 1
        except sqlite3.Error as e:
            print(f"Error checking table existence: {e}")
            return False

    def create_table(self, cursor, table_name, query):
        try:
            cursor.execute(query)
            print(f"Table '{table_name}' created successfully")
        except sqlite3.Error as e:
            print(f"Error creating table '{table_name}': {e}")

    def initialize_database(self):
        cursor = self.connect()
        if cursor is None:
            print("Unable to initialize database.")
            return None

        try:
            for table, query in zip(self.table_list, self.queries):
                if not self.check_table_existence(cursor, table):
                    print(f"Table '{table}' does not exist")
                    self.create_table(cursor, table, query)
                else:
                    print(f"Table '{table}' already exists")
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")

    def close_connection(self):
        if self.connection:
            self.connection.commit()
            self.connection.close()
            print("Connection to SQLite Database closed")
        else:
            print("No active connection to close")

# Define the database source
DBSource = './vms_db.db'

# Create a DatabaseManager instance
db_manager = DatabaseManager(DBSource, table_list, queries)

# Initialize the database
db_manager.initialize_database()

# Close the database connection
db_manager.close_connection()
