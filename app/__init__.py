from flask import Flask

from app.blueprints.adopt.routes import adopt_bp
from app.blueprints.donate.routes import donate_bp
from app.blueprints.home.routes import home_bp
from app.blueprints.shop.routes import shop_bp


def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(donate_bp)
    app.register_blueprint(shop_bp)
    app.register_blueprint(adopt_bp)

    return app
