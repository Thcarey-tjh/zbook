"""
    Created by Thomas on 2021/4/13
"""
from flask import jsonify, request

from app.libs.heiper import is_isbn_or_key
from app.spider.zshu_book import ZShuBook
from . import web
from ..forms.book import SearchForm


@web.route("/book/search")
def search():
    '''
    q：用户输入的查询，可能是普通关键字/isbn
    page
    :return:json数据
    '''
    form = SearchForm(request.args)

    if form.validate():
        q = form.q.data
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)

        if isbn_or_key == 'isbn':
            result = ZShuBook.search_by_isbn(q)
        else:
            result = ZShuBook.searcg_by_keyword(q,page)

        return jsonify(result)
    else:
        return jsonify(form.errors)
