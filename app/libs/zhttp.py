"""
    Created by Thomas on 2021/4/13
"""

# urllib 很难用，不推荐
# requests 第三方库，推荐，更加人性化和方便

import requests

class HTTP:
    '''
    封装请求API数据的类
    '''

    @staticmethod
    def get(url,return_json=True):
        '''
        :param url:请求的url地址
        :param return_json:控制API返回的是字符串还是json，增强了本函数的通用性
        :return:return_json
        '''

        r = requests.get(url)

        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

