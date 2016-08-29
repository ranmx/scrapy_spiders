# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy.http import FormRequest
from bs4 import BeautifulSoup as bs


from lianjia.config import *

import re


class MySpider(scrapy.Spider):
    name = "lianjiaershou"
    allowed_domains = ["http://sh.lianjia.com"]
    start_urls = ['https://passport.lianjia.com/cas/login?service=http://user.sh.lianjia.com/index/ershou']
    header_login = HEADER_START

    def parse(self, response):
        print '=' * 100
        print response.meta
        print '=' * 100
        self.log_in(response)

    def log_in(self, response):
        jsessionID_regex = re.compile(JSESSIONID)
        jsessionID = jsessionID_regex.match(response.headers['Set-Cookie']).group()
        body_bs = bs(response.body, 'lxml')
        user_logn = body_bs.find('ul', class_="user-logn")
        hidden_input = user_logn.find_all('input', type='hidden')
        lt = hidden_input[0]['value']
        execution = hidden_input[1]['value']

        header = HEADER_LOGIN
        header['Cookie'] = [jsessionID]
        form = FORM_DATA
        form['execution'] = execution
        form['lt'] = lt

        response_with_cookies = scrapy.Request(url=self.start_urls[0],
                                               headers=header,
                                               # cookies=jsessionID
                                               )

        print '+' * 100
        print response_with_cookies.body
        print '+' * 100
        print form

        scrapy.FormRequest(
           url=self.start_urls[0],
           headers=header,
           formdata=form,
           callback=self.after_login
        )

    def after_login(self, response):
        print '=' * 100
        print response.headers
        print '=' * 100


process = CrawlerProcess({
'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.create_crawler(MySpider)
process.start()









