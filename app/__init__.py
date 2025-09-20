from flask import Flask


def create_app():
    app = Flask(__name__)

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
