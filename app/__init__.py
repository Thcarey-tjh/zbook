"""
    Created by Thomas on 2021/4/13
"""
from flask import Flask

from app.models.book import db


def create_app():
    '''
    初始化核心对象，这里包含初始化要做的所有操作
    :return:app核心对象
    '''

    app = Flask(__name__)

    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)

    return app

def register_blueprint(app):
    '''
    在app对象中注册蓝图
    :param app:app核心对象
    '''

    from app.web.book import web
    from app.web.user import web
    app.register_blueprint(web)