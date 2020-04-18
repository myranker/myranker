from flask import abort, render_template, url_for, redirect, flash, request, Blueprint
from myranker import db
from myranker.models import User
import random

main = Blueprint('main', __name__)

def generate_user_code():
    letters = '0123456789abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(letters) for i in range(8))


@main.route('/')
def index():
    return render_template('index.html.j2')


@main.route('/begin')
def begin():
    code = generate_user_code()
    while (User.query.filter_by(code=code).first()):
        code = generate_user_code()

    user = User(code=code)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('ranker.alevels', code=code))
