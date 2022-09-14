import requests, os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("API_KEY")
token = os.getenv("API_TOKEN")
board_id = os.getenv("BOARD_ID")

def get_items_all():

    response = requests.get(f"https://api.trello.com/1/boards/{board_id}/lists?key={key}&token={token}&cards=open")
        
    response_json = response.json()

    return response_json

def get_open_items():

    list_of_cards_open =[]

    for trello_list in get_items_all():
        list_name = trello_list["name"]
        cards = trello_list["cards"]

        for card in cards:
            if trello_list["name"] == "To Do" or trello_list["name"] == "Doing":
                trello_item = {
                    "title": card["name"],
                    "id": card["id"],
                    "status": list_name
                }
                list_of_cards_open.append(trello_item)
    
    return list_of_cards_open

def get_closed_items():
    
    list_of_cards_done =[]

    for trello_list in get_items_all():
        list_name = trello_list["name"]
        cards = trello_list["cards"]

        for card in cards:
            if trello_list["name"] == "Done":
                trello_item = {
                    "title": card["name"],
                    "id": card["id"],
                    "status": list_name
                }
                list_of_cards_done.append(trello_item)
    
    return list_of_cards_done