import requests
import xml.etree.ElementTree as ele

rss_url="http://www.hindustantimes.com/rss/topnews/rssfeed.xml"
def coverttohtml():
    response=requests.get(rss_url)
    return response
def parsingxmltree(rss):
    root=ele.fromstring(rss)
    newsitems=[]
    for item in root.findall("./channel/item"):
        news={}
        for subnews in item:
            if child.tag=='{http://search.yahoo.com/mrss/}content':

                news['media']=child.attrib['url']
            else:
                news[child.tag]=child.text.encode('utf8')
        newsitems.append(news)
    return newsitems
def shouldimportthis():
    rss=converttohtml()
    newsitems=parsingxmltree(rss)
    #pip instprint(newsitems)
    return newsitems
