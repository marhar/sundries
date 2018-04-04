#!/usr/bin/python

import datetime 
from rfeed import *
import urllib
from BeautifulSoup import BeautifulSoup

url = 'http://blog.dilbert.com'

def main():
    #html=urllib.urlopen(url).read()
    html = open('aa').read()
    soup = BeautifulSoup(html)
    item_list = []
    for audio in soup.findAll('audio'):
        a = audio.findAll('a')[0]
        href = a['href']

        item_list.append(Item(
            title = "Sample article",
            link = href,
            description = "This is the description of the first article",
            author = "Scott Adams",
            guid = Guid(href),
            pubDate = datetime.datetime(2014, 12, 29, 10, 00),
            enclosure = Enclosure(url=href, length=0, type='')))

    feed = Feed(
        title = "Sample Podcast RSS Feed",
        link = "http://www.example.com/rss",
        description = "An example of how to generate an RSS 2.0 feed",
        language = "en-US",
        lastBuildDate = datetime.datetime.now(),
        items = item_list
    )
    print(feed.rss())

main()
