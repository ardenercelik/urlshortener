# main dosyası uygulamayı başlatıyor.
# uygulama yapısı Flask - application factories.
from flask import Flask
from .extensions import db
from .routes import short


def create_app(config_file="settings.py"):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)  # init db

    app.register_blueprint(short)



    return app
