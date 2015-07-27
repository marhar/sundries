#!/usr/bin/env python
"""
A simple OPML file scanner.
http://www.opml.org/spec
"""

import xml.dom.minidom

class OpmlFile(object):
    """
    a parsed OMPL file
    http://www.opml.org/spec
    """
    def __init__(self,s,verbose=False):
        self.tree={}
        self.verbose=verbose
        self.visited={}

        dom = xml.dom.minidom.parseString(s)
        body=dom.getElementsByTagName("body")[0]
        #body=body.getElementsByTagName("body")[0]
        self.do_body(body)

    def do_outline(self,dom,parent,lev=0):
        if self.verbose: print ' '*lev*4,dom.getAttribute('text')

        # BUG, figure out why multiple visits
        if self.visited.has_key(dom.getAttribute('text')):
            return
        else:
            self.visited[dom.getAttribute('text')]=1

        if parent is not None:
            self.tree[parent.getAttribute('text'),dom.getAttribute('text')]=lev
        else:
            self.tree[None,dom.getAttribute('text')]=lev
        olist=dom.getElementsByTagName("outline")
        for x in olist:
            self.do_outline(x,dom,lev+1)

    def do_body(self,dom):
        olist=dom.getElementsByTagName("outline")
        for x in olist:
            self.do_outline(x,None)

if __name__=="__main__":
    def main():

        opml_sample="""\
        <?xml version="1.0" encoding="UTF-8"?>
        <opml version="1.0">
          <head>
            <title>fogbugz-project2</title>
            <expansionState>1,4,5,6</expansionState>
          </head>
          <body>
            <outline text="xyzzy part 1" _note="some text for 1"/>
            <outline text="xyzzy part 2">
              <outline text="xyzzy part 2a"/>
              <outline text="xyzzy part-2-b"/>
            </outline>
            <outline text="xyzzy part 3">
              <outline text="xyzzy part 3a" _note="some text for 3a">
                <outline text="xyzzy part 3a1">
                  <outline text="xyzzy part 3a1A"/>
                </outline>
              </outline>
            </outline>
          </body>
        </opml>
        """

        import pprint
        opml=OpmlFile(file("tiny3.opml").read(),verbose=True)
        pprint.pprint(opml.tree)

    main()
