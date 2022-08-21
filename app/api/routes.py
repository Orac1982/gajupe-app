from flask import Blueprint
# from app.models import Student

api_bp = Blueprint(
    'api_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


# @api_bp.route('/api/students')
# def students():
#     return {'data': [student.to_dict() for student in Student.query]}
