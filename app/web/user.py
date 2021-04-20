"""
    Created by Thomas on 2021/4/16
"""
from . import web

@web.route("/user")
def login():
    return "user"