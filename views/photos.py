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


photos_blueprint = Blueprint('photos', __name__, url_prefix='/photos')


@photos_blueprint.route('/list', methods=['GET'])
def read():
    return render_template('base.html')
