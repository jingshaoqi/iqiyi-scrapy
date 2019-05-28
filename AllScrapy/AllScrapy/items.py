# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ActorItem(scrapy.Item):
    id=scrapy.Field()
    name=scrapy.Field()
    imageurl=scrapy.Field()
    character=scrapy.Field()
    actorid=scrapy.Field()
    timestamp=scrapy.Field()
    saveimageurl=scrapy.Field()
class CategoryItem(scrapy.Item):
    id=scrapy.Field()
    categories_id=scrapy.Field()
    name=scrapy.Field()
    url=scrapy.Field()
    subType=scrapy.Field()
    subName=scrapy.Field()
    level=scrapy.Field()
    qipuId=scrapy.Field()
    parentId=scrapy.Field()
    timestamp=scrapy.Field()
class DirectorItem(scrapy.Item):
    id=scrapy.Field()
    name=scrapy.Field()
    imageurl=scrapy.Field()
    directorid=scrapy.Field()
    timestamp=scrapy.Field()
    saveimageurl=scrapy.Field()
class Main_charactorItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    imageurl = scrapy.Field()
    character = scrapy.Field()
    maincharactorid=scrapy.Field()
    timestamp = scrapy.Field()
    saveimageurl = scrapy.Field()

class MovieTableItem(scrapy.Item):
    id=scrapy.Field()
    movieid=scrapy.Field()
    channelld=scrapy.Field()
    description = scrapy.Field()
    name = scrapy.Field()
    playurl = scrapy.Field()
    duration = scrapy.Field()
    focus = scrapy.Field()
    score = scrapy.Field()
    secondInfo=scrapy.Field()
    formatPeriod=scrapy.Field()
    siteId=scrapy.Field()
    issuetime=scrapy.Field()
    imageurl=scrapy.Field()
    timestamp=scrapy.Field()
    saveimageurl=scrapy.Field()
class Screen_writerItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    imageurl = scrapy.Field()
    screen_writer_id = scrapy.Field()
    timestamp = scrapy.Field()
    saveimageurl = scrapy.Field()

class PerformerDetailTableItem(scrapy.Item):
        name = scrapy.Field()
        jobtitle = scrapy.Field()
        width = scrapy.Field()
        height = scrapy.Field()
        blood = scrapy.Field()
        address = scrapy.Field()
        imageurl = scrapy.Field()
        des = scrapy.Field()
        saveimageurl = scrapy.Field()
        timestamp = scrapy.Field()
        performerid=scrapy.Field()


