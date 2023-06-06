from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.todo_app_items import get_items_all, add_item, close_item
from todo_app.flask_config import Config
from todo_app.data.view_model import ViewModel
from dotenv import load_dotenv

load_dotenv()

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        item_view_model = ViewModel(get_items_all())
        return render_template('index.html', view_model = item_view_model )

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
    
    return app
