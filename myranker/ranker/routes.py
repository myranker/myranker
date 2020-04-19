from flask import abort, render_template, url_for, redirect, flash, request, Blueprint
from myranker.models import User, Alevel, University
from myranker import db
from myranker.ranker.rank import rank

ranker = Blueprint('ranker', __name__)

@ranker.route('/alevels/<string:code>', methods=['GET', 'POST'])
def alevels(code):
    from myranker.ranker.forms import AlevelForm
    user = User.query.filter_by(code=code).first()
    if not user:
        return redirect(url_for('main.begin'))
    if user.is_complete:
        return redirect(url_for('ranker.results', code=code))
    form = AlevelForm()

    if user.alevel_1:
        form.alevel_1.default = str(user.alevel_1)
        form.grade_1.default = str(user.grade_1)

    if user.alevel_2:
        form.alevel_2.default = str(user.alevel_2)
        form.grade_2.default = str(user.grade_2)

    if user.alevel_3:
        form.alevel_3.default = str(user.alevel_3)
        form.grade_3.default = str(user.grade_3)

    if user.alevel_4:
        form.alevel_4.default = str(user.alevel_4)
        form.grade_4.default = str(user.grade_4)

    if user.alevel_5:
        form.alevel_5.default = str(user.alevel_5)
        form.grade_5.default = str(user.grade_5)

    if user.alevel_6:
        form.alevel_6.default = str(user.alevel_6)
        form.grade_6.default = str(user.grade_6)

    if user.alevel_7:
        form.alevel_7.default = str(user.alevel_7)
        form.grade_7.default = str(user.grade_7)

    if user.alevel_8:
        form.alevel_8.default = str(user.alevel_8)
        form.grade_8.default = str(user.grade_8)

    if form.validate_on_submit():
        if form.alevel_1.data == '-':
            user.alevel_1 = None
            user.grade_1 = None
        else:
            user.alevel_1 = int(form.alevel_1.data)
            user.grade_1 = int(form.grade_1.data)

        if form.alevel_2.data == '-':
            user.alevel_2 = None
            user.grade_2 = None
        else:
            user.alevel_2 = int(form.alevel_2.data)
            user.grade_2 = int(form.grade_2.data)

        if form.alevel_3.data == '-':
            user.alevel_3 = None
            user.grade_3 = None
        else:
            user.alevel_3 = int(form.alevel_3.data)
            user.grade_3 = int(form.grade_3.data)

        if form.alevel_4.data == '-':
            user.alevel_4 = None
            user.grade_4 = None
        else:
            user.alevel_4 = int(form.alevel_4.data)
            user.grade_4 = int(form.grade_4.data)

        if form.alevel_5.data == '-':
            user.alevel_5 = None
            user.grade_5 = None
        else:
            user.alevel_5 = int(form.alevel_5.data)
            user.grade_5 = int(form.grade_5.data)

        if form.alevel_6.data == '-':
            user.alevel_6 = None
            user.grade_6 = None
        else:
            user.alevel_6 = int(form.alevel_6.data)
            user.grade_6 = int(form.grade_6.data)

        if form.alevel_7.data == '-':
            user.alevel_7 = None
            user.grade_7 = None
        else:
            user.alevel_7 = int(form.alevel_7.data)
            user.grade_7 = int(form.grade_7.data)

        if form.alevel_8.data == '-':
            user.alevel_8 = None
            user.grade_8 = None
        else:
            user.alevel_8 = int(form.alevel_8.data)
            user.grade_8 = int(form.grade_8.data)

        db.session.commit()

        return redirect(url_for('ranker.course', code=code))
    form.process()

    return render_template('ranker/alevels.html.j2', title='A-levels', form=form)


@ranker.route('/course/<string:code>', methods=['GET', 'POST'])
def course(code):
    from myranker.ranker.forms import CourseForm
    user = User.query.filter_by(code=code).first()
    if not user:
        return redirect(url_for('main.begin'))
    if user.is_complete:
        return redirect(url_for('ranker.results', code=code))
    if not user.alevel_1:
        return redirect(url_for('ranker.alevels', code=code))
    form = CourseForm()
    if user.course:
        form.course.default = user.course
    if form.validate_on_submit():
        user.course = form.course.data
        db.session.commit()
        return redirect(url_for('ranker.preferences', code=code))
    form.process()
    return render_template('ranker/course.html.j2', title='Course', form=form, code=code)


@ranker.route('/preferences/<string:code>', methods=['GET', 'POST'])
def preferences(code):
    from myranker.ranker.forms import PreferencesForm
    user = User.query.filter_by(code=code).first()
    if not user:
        return redirect(url_for('main.begin'))
    if user.is_complete:
        return redirect(url_for('ranker.results', code=code))
    if not user.course:
        return redirect(url_for('ranker.course', code=code))
    form = PreferencesForm()
    if form.validate_on_submit():
        user.league_table_pref = int(form.league_table_pref.data)
        user.student_satisfaction_pref = int(form.student_satisfaction_pref.data)
        user.employability_pref = int(form.employability_pref.data)
        user.research_quality_pref = int(form.research_quality_pref.data)
        user.student_to_staff_pref = int(form.student_to_staff_pref.data)
        user.cost_of_living_pref = int(form.cost_of_living_pref.data)
        user.international_student_pref = int(form.international_student_pref.data)

        user.uni_1, user.uni_2, user.uni_3, user.uni_4, user.uni_5, user.uni_6, user.uni_7, user.uni_8, user.uni_9, user.uni_10 = rank(user)

        user.is_complete = True

        db.session.commit()

        return redirect(url_for('ranker.results', code=code))
    return render_template('ranker/preferences.html.j2', title='Preferences', form=form, code=code)


@ranker.route('/results/<string:code>')
def results(code):
    user = User.query.filter_by(code=code).first()
    if not user:
        return redirect(url_for('main.begin'))
    if not user.is_complete:
        return redirect(url_for('ranker.preferences', code=code))
    unis = [University.query.get(user.uni_1), University.query.get(user.uni_2), University.query.get(user.uni_3), University.query.get(user.uni_4), University.query.get(user.uni_5), University.query.get(user.uni_6), University.query.get(user.uni_7), University.query.get(user.uni_8), University.query.get(user.uni_9), University.query.get(user.uni_10)]
    return render_template('ranker/results.html.j2', title='Results', code=code, unis=unis)
