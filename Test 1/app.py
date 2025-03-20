import os
import importlib
import inspect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config
from utils.error_handler import handle_exception
from api.base_resource import Resource

db = SQLAlchemy()
migrate = Migrate()

def install_resource(app, resource_module):
    if not resource_module:
        return

    try:
        resources = getattr(resource_module, 'resources', [])
        base_endpoint = getattr(resource_module, 'endpoint', '')
    except AttributeError:
        print(f"Warning: Module {resource_module.__name__} does not define 'resources' or 'endpoint'.")
        return

    for cls in resources:
        if not issubclass(cls, Resource):
            print(f"Warning: {cls.__name__} is not a subclass of Resource.")
            continue

        if not cls.endpoint:
            endpoint = base_endpoint
        else:
            endpoint = base_endpoint + cls.endpoint

        app.add_url_rule(endpoint, view_func=cls.as_view(cls.__name__))
        print(f"Registered endpoint: {endpoint} for resource: {cls.__name__}")

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_error_handler(Exception, handle_exception)

    # Install resources
    from api import accounts
    install_resource(app, accounts)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)