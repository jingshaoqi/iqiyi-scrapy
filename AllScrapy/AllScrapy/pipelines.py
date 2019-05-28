# -*- coding: utf-8 -*-

from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings
from AllScrapy.items import *
import oss2 as oss2
import requests
import traceback

AccessKeyId=get_project_settings().get('ACCESSKEYID')
AccessKeySecret=get_project_settings().get('ACCESSKEYSECRET')
Endpoint=get_project_settings().get('ENDPOINT')
BUCKET=get_project_settings().get('BUCKET')
bucket = oss2.Bucket(oss2.Auth(AccessKeyId, AccessKeySecret), Endpoint, BUCKET)
# url='http://pic3.iqiyipic.com/image/20190520/e4/9e/v_127468659_m_601_m5.jpg'
import hashlib

def upload(url,folder=None):
    if url==None:
        return None
    try:
        m = hashlib.md5()
        m.update(url.encode('UTF-8'))
        filename=m.hexdigest()
        input = requests.get(url)
        result = bucket.put_object(folder+'/' + filename + '.jpg', input)
        # print(result.status)
        if result.status == 200:
            # print("上传成功")
            return "https://"+BUCKET+"."+Endpoint+"/"+folder+"/"+filename+".jpg"
        else:
            return None
    except:
        traceback.print_exc()
        return None
#url=upload("http://pic3.iqiyipic.com/image/20190520/e4/9e/v_127468659_m_601_m5.jpg",'moviepic')
#print(url)



#基础类
class RootPipline(object):
    def open_spider(self,spider):
        ##读取settings中的配置信息
        db= spider.settings['DATABASE']
        host=spider.settings['HOST']
        port=spider.settings['PORT']
        user=spider.settings['USERNAME']
        passwd=spider.settings['PASSWORD']
        #第一个参数是使用mysql.connector模块连接  utf8，如果使用utf-8报错
        self.dbpool=adbapi.ConnectionPool('mysql.connector',host=host,db=db,user=user,passwd=passwd,port=port,charset='utf8')
    def close_spider(self,spider):
        self.dbpool.close()

    def process_item(self, item, spider):
        if isinstance(item, MovieTableItem):
            uploadurl = upload(item['imageurl'], 'moviepic')
            item['saveimageurl']=uploadurl
            self.dbpool.runInteraction(self.movietableAdd, item)
        if isinstance(item, ActorItem):
            self.dbpool.runInteraction(self.actorAdd, item)
        if isinstance(item, CategoryItem):
            self.dbpool.runInteraction(self.categoryAdd, item)
        if isinstance(item, DirectorItem):
            uploadurl = upload(item['imageurl'], 'personpic')
            item['saveimageurl']=uploadurl
            self.dbpool.runInteraction(self.directorAdd, item)
        if isinstance(item, Main_charactorItem):
            uploadurl = upload(item['imageurl'], 'personpic')
            item['saveimageurl'] = uploadurl
            self.dbpool.runInteraction(self.main_charactorAdd, item)
        if isinstance(item, Screen_writerItem):
            uploadurl = upload(item['imageurl'], 'personpic')
            item['saveimageurl'] = uploadurl
            self.dbpool.runInteraction(self.screen_writerAdd, item)
        if isinstance(item, PerformerDetailTableItem):
            uploadurl = upload(item['imageurl'], 'personpic')
            item['saveimageurl'] = uploadurl
            self.dbpool.runInteraction(self.performerdetailAdd, item)
        return item
    #各种模型的保存
    def categoryAdd(self, tx, item):
        sqlstr = """insert into category values (%d,%d,"%s","%s",%d,"%s",%d,%d,%d,%d)""" % (
            item['id'], item['categories_id'], item['name'], item['url'], item['subType'], item['subName'], item['level'],
            item['qipuId'], item['parentId'], item['timestamp'])
        return executeSQL(tx, sqlstr)

    def directorAdd(self, tx, item):
        sqlstr = """insert into director values (%d,"%s","%s",%d,%d,"%s")""" % (
        item['id'], item['name'], item['imageurl'], item['directorid'], item['timestamp'], item['saveimageurl'])
        return executeSQL(tx, sqlstr)

    def main_charactorAdd(self, tx, item):
        sqlstr = """insert into main_charactor values (%d,"%s","%s","%s",%d,%d,"%s")""" % (item['id'], item['name'], item['imageurl'], item['character'], item['maincharactorid'], item['timestamp'],item['saveimageurl'])
        print(sqlstr)
        return executeSQL(tx, sqlstr)

    def movietableAdd(self, tx, item):
        sqlstr=""" insert into movietable values(%d,%d,%d,"%s","%s","%s","%s","%s",%f,"%s","%s","%s",%d,"%s",%d,"%s")"""\
               % (item['id'], item['movieid'], item['channelld'],item['description'],item['name'],item['playurl'],item['duration'],item['focus'],item['score'],item['secondInfo'],item['formatPeriod'],item['siteId'],item['issuetime'],item['imageurl'],item['timestamp'],item['saveimageurl'])
        print(sqlstr)
        return executeSQL(tx, sqlstr)

    def screen_writerAdd(self, tx, item):
        sqlstr = """insert into screen_writer values (%d,"%s",%d,'%s',%d,"%s")""" % (
            item['id'], item['name'], item['screen_writer_id'], item['imageurl'], item['timestamp'], item['saveimageurl'])
        return executeSQL(tx, sqlstr)

    def actorAdd(self, tx, item):
        uploadurl=upload(item['imageurl'],'personpic')
        sqlstr = """insert into actor values (%d,"%s","%s","%s",%d,%d,"%s")""" % (
            item['id'], item['name'], item['imageurl'], item['character'], item['actorid'], item['timestamp'], uploadurl)
        return executeSQL(tx, sqlstr)

    def performerdetailAdd(self, tx, item):
        sqlstr = """insert into performerdetail values ("%s","%s","%s","%s","%s","%s","%s","%s","%s",%d,%d)""" % (
            item['name'], item['jobtitle'], item['width'], item['height'], item['blood'], item['address'],item['imageurl'],item['des'],item['saveimageurl'],item['timestamp'],item['performerid'])
        return executeSQL(tx, sqlstr)


#工具封装
def executeSQL(tx,sql):
    try:
        tx.execute(sql)
        return True
    except:
        return False
def selectSQL(tx,sql):
    try:
        tx.execute(sql)
        result = tx.fetchall()
        return result
    except:
        print("出错")
        return None
def makeMD5(str):
    m = hashlib.md5()
    m.update(str.encode('UTF-8'))
    return  m.hexdigest()




