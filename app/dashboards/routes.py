from flask import Blueprint, render_template

# Blueprint Configuration
dashboards_bp = Blueprint(
    'dashboards_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@dashboards_bp.route('/')
def index():
    return render_template('dashboards.html', title='Dashboard')
