import pymongo
from pymongo import MongoClient
import datetime
import pprint
import dotenv 
import os

dotenv.load_dotenv()

client = MongoClient(os.getenv("CONNECTION_STRING"))

db = client.jp_todoapp

posts = db.posts

for post in posts.find({"status": "Doing"}):
      pprint.pprint(post)

'''post = {"item name": "An Item on the List In Progress",
        "status": "Doing",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
                
post_id = posts.insert_one(post).inserted_id'''