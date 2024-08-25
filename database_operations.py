
import sqlite3

class DatabaseOperations:
    def __init__(self, db_name='database.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (" + ', '.join(columns) + ');'
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def insert_data(self, table_name, data):
        placeholders = ', '.join(['?'] * len(data))
        columns = ', '.join(data.keys())
        values = tuple(data.values())
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(insert_query, values)
        self.conn.commit()

    def fetch_data(self, table_name, condition=None):
        query = f"SELECT * FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()

# Example usage:
# db = DatabaseOperations()
# db.create_table('replies', ['keyword', 'reply'])
# db.insert_data('replies', {'keyword': '关键字1', 'reply': '回复内容1'})
# data = db.fetch_data('replies')
# print(data)
# db.close_connection()
