# -*- coding: utf-8 -*-
from flask import Flask

import mqpcf_v1


def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        mqpcf_v1.bp,
        url_prefix='/mqpcf/v1')

    return app

if __name__ == '__main__':
    create_app().run(debug=True)