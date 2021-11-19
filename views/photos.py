import os
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
    return render_template(
        'photos_list.html',
        images=os.listdir('static/photos_uploaded'),
    )

@photos_blueprint.route('/save', methods=['POST'])
@login_required
def save():
    file = request.files['file']
    file.save(os.path.join('static/photos_uploaded', file.filename))
    return redirect('/list')
