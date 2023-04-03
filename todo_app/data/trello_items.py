import requests, os
from todo_app.data.item import Item

key = os.getenv("API_KEY")
token = os.getenv("API_TOKEN")
board_id = os.getenv("BOARD_ID")
todo_id = os.getenv("TO_DO_ID")
doing_id = os.getenv("DOING_ID")
done_id = os.getenv("DONE_ID")

def get_items_all():

    response = requests.get(f"https://api.trello.com/1/boards/{board_id}/lists?key={key}&token={token}&cards=open")
        
    response_json = response.json()

    list_of_cards =[]

    for trello_list_name in response_json:
        cards = trello_list_name["cards"]

        for card in cards:
            list_of_cards.append(Item.from_trello_card(card, trello_list_name))

    return list_of_cards

def add_item(title):

    item = requests.post(f"https://api.trello.com/1/cards?idList={todo_id}&key={key}&token={token}&name={title}")

    return item

def doing_item(card_id):
    
    item = requests.put(f"https://api.trello.com/1/cards/{card_id}?idList={doing_id}&key={key}&token={token}&board_id={board_id}")

    return item

def close_item(card_id):

    item = requests.put(f"https://api.trello.com/1/cards/{card_id}?idList={done_id}&key={key}&token={token}&board_id={board_id}")
    
    return item