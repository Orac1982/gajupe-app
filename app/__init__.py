from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from .api.routes import api_bp
from .dashboards.routes import dashboards_bp
from .students.routes import students_bp
from .datasets.routes import datasets_bp
from .workflows.routes import workflows_bp
from .reports.routes import reports_bp
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
security = Security()


def create_app():

    # Create Flask App
    app = Flask(__name__)
    app.config.from_object('config')

    # Initialise extensions
    db.init_app(app)

    from app.models import User, Role
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    with app.app_context():

        # Import parts of our application
        from .api import routes
        from .dashboards import routes
        from .students import routes
        from .datasets import routes
        from .workflows import routes
        from .reports import routes

        # Register Blueprints
        app.register_blueprint(api_bp)
        app.register_blueprint(dashboards_bp)
        app.register_blueprint(students_bp)
        app.register_blueprint(datasets_bp)
        app.register_blueprint(workflows_bp)
        app.register_blueprint(reports_bp)

        # Create sql tables for data models
        db.create_all()

    return app
