from flask import url_for
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.fields.html5 import DecimalRangeField
from wtforms.validators import InputRequired, Email, ValidationError, EqualTo, Length
from myranker.models import Alevel, Alevelgrade, Course


class AlsoHasData(object):  # --> Change to 'LessThan'
    """
    Compares the values of two fields.

    :param fieldname:
        The name of the other field to compare to.
    :param message:
        Error message to raise in case of a validation error. Can be
        interpolated with `%(other_label)s` and `%(other_name)s` to provide a
        more helpful error.
    """
    def __init__(self, fieldname, message=None):
        self.fieldname = fieldname
        self.message = message

    def __call__(self, form, field):
        try:
            other = form[self.fieldname]
        except KeyError:
            raise ValidationError(field.gettext("Invalid field name '%s'.") % self.fieldname)
        if field.data == '-' and other.data != '-':  #  --> Change to >= from !=
            d = {
                'other_label': hasattr(other, 'label') and other.label.text or self.fieldname,
                'other_name': self.fieldname
            }
            message = self.message
            if message is None:
                message = field.label() + ' required.'

            raise ValidationError(message)


class AlevelForm(FlaskForm):
    list_of_alevels = Alevel.query.all()
    alevels = [('-', 'A-Level')]
    for alevel in list_of_alevels:
        alevels.append((str(alevel.id), alevel.name))

    list_of_grades = Alevelgrade.query.all()
    grades = [('-', 'Grade')]
    for grade in list_of_grades:
        grades.append((str(grade.id), grade.grade))

    alevel_1 = SelectField('A-Level', choices=alevels, default='-', validators=[AlsoHasData('grade_1')])
    alevel_2 = SelectField('A-Level', choices=alevels, default='-', validators=[AlsoHasData('grade_2')])
    alevel_3 = SelectField('A-Level', choices=alevels, default='-', validators=[AlsoHasData('grade_3')])
    alevel_4 = SelectField('A-Level', choices=alevels, default='-', validators=[AlsoHasData('grade_4')])
    alevel_5 = SelectField('A-Level', choices=alevels, default='-', validators=[AlsoHasData('grade_5')])
    alevel_6 = SelectField('A-Level', choices=alevels, default='-', validators=[AlsoHasData('grade_6')])
    alevel_7 = SelectField('A-Level', choices=alevels, default='-', validators=[AlsoHasData('grade_7')])
    alevel_8 = SelectField('A-Level', choices=alevels, default='-', validators=[AlsoHasData('grade_8')])

    grade_1 = SelectField('Grade', choices=grades, default='-', validators=[AlsoHasData('alevel_1')])
    grade_2 = SelectField('Grade', choices=grades, default='-', validators=[AlsoHasData('alevel_2')])
    grade_3 = SelectField('Grade', choices=grades, default='-', validators=[AlsoHasData('alevel_3')])
    grade_4 = SelectField('Grade', choices=grades, default='-', validators=[AlsoHasData('alevel_4')])
    grade_5 = SelectField('Grade', choices=grades, default='-', validators=[AlsoHasData('alevel_5')])
    grade_6 = SelectField('Grade', choices=grades, default='-', validators=[AlsoHasData('alevel_6')])
    grade_7 = SelectField('Grade', choices=grades, default='-', validators=[AlsoHasData('alevel_7')])
    grade_8 = SelectField('Grade', choices=grades, default='-', validators=[AlsoHasData('alevel_8')])

    submit = SubmitField('Next →')

    def validate_alevel_1(self, alevel_1):
        if alevel_1.data == '-':
            raise ValidationError('Select at least one A-level.')


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


class PreferencesForm(FlaskForm):
    league_table_pref = DecimalRangeField('League Table Ranking', default=5)
    student_satisfaction_pref = DecimalRangeField('Student Satisfaction', default=5)
    employability_pref = DecimalRangeField('Employability', default=5)
    research_quality_pref = DecimalRangeField('Research Quality', default=5)
    student_to_staff_pref = DecimalRangeField('Student-to-Staff Ratio', default=5)
    cost_of_living_pref = DecimalRangeField('Cost of Living', default=5)
    international_student_pref = DecimalRangeField('High International Student Ratio', default=5)
    submit = SubmitField('Next →')
