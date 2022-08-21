from flask import Blueprint, render_template

# Blueprint Configuration
reports_bp = Blueprint(
    'reports_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@reports_bp.route('/')
def index():
    return render_template('reports.html', title='Reports')
