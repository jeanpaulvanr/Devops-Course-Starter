import requests
import os

key = os.getenv("API_KEY")
token = os.getenv("API_TOKEN")
board_id = os.getenv("BOARD_ID")

#response = requests.get(f"https://api.trello.com/1/boards/{board_id}/lists?key={key}&token={token}&cards=all")

response = requests.get(f"https://api.trello.com/1/boards/sb0NVnTP/lists?key=cb25b32fe9619e59b4a7445d8f4b80f4&token=430ec4388718ead2e2017b24c724576eb2a0cd6cf066efdc439229288245e7b0&cards=all")

response_json = response.json()

list_of_cards =[]

for trello_list in response_json:
    list_name = trello_list["name"]
    cards = trello_list["cards"]

#how does the above for loop link to the bottom for loop? i.e. loop once top and then go through cards? Or loop through top creating 'full' list_name and cards? But then how does the status know the list_name if that's the case?
#why define list_of_cards but not list_name? Or is that because you are defining a list? Does this answer my above question and the for loop steps into the second for loop before stepping back to start the next round of looping?

    for card in cards:
        item = {
            "title": card["name"],
            "id": card["id"],
            "status": list_name
        }
        list_of_cards.append(item)

for c in list_of_cards:
    print(c)
