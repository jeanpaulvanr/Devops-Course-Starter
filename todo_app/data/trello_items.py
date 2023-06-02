import requests, os
from todo_app.data.item import Item

def get_items_all():

    response = requests.get(f"https://api.trello.com/1/boards/{board_id()}/lists?key={key()}&token={token()}&cards=open")
        
    response_json = response.json()

    list_of_cards =[]

    for a_card in response_json:
        cards = a_card["cards"]

        for card in cards:
            list_of_cards.append(Item.from_a_card(card, a_card))

    return list_of_cards

def add_item(title):

    item = requests.post(f"https://api.trello.com/1/cards?idList={todo_id()}&key={key()}&token={token()}&name={title}")

    return item

def doing_item(card_id):
    
    item = requests.put(f"https://api.trello.com/1/cards/{card_id}?idList={doing_id()}&key={key()}&token={token()}&board_id={board_id()}")

    return item

def close_item(card_id):

    item = requests.put(f"https://api.trello.com/1/cards/{card_id}?idList={done_id()}&key={key()}&token={token()}&board_id={board_id()}")
    
    return item

def key():
    return os.getenv("API_KEY")

def token():
    return os.getenv("API_TOKEN")

def board_id():
    return os.getenv("BOARD_ID")

def todo_id():
    return os.getenv("TO_DO_ID")

def doing_id():
    return os.getenv("DOING_ID")

def done_id():
    return os.getenv("DONE_ID")