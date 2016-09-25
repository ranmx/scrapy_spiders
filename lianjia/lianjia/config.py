# -*- coding: utf-8 -*-
from acount import *

DISTRICT_C = [u'浦东', u'闵行', u'宝山', u'徐汇', u'普陀', u'杨浦', u'长宁', u'松江', u'嘉定',
              u'黄浦', u'静安', u'闸北', u'虹口', u'青浦', u'奉贤', u'金山', u'崇明', u'上海周边']

JSESSIONID = '(?:=)([^;]+)'

HEADER_LOGIN = {
    'Host': "passport.lianjia.com",
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'Accept-Language': "en-US,en;q=0.7,zh-CN;q=0.3",
    'Accept-Encoding': "gzip, deflate, br",
    'Connection': "keep-alive",
    'Upgrade-Insecure-Requests': "1",
    'service': "http://sh.lianjia.com/ershoufang/d1"
}

FORM_DATA = {
    'username': ACCOUNT['user'],
    'password': ACCOUNT['password'],
    # 'service': 'http://bj.lianjia.com/',
    # 'isajax': 'true',
    # 'remember': 1,
    'execution': '',
    '_eventId': 'submit',
    'lt': '',
    'verifyCode': '',
    'redirect': '',
    'remember': '1'
}

HEADER_TICKET_302 = {
    'Host': "user.sh.lianjia.com",
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'Accept-Language': "en-US,en;q=0.7,zh-CN;q=0.3",
    'Accept-Encoding': "gzip, deflate",
    'DNT': "1",
    'Connection': "keep-alive",
    'Upgrade-Insecure-Requests': "1"
}



