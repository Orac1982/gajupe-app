from flask import Blueprint, render_template

# Blueprint Configuration
workflows_bp = Blueprint(
    'workflows_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@workflows_bp.route('/')
def index():
    return render_template('workflows.html', title='Workflows')
