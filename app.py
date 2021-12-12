#!/usr/bin/env python3

import os

from flask import Flask, redirect, url_for, send_from_directory
from flask_thumbnails import Thumbnail

from views.auth import auth_blueprint, login_required
from views.photos import photos_blueprint


app = Flask(__name__)
thumb = Thumbnail(app)


app.register_blueprint(auth_blueprint)
app.register_blueprint(photos_blueprint)


PUBLIC_STATIC = set([
    'favicon.ico',
    'akta_kamera.png',
    'style.css',
])


@app.route('/')
def index():
    return redirect(url_for('photos.read'))


@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='akta_kamera.png'))


@login_required
def protected_static(dirname, filename):
    return send_from_directory(dirname, filename)


def static(filename=None):
    dirname, fname = os.path.split(filename)
    dirname = f'static/{dirname}'
    if filename in PUBLIC_STATIC:
        return send_from_directory(dirname, fname)
    return protected_static(dirname, fname)


app.view_functions['static'] = static
app.config.from_mapping(
    # docs: https://github.com/silentsokolov/flask-thumbnails
    THUMBNAIL_MEDIA_ROOT='static/photos_uploaded',
    THUMBNAIL_MEDIA_THUMBNAIL_ROOT='static/thumbs',
    THUMBNAIL_MEDIA_THUMBNAIL_URL='../static/thumbs',
)
app.config.from_mapping(
    SECRET_KEY='blabla3asflkjaskjfkdsajfj33',
)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
