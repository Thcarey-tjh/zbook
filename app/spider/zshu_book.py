"""
    Created by Thomas on 2021/4/13
"""
from flask import current_app

from app.libs.zhttp import HTTP

class ZShuBook:
    '''
    请求过程的类封装
    '''

    isbn_url = 'http://t.talelin.com/v2/book/isbn/{}'
    keyword_url = 'http://t.talelin.com/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls,isbn):
        '''
        isbn关键字搜索
        :param isbn:
        :return:请求到的数据
        '''

        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def searcg_by_keyword(cls,keyword,page=1):
        '''
        普通关键字搜索
        :param keyword:
        :return:请求到的数据
        '''

        url = cls.keyword_url.format(keyword,current_app.config['PER_PAGE'],cls.calculate(page))
        result = HTTP.get(url)
        return result

    @staticmethod
    def calculate(page):
        return (page - 1) * current_app.config['PER_PAGE']
