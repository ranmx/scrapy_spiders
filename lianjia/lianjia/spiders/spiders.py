# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.contrib.spiders import CrawlSpider, Rule
import lianjia.settings
from scrapy.http import Request
from scrapy.http import FormRequest
from bs4 import BeautifulSoup as bs


from lianjia.config import *

import re


class MySpider(CrawlSpider):
    name = "spider"
    allowed_domains = ["sh.lianjia.com", "lianjia.com", "passport.lianjia.com"]
    start_url = 'https://passport.lianjia.com/cas/login?service=http://user.sh.lianjia.com/index/ershou'

    def start_requests(self):
        yield Request(self.start_url,
                      meta={'cookiejar': 1},
                      callback=self.get_form
                      )

    def get_form(self, response):
        cookies = {}
        jsessionID_regex = re.compile(JSESSIONID)
        jsessionID = jsessionID_regex.search(response.headers['Set-Cookie']).groups()[0]
        cookies['JSESSIONID'] = jsessionID
        cookies['Path'] = '/cas/'
        cookies['HttpOnly'] = 'true'

        body_bs = bs(response.body, 'lxml')
        user_logn = body_bs.find('ul', class_="user-logn")
        hidden_input = user_logn.find_all('input', type='hidden')
        lt = hidden_input[0]['value']
        execution = hidden_input[1]['value']

        print '=' * 40 + 'get_form' + '=' * 40
        print cookies
        print '=' * 100

        request_with_cookies = Request(url=self.start_url,
                                       cookies=cookies,
                                       callback=self.login,
                                       dont_filter=True
                                       )
        request_with_cookies.meta['execution'] = execution
        request_with_cookies.meta['lt'] = lt
        return request_with_cookies

    def login(self, response):
        form = FORM_DATA
        form['execution'] = response.meta['execution']
        form['lt'] = response.meta['lt']
        print '=' * 40 + 'login' + '=' * 40
        print form
        print '=' * 100
        return FormRequest.from_response(
              response,
              formdata=form,
              headers=HEADER_LOGIN,
              callback=self.after_login
              )

    def after_login(self, response):
        print '=' * 40 + 'after login' + '=' * 40
        print response.headers
        print '=' * 100



