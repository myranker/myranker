from flask import current_app
from myranker import db

class Alevel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)


class Alevelgrade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(2), nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(8), nullable=False)

    alevel_1 = db.Column(db.Integer, db.ForeignKey('alevel.id'))
    alevel_2 = db.Column(db.Integer, db.ForeignKey('alevel.id'))
    alevel_3 = db.Column(db.Integer, db.ForeignKey('alevel.id'))
    alevel_4 = db.Column(db.Integer, db.ForeignKey('alevel.id'))
    alevel_5 = db.Column(db.Integer, db.ForeignKey('alevel.id'))
    alevel_6 = db.Column(db.Integer, db.ForeignKey('alevel.id'))
    alevel_7 = db.Column(db.Integer, db.ForeignKey('alevel.id'))
    alevel_8 = db.Column(db.Integer, db.ForeignKey('alevel.id'))

    grade_1 = db.Column(db.Integer, db.ForeignKey('alevelgrade.id'))
    grade_2 = db.Column(db.Integer, db.ForeignKey('alevelgrade.id'))
    grade_3 = db.Column(db.Integer, db.ForeignKey('alevelgrade.id'))
    grade_4 = db.Column(db.Integer, db.ForeignKey('alevelgrade.id'))
    grade_5 = db.Column(db.Integer, db.ForeignKey('alevelgrade.id'))
    grade_6 = db.Column(db.Integer, db.ForeignKey('alevelgrade.id'))
    grade_7 = db.Column(db.Integer, db.ForeignKey('alevelgrade.id'))
    grade_8 = db.Column(db.Integer, db.ForeignKey('alevelgrade.id'))

    course = db.Column(db.Integer, db.ForeignKey('course.id'))

    league_table_pref = db.Column(db.Integer)
    student_satisfaction_pref = db.Column(db.Integer)
    employability_pref = db.Column(db.Integer)
    research_quality_pref = db.Column(db.Integer)
    student_to_staff_pref = db.Column(db.Integer)
    cost_of_living_pref = db.Column(db.Integer)
    international_student_pref = db.Column(db.Integer)

    uni_1 = db.Column(db.Integer, db.ForeignKey('university.id'))
    uni_2 = db.Column(db.Integer, db.ForeignKey('university.id'))
    uni_3 = db.Column(db.Integer, db.ForeignKey('university.id'))
    uni_4 = db.Column(db.Integer, db.ForeignKey('university.id'))
    uni_5 = db.Column(db.Integer, db.ForeignKey('university.id'))
    uni_6 = db.Column(db.Integer, db.ForeignKey('university.id'))
    uni_7 = db.Column(db.Integer, db.ForeignKey('university.id'))
    uni_8 = db.Column(db.Integer, db.ForeignKey('university.id'))
    uni_9 = db.Column(db.Integer, db.ForeignKey('university.id'))
    uni_10 = db.Column(db.Integer, db.ForeignKey('university.id'))

    is_complete = db.Column(db.Boolean, nullable=False, default=False)


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
