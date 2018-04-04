#!/usr/bin/python

import datetime 
import os
import rfeed
import urllib
from BeautifulSoup import BeautifulSoup

url = 'http://blog.dilbert.com'

def main():
    #html=urllib.urlopen(url).read()
    os.system('curl -s '+url+' >aa')
    html = open('aa').read()
    soup = BeautifulSoup(html)
    item_list = []
    for audio in soup.findAll('audio'):
        a = audio.findAll('a')[0]
        href = a['href']

        item_list.append(rfeed.Item(
            title = href,
            link = href,
            description = "fake description",
            author = "Scott Adams",
            guid = rfeed.Guid(href),
            pubDate = datetime.datetime(2014, 12, 29, 10, 00),
            enclosure = rfeed.Enclosure(url=href, length=0, type='')))

    feed = rfeed.Feed(
        title = "Scott Adams",
        link = "http://markharrison.net/sa.rss",
        description = "Words of Scott Adams",
        language = "en-US",
        lastBuildDate = datetime.datetime.now(),
        items = item_list
    )
    print(feed.rss())

main()
