# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class District(scrapy.Item):
    name = scrapy.Field()
    subareas = scrapy.Field()
    number = scrapy.Field()
    url = scrapy.Field()


class Street(scrapy.Item):
    name = scrapy.Field()
    district = scrapy.Field()
    xiaoqu = scrapy.Field()
    number = scrapy.Field()
    url = scrapy.Field()


class Community(scrapy.Item):
    ID = scrapy.Field()
    street = scrapy.Field()
    name = scrapy.Field()
    location = scrapy.Field()
    railway = scrapy.Field()
    number = scrapy.Field()
    average = scrapy.Field()
    build_time = scrapy.Field()
    buildings = scrapy.Field()
    rooms = scrapy.Field()
    plot_ratio = scrapy.Field()
    green_land = scrapy.Field()
    url = scrapy.Field()


class Property(scrapy.Item):
    ID = scrapy.Field()
    price = scrapy.Field()
    community = scrapy.Field()
    area = scrapy.Field()
    room_type = scrapy.Field()
    price_pm = scrapy.Field()
    direction = scrapy.Field()
    pay_per_m = scrapy.Field()
    agent = scrapy.Field()
    tax = scrapy.Field()
    decoration = scrapy.Field()
    url = scrapy.Field()









