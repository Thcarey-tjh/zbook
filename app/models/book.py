"""
    Created by Thomas on 2021/4/18
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer,String


db = SQLAlchemy()
class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))  # 出版社
    isbn = Column(String(15),nullable=False,unique=True)
    price = Column(String(20))
    pages = Column(Integer)  # 页数
    pubdate = Column(String(20))  # 出版年月
    summary = Column(String(1000))  # 书籍简介
    image = Column(String(50))

    def sample(self):
        pass