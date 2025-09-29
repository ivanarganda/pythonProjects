import sqlite3

database = './concesionary.sqlite'

class DB:

    def __init__(self):

        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def execute(self, query, params=()):

        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor

    def fetchall(self):

        return self.cursor.fetchall()

    def fetchone(self):

        return self.cursor.fetchone()

    def close(self):

        self.connection.close()