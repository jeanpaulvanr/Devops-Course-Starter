import requests, os
from todo_app.data.item import Item

key = os.getenv("API_KEY")
token = os.getenv("API_TOKEN")
board_id = os.getenv("BOARD_ID")

def get_items_all():

    response = requests.get(f"https://api.trello.com/1/boards/{board_id}/lists?key={key}&token={token}&cards=open")
        
    response_json = response.json()

    return response_json

def get_items(status):

    list_of_cards =[]

    for trello_list_name in get_items_all():
        cards = trello_list_name["cards"]

        for card in cards:
            if trello_list_name["name"] == status:
                list_of_cards.append(Item.from_trello_card(card, trello_list_name))
                                                                  
    return list_of_cards

def get_do_items():
    
    list_of_cards_open = get_items('To Do')
                                                                  
    return list_of_cards_open

def get_doing_items():
    
    list_of_cards_in_progress = get_items('Doing')
                                                                  
    return list_of_cards_in_progress

def get_done_items():
    
    list_of_cards_closed = get_items('Done')
                                                                  
    return list_of_cards_closed

def add_item(title):

    for trello_list in get_items_all():
        if trello_list["name"] == "To Do":
            list_id = trello_list["id"]

    item = requests.post(f"https://api.trello.com/1/cards?idList={list_id}&key={key}&token={token}&name={title}")

    return item

def close_item(card_id):
    
    for trello_list in get_items_all():
        if trello_list["name"] == "Done":
            list_id = trello_list["id"]

    item = requests.put(f"https://api.trello.com/1/cards/{card_id}?idList={list_id}&key={key}&token={token}&board_id={board_id}")
    
    return item