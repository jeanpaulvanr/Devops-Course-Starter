import pymongo
import datetime

# Change so secrets aren't revealed
client = pymongo.MongoClient("mongodb://jpvan:FQihihBkCCrZg9ZX91ng7XYgkQlXrENHe7pgqeDGuj3IjX51f6qFxChXZgRrroCYGeNp8uQPEXVcACDbeaa5TQ==@jpvan.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@jpvan@")

db = client.jp_todoapp

post = {"item name": "Another Item on the List",
        "status": "To Do",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
