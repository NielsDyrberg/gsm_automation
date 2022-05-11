
"""
Database execution

"""


from ExecutersInterface import ExecutersInterface
import mysql.connector
from decouple import config

class DatabaseExecution(ExecutersInterface):
    def __init__(self):
        mydb = mysql.connector.connect(
            host = config('DB_HOST', default=''),
            user = config('DB_USER', default=''),
            password = config('DB_PASSWORD', default=''),
        )
        mycursor = mydb.cursor()

        #mycursor.execute("CREATE DATABASE mydatabaseTWO") # !!!DANGER!!!

    def execute(self):
        pass


if __name__ == "__main__":
    dbe = DatabaseExecution()
    dbe.execute()