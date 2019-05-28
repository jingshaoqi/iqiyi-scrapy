# -*- coding: utf-8 -*-
import json
import time
from scrapy import Request
from scrapy.utils.project import get_project_settings
import redis
r = redis.Redis(host=get_project_settings().get('REDISHOST'), port=get_project_settings().get('REDISPORT'),db=get_project_settings().get('REDISDB'))
r.set("error", 0)
#12小时过期
r.expire("error", 60*60*12)
from AllScrapy.items import *

class IQIYISpider(scrapy.Spider):
    name = 'iqiyi'
    allowed_domains = ['iqiyi.com']
    #start_urls=['http://pcw-api.iqiyi.com/search/video/videolists?channel_id=1&data_type=1&pageSize=48&site=iqiyi&pageNum=1']
    def start_requests(self):
        pages = []
        for i in range(1, 30):
            url = 'http://pcw-api.iqiyi.com/search/video/videolists?channel_id=%d&data_type=1&pageSize=48&site=iqiyi&pageNum=1'%i
            # dont_filter=True 首次请求不会加入到过滤列表
            page = scrapy.Request(url, dont_filter=True)
            pages.append(page)
        return pages

    def parse(self, response):

        jsonobj = json.loads(response.text)
        movieitems = jsonobj['data']['list']
        if len(movieitems) == 0:
            return
        else:
            url1=response.url
            nexturl=url1[:url1.index('pageNum=') + 8] + str(int(url1[url1.index('pageNum=') + 8:]) + 1)
            print(nexturl)
            yield Request(nexturl,callback=self.parse)

        for item in movieitems:
            siteid = item['siteId']
            if siteid != 'iqiyi':
                continue
            id = int(time.time() * 1000 - 1558524422580)
            #redis读取
            b=r.sadd('movieid',item['tvId'])
            #可以成功插入movieid，则表示没有重复
            if b == 1:
                description = item.get('description')
                if description != None:
                    description = description.replace('"', '\\"')
                focus = item.get('focus')
                if focus != None:
                    focus = focus.replace('"', '\\"')
                #组装模型存入数据库
                m=MovieTableItem()
                m['id']=id
                m['movieid']=item['tvId']
                m['channelld']=item['channelId']
                m['description']=description
                m['name']=item['name']
                m['playurl']=item['playUrl']
                m['duration']=item['duration']
                m['focus']=focus
                m['score']=item.get('score')if item.get('score')else 0
                m['secondInfo']=item['secondInfo']
                m['formatPeriod']=item['formatPeriod']
                m['siteId']='iqiyi'
                try:
                    m['issuetime']=item['issueTime']
                except:
                    m['issuetime']=0
                m['imageurl']=item['imageUrl']
                m['timestamp']=int(time.time())
                yield m
            else:
                # 该数据存在,如果重复的太多，就跳过这个分类
                error=r.get('error')
                errornum=int(error)+1
                if errornum >1000:
                    return
                else:
                    r.set('error',int(error)+1)
                    #过期时间12小时
                    r.expire("error", 60*60*12)

                continue
            # 类型
            cates = item.get('categories')
            if cates == None:
                continue
            for citem in cates:
                c=CategoryItem()
                c['id']=id
                c['categories_id']=citem['id']
                c['name']=citem['name']
                c['url']=citem['url']
                c['subType']=citem['subType']
                c['subName']=citem['subName']
                c['level']=citem['level']
                c['qipuId']=citem['qipuId']
                c['parentId']=citem['parentId']
                c['timestamp']=int(time.time())
                yield c
            if item.get('cast') != None:
                directors = item['cast'].get('director')
                if directors != None:
                    for i in directors:
                        #director组装模型
                        d=DirectorItem()
                        d['id']=id
                        d['name']=i['name']
                        d['imageurl']=i.get('image_url')
                        d['directorid']=i['id']
                        d['timestamp']=int(time.time())

                        b=r.sadd('performerid',i['id'])
                        if b==1:
                            url_p='https://www.iqiyi.com/lib/s_'+str(i['id'])+'.html'
                            print(url_p)
                            yield  scrapy.Request(url_p, callback=self.performerDetail,meta={'id': i['id']})

                        yield d
                main_charactors = item['cast'].get('main_charactor')
                if main_charactors != None:
                    for i in main_charactors:
                        m=Main_charactorItem()
                        m['id']=id
                        m['name']=i['name']
                        m['imageurl']=i.get('image_url')
                        m['character']=",".join(i['character']).replace('"', '\\"')
                        m['maincharactorid']=i['id']
                        m['timestamp']=int(time.time())
                        b = r.sadd('performerid', i['id'])
                        if b == 1:
                            url_p = 'https://www.iqiyi.com/lib/s_' + str(i['id']) + '.html'
                            print(url_p)
                            yield scrapy.Request(url_p, callback=self.performerDetail,meta={'id': i['id']})

                        yield m

                screen_writers = item['cast'].get('screen_writer')
                if screen_writers != None:
                    for i in screen_writers:
                        s=Screen_writerItem()
                        s['id']=id
                        s['name']=i['name']
                        s['screen_writer_id']=i['id']
                        s['imageurl']=i.get('image_url')
                        s['timestamp']=int(time.time())
                        b = r.sadd('performerid', i['id'])
                        if b == 1:
                            url_p = 'https://www.iqiyi.com/lib/s_' + str(i['id']) + '.html'
                            print(url_p)
                            yield scrapy.Request(url_p, callback=self.performerDetail,meta={'id': i['id']})

                        yield s
                actors = item['cast'].get('actor')
                if actors != None:
                    for i in actors:
                        a=ActorItem()
                        a['id']=id
                        a['name']=i['name']
                        a['imageurl']=i.get('image_url')
                        a['character']=','.join(i['character'])
                        a['actorid']=i['id']
                        a['timestamp']=int(time.time())
                        b = r.sadd('performerid', i['id'])
                        if b == 1:
                            url_p = 'https://www.iqiyi.com/lib/s_' + str(i['id']) + '.html'
                            print(url_p)
                            yield scrapy.Request(url_p, callback=self.performerDetail,meta={'id': i['id']})

                        yield a
    def performerDetail(self,response):
        id = response.meta['id']
        p = PerformerDetailTableItem()
        p['name'] = response.xpath("//h1[@itemprop='name']/text()").extract_first()
        p['jobtitle'] = response.xpath("normalize-space(//li[@itemprop='jobTitle']/text())").extract_first()
        p['width'] = response.xpath("normalize-space(//li[@itemprop='weight']/text())").extract_first()
        p['height'] = response.xpath("normalize-space(//li[@itemprop='height']/text())").extract_first()
        p['blood'] = response.xpath(
            "normalize-space(//div[@class='mx_topic-item']/ul/li[last()]/text())").extract_first()
        p['address'] = response.xpath("normalize-space(//li[@itemprop='birthplace']/text())").extract_first()
        p['imageurl'] = "http:"+response.xpath("//img[@itemprop='image']/@src").extract_first()
        p['timestamp'] = int(time.time())
        p['performerid']=id
        try:
            # 描述
            p['des'] = response.xpath("//p[@class='mx_detail']/text()").extract()[-2].replace(' ', '')
        except:
            p['des']=None
        yield  p














