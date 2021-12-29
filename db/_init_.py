import os
import pymongo

# Playing Around with Mongodb

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["family_data"]
my_collection = db["family_members"]

mydict = {"name": "Ishaan", "age": 19}
x = my_collection.insert_one(mydict)

print(x.inserted_id)