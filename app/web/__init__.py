"""
    Created by Thomas on 2021/4/13
"""
# 蓝图 Blueprint
from flask import Blueprint

web = Blueprint('web',__name__)

from app.web import book
from app.web import user