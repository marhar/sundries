#!/usr/bin/python

import datetime 
import os
import sys
import rfeed
import urllib
import xml.dom.minidom
from BeautifulSoup import BeautifulSoup

url = 'https://blog.dilbert.com'

def main():
    item_list = []

    for f in sys.argv[1:]:
    
        item_list.append(rfeed.Item(
            title = f,
            link = f,
            guid = rfeed.Guid(f),
            enclosure = rfeed.Enclosure(url=f, length=0, type='')))

    feed = rfeed.Feed(
        title = "Eisenhorn",
        link = "eisenhorn.rss",
        description = "Eisenhorn",
        language = "en-US",
        lastBuildDate = datetime.datetime.now(),
        items = item_list
    )
    print xml.dom.minidom.parseString(feed.rss()).toprettyxml(indent='  ')


main()
