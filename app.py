#!/usr/bin/env python3

from flask import Flask, redirect, url_for
from views.auth import auth_blueprint
from views.photos import photos_blueprint


app = Flask(__name__)

app.register_blueprint(auth_blueprint)
app.register_blueprint(photos_blueprint)


@app.route('/')
def index():
    return redirect(url_for('photos.read'))


if __name__ == '__main__':
    app.config.from_mapping(
        SECRET_KEY='blabla333',
    )
    app.run(host='0.0.0.0', port=8000)
