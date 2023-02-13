from peewee import *
from os import path
db_connection = path.dirname(path.relpath(__file__))
db = SqliteDatabase(path.join(db_connection,"Donald.db"))

# create a table called users in the database
class User(Model):
    name = CharField()
    email = CharField(unique =True)
    password = CharField()
    class Meta:
        database = db
User.create_table(fail_silently = True)



#create a table called products
class Product(Model):
    name = CharField()
    qty =CharField()
    price = CharField()

    class Meta:
        database = db

Product.create_table(fail_silently =True)


# create a table named employees

class Employee(Model):
    name = CharField()
    email = CharField()
    post = CharField()

    class Meta:
        database = db


Employee.create_table(fail_silently=True)




