#!/usr/bin/python
"""
wait for window to become visible
"""

import sys
import x11util

def main():
    for name in sys.argv[1:]:
        #x11util.windowraise(name)
        print x11util.windowpos(name)
        x11util.moveto(name,0,0)
        x11util.slideto(name,600,100)

main()
