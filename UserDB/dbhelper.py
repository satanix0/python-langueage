import mysql.connector
import sys


class DBhelper:
    def __init__(self):

        try:
            self.conn = mysql.connector.connect(
                host="localhost", user="root", password="", database="users")

            self.mycursor = self.conn.cursor()
        except:
            print("Some Error occurred")
            sys.exit(1)
        else:
            print("Connected to database")

    def create_user(self, name, email, password):
        try:
            self.mycursor.execute(
                """INSERT INTO users VALUES (NULL, '{}', '{}', '{}'""".format(name, email, password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1

    def search(self, email, password):

        self.mycursor.execute(
            """SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'""".format(email, password))
        # fetches the returned values from the query
        data = self.mycursor.fetchall()
        print(data)
        return data