import sys
import os
import re
import urllib
import urlparse
from pprint import pprint
from BeautifulSoup import BeautifulSoup

TOP='http://hobbyking.com/hobbyking/store'
CACHED='./CACHE'

class HKObject(object):
    def cachepath(self):
        dd='%s/%s'%(CACHED,self.mytype)
        pp='%s/%s.html'%(dd,self.itemno)
        return (dd,pp)

    def readme(self):
        (dd,pp)=self.cachepath()
        try:
            ff=open(pp)
            self.html=ff.read()
            ff.close()
            return
        except IOError,e:
            if e.errno != 2: raise e
        except OSError,e:
            if e.errno != 2: raise e

        try:
            os.makedirs(dd)
        except OSError,e:
            if e.errno != 17: raise
        self.html=urllib.urlopen(self.url).read()
        ff=open(pp,"w")
        print >>ff,self.html
        ff.close()

    def blowcache(self):
        (dd,pp)=self.cachepath()
        try:
            os.unlink(pp)
        except OSError,e:
            if e.errno != 2: raise
        try:
            os.rmdir(dd)
        except OSError,e:
            if e.errno != 66: raise

    def parseme(self):
        self.url=self.urlt%(self.itemno)
        self.readme()
        self.soup=BeautifulSoup(self.html)

class Item(HKObject):
    urlt='%s/uh_viewItem.asp?idProduct=%%d'%(TOP)
    def __init__(self,prodno):
        self.prodno=prodno
        self.mytype='item'
        self.itemno=prodno
        self.parseme()

        #---------------------------------------------------------------
        # <!--product images and details-->
        # productid:
        # heading:
        # img:
        # crowns:
        #---------------------------------------------------------------
        self.details={}
        xxprod=self.soup.find(text=re.compile("product images and details"))
        tbl=xxprod.findNextSibling()
        tmps=self.soup.firstText(re.compile('PRODUCT ID:'))
        mm=re.search('PRODUCT ID: *(.*)',tmps)
        self.details['productid']=mm.group(1)

        self.details['crowns']=None
        for i in [1,2,3,4,5]:
            searchstr='images/%d_crown.jpg'%(i)
            ff=tbl.find('img', src=searchstr)
            if ff:
                self.details['crowns']=i
                break

        img=tbl.find(src=re.compile("catalog/"))
        self.details['heading']=img.attrMap['alt']
        # later get heading from headingb span
        self.details['img']=img.attrMap['src']

        #---------------------------------------------------------------
        # <!-- database prodData-->
        #---------------------------------------------------------------
        self.config={}
        tags=['Model','Max Eff','Max Load','Kv','Weight',
              'Pull','Prop','Voltage','No Load Curr','Size ']
        txtb=tbl.firstText(re.compile('Model:')).findParent()
        for t in tags:
            self.config[t]=txtb.firstText(re.compile(t+':'))

    def dump(self):
        print '--'
        print 'prod %d'%(self.itemno)
        pprint(self.details,indent=4)
        pprint(self.config,indent=4)

    def details(self):
        return None
    def config(self):
        return None


class Category(HKObject):
    urlt='%s/uh_listCategoriesAndProducts.asp?idCategory=%%d'%(TOP)
    def __init__(self,catno):
        self.catno=catno
        self.mytype='category'
        self.itemno=catno
        self.parseme()



"""
def doprod(prodno):
    url=produrl%(prodno)
    html=urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    comm=soup.find(text=re.compile("product images and details"))
    tbl=comm.findNextSibling()
    img=tbl.find(src=re.compile("catalog/"))

    x={}

    ##x['name']=tbl.findAll(attrs={"class" : "headingb"})
    x['name']=img.attrMap['alt']
    x['pid']=soup.firstText(re.compile('PRODUCT ID:'))
    x['img']=img.attrMap['src']
    txtb=tbl.firstText(re.compile('Model:')).findParent()
    details=getdetails(txtb)
    for k in details.keys():
        x[k]=details[k]

    pprint(x)

def getdetails(txtb):
    tags=['Model','Max Eff','Max Load','Kv','Weight','Pull','Prop','Voltage','No Load Curr','Size ']
    x={}
    for t in tags:
        x[t]=txtb.firstText(re.compile(t+':'))
    return x
"""
