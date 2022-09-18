from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.trello_items import get_open_items, get_closed_items, add_item, close_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    return render_template('index.html', list_open_items=get_open_items(), list_closed_items=get_closed_items())

@app.route('/additem', methods=['POST'])
def additem():
    add_item(request.form.get('title'))
    return redirect(url_for('index'))

@app.route('/closeitem', methods=['POST'])
def closeitem():
    close_item(request.form.get('card_id'))
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()