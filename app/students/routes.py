from flask import Blueprint, render_template, request, redirect, url_for
from flask import current_app as app
# from app import Student, Grade

students_bp = Blueprint(
    'students_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


# @students_bp.route('/students')
# def list_students():
#     students = Student.query
#     return render_template('students.html', title='Students', students=students)
#
#
# @students_bp.route('/student/<usi>')
# def get_student(usi):
#     student = Student.query.filter_by(usi=usi).first()
#     # student_id = student.id
#     grades = Grade.query.filter_by(student_usi=usi).all()
#     title = 'Students / ' + student.first_name + ' ' + student.last_name
#     return render_template('student_dashboard.html', title=title, student=student, grades=grades)
#
#
# @students_bp.route('/api/students')
# def students_all():
#     return {'data': [student.to_dict() for student in Student.query]}
