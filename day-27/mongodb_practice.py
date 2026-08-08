import os
from flask import Flask
import pymongo
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
client = pymongo.MongoClient(MONGODB_URI)

print(client.list_database_names())
db = client["thirty_days_of_python"]

students = [
        {'name':'Anvesha','country':'India','city':'Mangalore','age':20},
        {'name':'Pratham','country':'India','city':'Mangalore','age':20},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
for student in students:
    db.students.insert_one(student)

student = db.students.find_one()
print(student)

students = db.students.find()
for student in students:
    print(student)

students = db.students.find({}, {"_id":0,  "name": 1, "country":1}) # 0 means not include and 1 means include
for student in students:
    print(student)

query = {'name':'Sami'}
db.students.delete_many(query)
for student in db.students.find():
    print(student)