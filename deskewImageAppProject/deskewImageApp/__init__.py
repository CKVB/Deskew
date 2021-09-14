from flask import Flask

def create_app(configuration_file="settings.py"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(configuration_file)
    with app.app_context():
        from .views import deskew_api, swagger_ui
        app.register_blueprint(deskew_api)
        app.register_blueprint(swagger_ui)
        return app
