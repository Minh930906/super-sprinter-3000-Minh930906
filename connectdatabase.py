from peewee import *


class ConnectDatabase():

    def get_connect_string():
        try:
            with open('connect_str.txt',"r") as db_name:
                data=db_name.read()
                return data
        except:
            print("You need to create a database and store its name in a file named 'connect_str.txt'.")

    db = PostgresqlDatabase(get_connect_string(),user=get_connect_string())
