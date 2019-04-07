from flask import Flask
from instance.config import Config


def create_app(config=Config):

	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(config)

	from .db import db
	db.init_app(app)

	from .main import bp
	app.register_blueprint(bp)

	return app
