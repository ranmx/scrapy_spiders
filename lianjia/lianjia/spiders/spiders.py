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
    allowed_domains = ["http://sh.lianjia.com"]
    start_urls = ['https://passport.lianjia.com/cas/login?service=http://user.sh.lianjia.com/index/ershou']

    def parse(self, response):
        print '=' * 40 + 'response meta' + '=' * 40
        print response.meta
        print '=' * 100
        self.log_in(response)

    def log_in(self, response):
        cookies = []
        jsessionID_regex = re.compile(JSESSIONID)
        jsessionID = jsessionID_regex.search(response.headers['Set-Cookie']).groups()[0]
        cookies.append({'JSESSIONID': jsessionID})

        body_bs = bs(response.body, 'lxml')
        user_logn = body_bs.find('ul', class_="user-logn")
        hidden_input = user_logn.find_all('input', type='hidden')
        lt = hidden_input[0]['value']
        execution = hidden_input[1]['value']

        header = HEADER_LOGIN
        form = FORM_DATA
        form['execution'] = execution
        form['lt'] = lt

        scrapy.FormRequest(
            url=self.start_urls[0],
            headers=header,
            cookies=cookies,
            formdata=form,
            callback=self.after_login
            )

    def after_login(self, response):
        print '=' * 40 + 'after login' + '=' * 40
        print response.headers
        print '=' * 100



