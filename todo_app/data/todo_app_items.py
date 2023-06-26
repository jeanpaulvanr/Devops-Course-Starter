import pymongo
from pymongo import MongoClient
import datetime
import pprint
import dotenv 
import os
from todo_app.data.data_item import Data_Item

def get_items_all():

    dotenv.load_dotenv()

    client = MongoClient(os.getenv("CONNECTION_STRING"))

    db = client.jp_todoapp

    posts = db.posts

    list_of_cards =[]

    for a_card in posts.find():
            list_of_cards.append(Data_Item.from_a_data_item(a_card, a_card))

    return list_of_cards

def add_item(title):

    ai_item = requests.post(f"https://api.trello.com/1/cards?idList={todo_id()}&key={key()}&token={token()}&name={title}")

    return ai_item

def doing_item(card_id):
    
    di_item = requests.put(f"https://api.trello.com/1/cards/{card_id}?idList={doing_id()}&key={key()}&token={token()}&board_id={board_id()}")

    return di_item

def close_item(card_id):

    ci_item = requests.put(f"https://api.trello.com/1/cards/{card_id}?idList={done_id()}&key={key()}&token={token()}&board_id={board_id()}")
    
    return ci_item