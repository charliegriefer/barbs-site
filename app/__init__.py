import os

from dotenv import load_dotenv
from flask import Flask

from app.extensions import cache

# Load environment variables from .env file
load_dotenv()


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object("config")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-key-for-testing")

    # Initialize extensions
    cache.init_app(app, config={"CACHE_TYPE": "SimpleCache"})

    # Import blueprints
    from app.blueprints.adopt.routes import adopt_bp
    from app.blueprints.donate.routes import donate_bp
    from app.blueprints.home.routes import home_bp
    from app.blueprints.shop.routes import shop_bp
    from app.blueprints.volunteer.routes import volunteer_bp

    # Register blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(donate_bp)
    app.register_blueprint(shop_bp)
    app.register_blueprint(adopt_bp)
    app.register_blueprint(volunteer_bp)

    return app


# Create the application instance
app = create_app()
