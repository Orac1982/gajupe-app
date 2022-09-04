from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from .api.routes import api_bp
from .dashboards.routes import dashboards_bp
from .students.routes import students_bp
from .datasets.routes import datasets_bp
from .workflows.routes import workflows_bp
from .reports.routes import reports_bp
from .security.routes import security_bp
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():

    # Create Flask App
    app = Flask(__name__)
    app.config.from_object('config')

    # Initialise extensions
    db.init_app(app)

    with app.app_context():

        # Import and register Blueprints
        from .api import routes
        from .dashboards import routes
        from .students import routes
        from .datasets import routes
        from .workflows import routes
        from .reports import routes
        from .security import routes
        app.register_blueprint(api_bp)
        app.register_blueprint(dashboards_bp)
        app.register_blueprint(students_bp)
        app.register_blueprint(datasets_bp)
        app.register_blueprint(workflows_bp)
        app.register_blueprint(reports_bp)
        app.register_blueprint(security_bp)

        # Create sql tables for data models
        db.create_all()

    return app
