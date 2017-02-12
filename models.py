from connectdatabase import ConnectDatabase
from peewee import *

class Story(Model):
    storytitle = CharField()
    userstory = CharField()
    criteria = CharField()
    businessvalue = IntegerField()
    estimation = FloatField()
    status = CharField()

    class Meta:
        database = ConnectDatabase.db
