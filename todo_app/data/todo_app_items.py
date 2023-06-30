import pymongo
import datetime
import os
from todo_app.data.data_item import Data_Item

def connection_mongo():

    client = pymongo.MongoClient(os.getenv("CONNECTION_STRING"))
    
    db = client.jp_todoapp

    posts = db.posts
    
    return posts

def get_items_all():

    posts = connection_mongo()

    list_of_cards =[]

    for a_card in posts.find():
            list_of_cards.append(Data_Item.from_a_data_item(a_card, a_card))

    return list_of_cards

def add_item(title):
    
    posts = connection_mongo()
    
    post = {"item name": title,
            "status": "To Do",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}
                    
    ai_item = posts.insert_one(post).inserted_id

    return ai_item

def close_item(card_id):

    posts = connection_mongo()
       
    ci_item = posts.update_one({"_id": card_id}, {"$set": {"status": "Done"}})
    
    return ci_item