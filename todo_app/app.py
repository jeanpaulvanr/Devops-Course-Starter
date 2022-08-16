from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    return render_template('index.html', list_items=get_items())

@app.route('/additem', methods=['GET', 'POST'])
def additem():
    if request.method == 'POST':
        add_item(request.form.get('title'))
        return redirect(url_for('index'))
    
if __name__ == "__main__":
    app.run(debug=True)
  
#How does it know to run app.py and not the other .py files? e.g. the test one I made.
#What is Poetry really? Read up on this more.
#Check that item.id in html relates to id in session items
#Check that 'title' in request.form.get above relates to name="title" in html

"""
#1.
def list_items():
    items = ["Messier 81", "StarBurst", "Black Eye", "Centarus A", "Whirlpool"]
    return items
# No longer required as code has moved on. Remember that list_items=this function i.e. list_items()

#2. This code worked - remember it for any text file manipulation, especially the OS import piece. HTML may have changed to affect it now.

import os

def add_item(newitem):
    with open(os.path.join(app.root_path, "list.txt"), 'a') as f:
        return f.write('\n' + newitem)

@app.route('/additem', methods=['GET', 'POST'])
def additem():
    if request.method == 'POST':
        add_item(request.form.get("title"))
        return redirect(url_for('index'))
        # return 'A POST request was made'
    elif request.method == 'GET':
        return 'A GET request was made'
    else:
        return 'Not a valid request method for this route'

@app.route('/')
def index():
    with open(os.path.join(app.root_path, "list.txt"), 'r') as f:
        return render_template('index.html', list_items=f.readlines())

"""