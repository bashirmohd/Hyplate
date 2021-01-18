from requests import get
from bs4 import BeautifulSoup
from datetime import datetime as dt
from random import shuffle
from pyquery import PyQuery

##########
def read_rss(url):
    article_list = []    
    r = get(url)
    soup = BeautifulSoup(r.content, features='xml')
    articles = soup.findAll('item')                
    
    for a in articles:
        try:
            article_obj = {}
            try:
                article_obj['title'] = a.find('title').text
            except:
                article_obj['title'] =  ''

            try:
                article_obj['link'] = a.find('link').text
            except:
                article_obj['link'] = ''
            try:
                date = a.find('pubDate').text[0:17]
                article_obj['date'] = dt.strptime(date, '%a, %d %b %Y').date()
            except:
                article_obj['date'] = date
            
            try:
                p1 = a.find('content:encoded')
                p1 = p1.text.replace('&lt;', '<').replace('&gt;', '>').replace(']]>', '>').replace('<![CDATA[', '')
                p = PyQuery(p1)
                img = p('div img').attr('src') or ('img').attr('src')
                article_obj['description'] = p('p').text()[0:200]+'...'
                article_obj['img'] = img
            except:
                p1 = a.find('description').text
                p1 = p1.replace('<![CDATA[', '')
                article_obj['description'] = p1[0:200]+'...'
                article_obj['img'] = '/static/assets/img/logos/infographics.png'
                
            try:

                article_obj['category'] =a.find('category').text
            except:
                article_obj['category'] = 'Web Scraping'

            article_list.append(article_obj)
        except:
            print('Cannot Pass'+url)
            pass
    return article_list