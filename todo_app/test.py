#from data.session_items import get_items

# list_items = ['Task 1', 'Task 2', 'Task 3']



# print(list_items[1])


"""
def list_items():
    items = ["Messier 81", "StarBurst", "Black Eye", "Centarus A", "Whirlpool"]
    return items

def add_item(title):
    items = list_items()
    items.append(title)
    return items

print(add_item("Test"))
"""


from flask import Flask

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(debug=True)