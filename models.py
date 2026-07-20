from peewee import *

db = SqliteDatabase('db.sqlite')


class BaseModel(Model):
    class Meta:
        database = db



class Company(BaseModel):
    name = CharField(unique=True)
    password = CharField()

class Product(BaseModel):
    name = CharField(unique=True)
    price = FloatField()
    category = CharField()
    company = ForeignKeyField(Company, backref="products")





def init_db():
    db.connect()
    db.create_tables([Company, Product])
    