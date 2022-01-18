import os
import functools

from flask import (
    Blueprint,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
    Response,
    send_from_directory,
)

from flask_paginate import Pagination, get_page_parameter

from .auth import login_required

from werkzeug.utils import secure_filename


photos_blueprint = Blueprint('photos', __name__, url_prefix='/photos')

PER_PAGE = 5


@photos_blueprint.route('/list', methods=['GET'])
@login_required
def read():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)

    istart = (page - 1) * PER_PAGE
    iend = page * PER_PAGE

    all_images = sorted(
        [img for img in os.listdir('static/photos_uploaded') if img.endswith('.jpg')],
        reverse=True,
    )

    pagination = Pagination(
        page=page,
        per_page=PER_PAGE,
        total=len(all_images),
        search=search,
        record_name='images',
        css_framework='foundation'
    )

    return render_template(
        'photos_list.html',
        images=all_images[istart:iend],
        pagination=pagination,
    )


@photos_blueprint.route('/dooofin', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        return Response("{'error': 'Fakaju whale!?'}", status=400, mimetype='application/json')
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return Response("{'error': 'Fakaju dooofin!?'}", status=400, mimetype='application/json')

    filename = secure_filename(file.filename)
    file.save(os.path.join('/home/ubuntu/camera/parking-camera/static/photos_uploaded/', filename))
    return Response("{'is goood': 'very good'}\n", status=200, mimetype='application/json')
