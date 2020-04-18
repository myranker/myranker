from flask import url_for
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import InputRequired, Email, ValidationError, EqualTo, Length
from myranker.models import Alevel, Alevelgrade, Course


class AlevelForm(FlaskForm):
    list_of_alevels = Alevel.query.all()
    alevels = [('-', 'A-Level')]
    for alevel in list_of_alevels:
        alevels.append((str(alevel.id), alevel.name))

    list_of_grades = Alevelgrade.query.all()
    grades = [('-', 'Grade')]
    for grade in list_of_grades:
        grades.append((str(grade.id), grade.grade))

    alevel_1 = SelectField('A-Level', choices=alevels, default='-')
    alevel_2 = SelectField('A-Level', choices=alevels, default='-')
    alevel_3 = SelectField('A-Level', choices=alevels, default='-')
    alevel_4 = SelectField('A-Level', choices=alevels, default='-')
    alevel_5 = SelectField('A-Level', choices=alevels, default='-')
    alevel_6 = SelectField('A-Level', choices=alevels, default='-')
    alevel_7 = SelectField('A-Level', choices=alevels, default='-')
    alevel_8 = SelectField('A-Level', choices=alevels, default='-')

    grade_1 = SelectField('Grade', choices=grades, default='-')
    grade_2 = SelectField('Grade', choices=grades, default='-')
    grade_3 = SelectField('Grade', choices=grades, default='-')
    grade_4 = SelectField('Grade', choices=grades, default='-')
    grade_5 = SelectField('Grade', choices=grades, default='-')
    grade_6 = SelectField('Grade', choices=grades, default='-')
    grade_7 = SelectField('Grade', choices=grades, default='-')
    grade_8 = SelectField('Grade', choices=grades, default='-')

    submit = SubmitField('Next →')


class CourseForm(FlaskForm):
    list_of_courses = Course.query.all()
    courses = [('-', 'Course')]
    for course in list_of_courses:
        courses.append((str(course.id), course.name))
    course = SelectField('Course', choices=courses, default='-')
    submit = SubmitField('Next →')

    def validate_course(self, course):
        if course.data == '-':
            raise ValidationError('Please select a course')
