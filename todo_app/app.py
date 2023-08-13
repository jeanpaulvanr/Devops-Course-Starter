from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.todo_app_items import get_items_all, add_item, close_item
from todo_app.flask_config import Config
from todo_app.data.view_model import ViewModel
from loggly.handlers import HTTPSHandler
from logging import Formatter

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config())
    app.logger.setLevel(app.config['LOG_LEVEL'])
    if app.config['LOGGLY_TOKEN'] is not None:
        handler = HTTPSHandler(f'https://logs-01.loggly.com/inputs/{app.config["LOGGLY_TOKEN"]}/tag/todo-app')
    handler.setFormatter(
        Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
    )
    app.logger.addHandler(handler)
    
    @app.route('/')
    def index():
        var_view_model = ViewModel(get_items_all())
        return render_template('index.html', html_view_model = var_view_model )

    @app.route('/additem', methods=['POST'])
    def additem():
        log_add_item = request.form.get('title')
        add_item(log_add_item)
        app.logger.info('The following Item has been added: %s', log_add_item)
        return redirect(url_for('index'))

    @app.route('/closeitem', methods=['POST'])
    def closeitem():
        log_close_item = request.form.get('card_id')
        close_item(log_close_item)
        app.logger.info('The following Item has been closed: %s', log_close_item)
        return redirect(url_for('index'))

    if __name__ == "__main__":
        app.run()
    
    return app
