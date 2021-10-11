import functools

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@auth_blueprint.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'johnko' and password == 'travoltanko':
            session.clear()
            session['user_id'] = {
                'username': 'johnko',
                'id': 1,
            }
            return redirect(url_for('index'))
        flash('Wronk creds!')
    return render_template('auth/login.html')


@auth_blueprint.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = 1


@auth_blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('.login'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
