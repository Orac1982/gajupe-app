from flask_security import UserMixin, RoleMixin
from app import db


roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grades = db.relationship('Grade', backref='student', lazy=True)
    checkpoints = db.relationship('Checkpoint', backref='student', lazy=True)
    reflections = db.relationship('Reflection', backref='reflection', lazy=True)
    usi = db.Column(db.String(64), index=True)
    school_code = db.Column(db.String(64))
    lms_code = db.Column(db.Integer)
    first_name = db.Column(db.String(256))
    last_name = db.Column(db.String(256))
    dob = db.Column(db.String(64))
    year_level = db.Column(db.Integer)
    roll_group_code = db.Column(db.String(16))
    active = db.Column(db.Boolean)

    def to_dict(self):
        return {
            'usi': self.usi,
            'school_code': self.school_code,
            'lms_code': self.lms_code,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'dob': self.dob,
            'year_level': self.year_level,
            'roll_group_code': self.roll_group_code,
            'active': self.active
        }


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    student_usi = db.Column(db.String, db.ForeignKey('student.usi'))
    timetable_period_code = db.Column(db.String(64))
    report_type_label = db.Column(db.String(64))
    programme_title = db.Column(db.String(64))
    subject_code = db.Column(db.String(64))
    mod_grade = db.Column(db.String(16))

    def to_dict(self):
        return {
            # 'student_id': self.student_id,
            'student_usi': self.student_usi,
            'timetable_period_code': self.timetable_period_code,
            'report_type_label': self.report_type_label,
            'programme_title': self.programme_title,
            'subject_code': self.subject_code,
            'mod_grade': self.mod_grade
        }
