#!/usr/bin/env python
"""
Fogbugz helper functions.
"""

import urllib
import xml.dom.minidom

class FogError(Exception):
    def __init__(self, value):
        self.value = str(value)
    def __str__(self):
        return repr(self.value)

class FogBugzConnection(object):
    """
    http://www.fogcreek.com/FogBugz/docs/70/topics/advanced/API.html
    TODO: make api for each operation, e.g. conn.new(sTitle='foo')
    """
    def __init__(self, topurl, email, password):
        self.topurl = topurl
        self.email = email
        self.password = password
        self.token=''
        self.fbparse=FogBugzParser()

        self.apiinfo()
        self.login()

    def login(self):
        resp=self.sendit({
            'cmd'      : 'logon',
            'email'    : self.email,
            'password' : self.password,
        })
        self.fbparse.raiseerror(resp)
        login_info=self.fbparse.login2(resp)
        self.token=str(login_info['token'])

    def apiinfo(self):
        # get api information
        f = urllib.urlopen(self.topurl+'/api.xml')
        resp=f.read()
        self.fbparse.raiseerror(resp)
        api_info=self.fbparse.api(resp)
        self.apiurl=api_info['url']
        self.apiminversion=api_info['minversion']
        self.apiversion=api_info['version']

    def sendit(self,params):
        params['token']=self.token
        f = urllib.urlopen(self.topurl+'/'+self.apiurl+urllib.urlencode(params))
        resp=f.read()

        try:
            # sorry for the double-parse...
            self.fbparse.raiseerror(resp)
        except FogError, e:
            print 'params=',params
            print str(e)
            raise(e)
        return resp

class FogBugzParser:

    #-------------------------------------------------------------------
    def pp(self,s):
        doc=xml.dom.minidom.parseString(s)
        return doc.toprettyxml(indent='  ')

    #-------------------------------------------------------------------
    def ppdoc(self,doc):
        print '='*60
        return doc.toprettyxml(indent='  ')

    #-------------------------------------------------------------------
    def getText(nodelist):
        rc = ""
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc = rc + node.data
        return rc

    #-------------------------------------------------------------------
    def response(self,s):
        xdom = xml.dom.minidom.parseString(s)
        xresponse=xdom.getElementsByTagName("response")[0]
        return xresponse

    #-------------------------------------------------------------------
    def raiseerror(self,s):
        """
        cheap hack, should be incorporated into real parsing
        <response><error code="1">Incorrect password or username</error></response>
        """
        xdom = xml.dom.minidom.parseString(s)
        xresponse=xdom.getElementsByTagName("response")[0]
        xerror=xresponse.getElementsByTagName("error")
        if xerror == []:
            return False
        else:
            xerror=xerror[0]
            code=xerror.getAttribute('code')
            errtext=self.getText(xerror.childNodes)
            raise FogError('error %s %s'%(code,errtext))

    #-------------------------------------------------------------------
    def generic_2level(self,s):
        """
         set of list of a=b in response
         <response> <foo>7</foo> <bar>1</bar> </response>
        """
        xdom = xml.dom.minidom.parseString(s)
        xresponse=self.response(s)
        qq={}
        for nn in xresponse.childNodes:
            if nn.nodeType == nn.ELEMENT_NODE:
                qq[str(nn.nodeName)]=str(nn.childNodes[0].nodeValue.strip())
        return qq

    #-------------------------------------------------------------------
    def generic_2leveldoc(self,doc):
        """
         set of list of a=b in something
         <something> <foo>7</foo> <bar>1</bar> </something>
        """
        qq={}
        for nn in doc.childNodes:
            if nn.nodeType == nn.ELEMENT_NODE:
                qq[str(nn.nodeName)]=str(nn.childNodes[0].nodeValue.strip())
        return qq

    #-------------------------------------------------------------------
    def generic_attributesdoc(self,doc):
        """
         set of attributes
         <something foo="1" bar="2">
        """
        qq={}
        for rr in doc.attributes.items():
            qq[str(rr[0])]=str(rr[1])
        return qq

    #-------------------------------------------------------------------
    def case(self,s):
        """
        <response>
          <case ixBug="11" operations="edit,assign,resolve,email,remind">
            <ixBug>
              11
            </ixBug>
            <ixBugParent>
              2
            </ixBugParent>
          </case>
        </response>
        """
        response=self.response(s)
        case=response.getElementsByTagName('case')[0]
        ixBug=case.getAttribute('ixBug')
        operations=case.getAttribute('operations')
        q1={}
        for rr in case.attributes.items():
            q1[str(rr[0])]=str(rr[1])
        #q1=self.generic_attributesdoc(case)
        q2=self.generic_2leveldoc(case)
        return [q1,q2]

    #-------------------------------------------------------------------
    def api(self,s):
        """
         <response>
          <version>7</version>
          <minversion>1</minversion>
          <url>api.asp?</url>
         </response>
        """
        return self.generic_2level(s)

    #-------------------------------------------------------------------
    def OLD_api(self,s):
        """
         <response>
          <version>7</version>
          <minversion>1</minversion>
          <url>api.asp?</url>
         </response>
        """
        xdom = xml.dom.minidom.parseString(s)
        xresponse=self.response(s)
        return {
            'version':   self.yank(xresponse.getElementsByTagName("version")),
            'minversion':self.yank(xresponse.getElementsByTagName("minversion")),
            'url':       self.yank(xresponse.getElementsByTagName("url"))
        }

    #-------------------------------------------------------------------
    def yank(self,dom):
        """yank the text out of <foo>text</foo>"""
        cdata=dom[0].childNodes[0]
        return cdata.wholeText

    #-------------------------------------------------------------------
    def login2(self,s):
        """
        <response>
          <token>
            <![CDATA[nt0s2pl2j7rck29jg0v9ijgj76va12]]>
          </token>
        </response>
        """
        return self.generic_2level(s)

    #-------------------------------------------------------------------
    def login(self,s):
        """
        <response>
          <token>
            <![CDATA[nt0s2pl2j7rck29jg0v9ijgj76va12]]>
          </token>
        </response>
        """
        x=self.generic_2level(s)
        return x['token']

    #-------------------------------------------------------------------
    def OLD_login(self,s):
        """
        <response>
          <token>
            <![CDATA[nt0s2pl2j7rck29jg0v9ijgj76va12]]>
          </token>
        </response>
        """
        xdom = xml.dom.minidom.parseString(s)
        xresponse=xdom.getElementsByTagName("response")[0]
        xtoken=xresponse.getElementsByTagName("token")
        cdata=xtoken[0].childNodes[0]
        tok=cdata.wholeText
        return tok

if __name__ == "__main__":
    def test_fogbugz():

        from pprint import pprint
        bugzp=FogBugzParser()

        zexpected=\
          [{'ixBug': '11', 'operations': 'edit,assign,resolve,email,remind'},
           {'ixBug': '11', 'ixBugParent': '2'}]

        zxml="""<?xml version="1.0" ?>
                <response>
              <case ixBug="11" operations="edit,assign,resolve,email,remind">
                <ixBug>
                  11
                </ixBug>
                <ixBugParent>
                  2
                </ixBugParent>
              </case>
            </response>"""

        print zxml
        print '----'
        z=bugzp.case(zxml)
        pprint(z)
        print zexpected==z
    test_fogbugz()
