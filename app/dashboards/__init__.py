from flask import Blueprint

# Blueprint Configuration
dashboards_bp = Blueprint(
    'dashboards_bp', __name__,
    template_folder='templates',
    static_folder='static'
)
