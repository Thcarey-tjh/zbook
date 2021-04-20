"""
    Created by Thomas on 2021/4/13
"""

def is_isbn_or_key(word):
    '''
    判断word是普通字符串还是isbn
    :param word:用户输入的关键字
    :return isbn_or_key:普通关键字/isbn
    '''

    # 传参默认为普通关键字
    isbn_or_key = 'key'

    # 判断q是isbn还是普通关键字
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'

    short_word = word.replace('-', '')

    if '_' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key == 'isbn'

    # 返回结果
    return isbn_or_key