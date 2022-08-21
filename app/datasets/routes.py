import os
import pandas as pd
from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory
# from app.models import db, Student, Grade

# Blueprint Configuration
datasets_bp = Blueprint(
    'datasets_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

#
# @datasets_bp.route('/datasets/grades')
# def list_grades():
#     grades = Grade.query
#     title = 'Datasets / Grades'
#     return render_template('grades.html', title=title, grades=grades)
#
#
# @datasets_bp.route('/datasets/import')
# def import_csv():
#     title = 'Import Datasets'
#     return render_template('import_csv.html', title=title)
#
#
# @datasets_bp.route('/datasets/import/upload_file', methods=['POST'])
# def upload_file():
#     # get the uploaded file
#     uploaded_file = request.files['file']
#     # if not empty
#     if uploaded_file.filename != '':
#         # set the file path
#         # file_path = os.path.join(config.UPLOAD_FOLDER, uploaded_file.filename)
#         # save the file
#         uploaded_file.save(uploaded_file.filename)
#         if int(request.form['type']) == 1:
#             parse_csv_students(uploaded_file.filename)
#         if int(request.form['type']) == 2:
#             parse_csv_grades(uploaded_file.filename)
#     return redirect('/datasets/import')
#
#
# def parse_csv_students(file_path):
#     # Use Pandas to parse the CSV file
#     csv_data = pd.read_csv(file_path)
#     # Loop through the rows and create a Student object for each row
#     for i, row in csv_data.iterrows():
#         student = Student(
#             usi=row['usi'],
#             school_code=row['school_code'],
#             lms_code=row['lms_code'],
#             first_name=row['first_name'],
#             last_name=row['last_name'],
#             dob=row['dob'],
#             year_level=row['year_level'],
#             roll_group_code=row['roll_group_code'],
#             active=row['active']
#         )
#         # Insert each grade into db
#         db.session.add(student)
#     db.session.commit()
#
#
# def parse_csv_grades(file_path):
#     csv_data = pd.read_csv(file_path)
#     for i, row in csv_data.iterrows():
#         grade = Grade(
#             student_usi=row['usi'],
#             timetable_period_code=row['timetable_period_code'],
#             report_type_label=row['report_type_label'],
#             programme_title=row['programme_title'],
#             subject_code=row['subject_code'],
#             mod_grade=row['moderated_grade']
#         )
#         db.session.add(grade)
#     db.session.commit()
#
#
# @datasets_bp.route('/app/static/downloads/<file>')
# def view_output_files(file):
#     filepath = os.path.abspath('app/static/downloads/')
#     return send_from_directory(filepath, file)
#
#
# @datasets_bp.route('/api/grades')
# def grades_all():
#     return {'data': [grade.to_dict() for grade in Grade.query]}
