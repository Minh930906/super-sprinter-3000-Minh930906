from connectdatabase import ConnectDatabase
from models import Story

ConnectDatabase.db.connect()
ConnectDatabase.db.drop_tables([Story], safe=True)
ConnectDatabase.db.create_tables([Story], safe=True)