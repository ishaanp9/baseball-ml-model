import os
import pymongo

# Playing Around with Mongodb

# NOTE: Task for 12/29/21
# Create MLB database
# Create collection for teams
# Create subcollection for individual teams
# Populate with players - with stats

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["MLB"]
collective_teams = mydb["Teams"]









