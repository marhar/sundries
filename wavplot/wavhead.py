#!/usr/bin/env /usr/anim/modsquad/bin/dmgpython
"""
wavhead - print wav header information
"""

import sys
import wave
import struct

for fn in sys.argv[1:]:
    print fn
    ii=wave.open(fn,'r')
    print "    getnchannels",ii.getnchannels()
    print "    getsampwidth",ii.getsampwidth()
    print "    getframerate",ii.getframerate()
    print "      getnframes",ii.getnframes()
    #print "     getcomptype",ii.getcomptype()
    #print "     getcompname",ii.getcompname()
    ii.close()
