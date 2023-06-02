import pymongo
import datetime
import pprint
import dotenv 
import os

# Change so secrets aren't revealed

dotenv.load_dotenv()

client = pymongo.MongoClient(os.getenv("CONNECTION_STRING"))

db = client.jp_todoapp

'''post = {"item name": "Another Item on the List",
        "status": "To Do",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}'''

posts = db.posts
#post_id = posts.insert_one(post).inserted_id

for post in posts.find({"status": "To Do"}):
      pprint.pprint(post)
