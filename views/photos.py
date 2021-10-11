import functools

from flask import (
    Blueprint,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

from .auth import login_required


photos_blueprint = Blueprint('photos', __name__, url_prefix='/photos')


@photos_blueprint.route('/list', methods=['GET'])
@login_required
def read():
    return render_template('base.html')
