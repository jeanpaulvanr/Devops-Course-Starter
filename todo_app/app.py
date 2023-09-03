import os
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_required, login_user
import flask_login
import requests
from todo_app.data import user
from todo_app.data.todo_app_items import get_items_all, add_item, close_item
from todo_app.flask_config import Config
from todo_app.data.view_model import ViewModel
from loggly.handlers import HTTPSHandler
from logging import Formatter

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config())
    app.logger.setLevel(app.config['LOG_LEVEL'])
    if app.config['LOGGING_SERVICE_TOKEN'] is not None:
        handler = HTTPSHandler(f'https://logs-01.loggly.com/inputs/{app.config["LOGGING_SERVICE_TOKEN"]}/tag/todo-app')
        handler.setFormatter(Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s"))
        app.logger.addHandler(handler)
    
    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthenticated():
        client_id = os.getenv('GITHUB_CLIENT_ID')
        return redirect(f"https://github.com/login/oauth/authorize?client_id={client_id}")

    @login_manager.user_loader
    def load_user(user_id):
        
        return user.User(user_id)

    login_manager.init_app(app)
    
    @app.route('/')
    @login_required
    def index():
        var_view_model = ViewModel(get_items_all())
        return render_template('index.html', html_view_model = var_view_model )

    @app.route('/login/callback')
    def login():
        authorisation_code =  request.args.get('code')
        
        client_id = os.getenv('GITHUB_CLIENT_ID')
        client_secret = os.getenv('GITHUB_CLIENT_SECRET')
        
        params = {
            "client_id": client_id,
            "client_secret": client_secret,
            "code": authorisation_code            
        }
        
        headers = {
                "Accept": "application/json"
        }
        
        response = requests.post(f"https://github.com/login/oauth/access_token", params = params, headers = headers)

        access_token = response.json()["access_token"]

        headers = {
                "Authorization": f"Bearer {access_token}"
        }
        
        user_data_response = requests.get("https://api.github.com/user", headers = headers)

        #print(user_data_response)

        user_id = user_data_response.json()["id"]

        login_user(user.User(user_id))

        return redirect(url_for('index'))

    @app.route('/additem', methods=['POST'])
    @login_required
    def additem():
        log_add_item = request.form.get('title')
        id = add_item(log_add_item)
        app.logger.info('The following Item has been added: %s', id)
        return redirect(url_for('index'))

    @app.route('/closeitem', methods=['POST'])
    @login_required
    def closeitem():
        log_close_item = request.form.get('card_id')
        close_item(log_close_item)
        app.logger.info('The following Item has been closed: %s', log_close_item)
        return redirect(url_for('index'))

    if __name__ == "__main__":
        app.run()
    
    return app