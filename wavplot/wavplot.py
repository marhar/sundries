#!/usr/bin/env /usr/anim/modsquad/bin/dmgpython
"""
how to plot a wav file
"""

import sys
import wave
import struct
import new
from pngcanvas import PNGCanvas 

#-----------------------------------------------------------------------
# experimental class modifications

def gettimecode_secs(self,frameno):
    return float(frameno)*(1.0/self.getframerate())
def gettimecode_mins(self,frameno):
    return float(frameno)*(1.0/self.getframerate())/60.0


#-----------------------------------------------------------------------
# wav decoders, 8,16,24,32 bits mono,stereo

def cvt08(x):
    """8 bit, mono"""
    v=struct.unpack('B',x)[0]
    return v

def cvt08s(x):
    """8 bit, stereo"""
    a=struct.unpack('BB',x)
    v=(a[0]+a[1])/2
    return v

def cvt16(x):
    """16 bit, mono"""
    v=struct.unpack('h',x)[0]
    return v

def cvt16s(x):
    """16 bit, stereo"""
    a=struct.unpack('hh',x)
    v=(a[0]+a[1])/2
    return v

def cvt24(x):
    """24 bit, mono"""
    a=struct.unpack('BBB',x)
    b=struct.pack('BBBB',0,a[0],a[1],a[2])
    v=struct.unpack('i',b)[0]
    return v

def cvt24s(x):
    """24 bit, stereo"""
    a=struct.unpack('BBBBBB',x)
    b0=struct.pack('BBBB',0,a[0],a[1],a[2])
    b1=struct.pack('BBBB',0,a[3],a[4],a[5])
    v0=struct.unpack('i',b0)[0]
    v1=struct.unpack('i',b1)[0]
    v=(v0+v1)/2
    return v

def cvt32(x):
    """32 bit, mono"""
    v=struct.unpack('i',x)[0]
    return v

def cvt32s(x):
    """32 bit, stereo"""
    a=struct.unpack('ii',x)
    v=(a[0]+a[1])/2
    return v

#-----------------------------------------------------------------------
def compute(file):
    
    ii=wave.open(file)
    nframes=ii.getnframes()
    framerate=ii.getframerate()
    if float(nframes)/framerate > 121:
        ii.gettimecode=new.instancemethod(gettimecode_mins,ii,ii.__class__)
    else:
        ii.gettimecode=new.instancemethod(gettimecode_secs,ii,ii.__class__)

    #-----------------------------------------------------------------------
    # decoder lookup table
    cvtfuncs=[[None,cvt08,cvt16,cvt24,cvt32],
              [None,cvt08s,cvt16s,cvt24s,cvt32s]]
    cvtfunc=cvtfuncs[ii.getnchannels()-1][ii.getsampwidth()]

    #-----------------------------------------------------------------------
    # plot vv=256 points
    #
    #
    stuff_i_think_needs_to_get_set_in_gnuplot="""
    set term "x11" size 256,192
    plot [] [-2147483648.0:2147483648.0] "out24.dat" w l
    """

    #-----------------------------------------------------------------------
    # pointsToPlot drives the sampling of the audio file
    # make it match the graph resolution as much as possible
    # fewer points=faster, more points=better detail up to a certain limit

    pointsToPlot=2000
    frameskip=int(nframes/pointsToPlot)     # sparse plot

    #-----------------------------------------------------------------------
    # main loop for plotting
    data = []

    frameno=0
    while True:
        if frameskip > 1:
            ii.setpos(frameno)
        x=ii.readframes(1)
        if len(x)==0:
            break
        v=cvtfunc(x)
        # unset key
        # set title "foo"
        # add x
        
        data.append( (ii.gettimecode(frameno),v))
        #print ii.gettimecode(frameno),v
        frameno+=frameskip
        if frameno >= nframes:
            break
    
    return  data

def genPng(file,data,width=256,height=256,lines=True):

    canvas = PNGCanvas(width, height)
    canvas.color = [0xff,0xff,0xff,0xff]
    canvas.filledRectangle(0, 0, width, height)
    canvas.color = [0,0,0,0xff]

    # open the file
    data = compute(sys.argv[1])

    x = [row[0] for row in data]
    y = [row[1] for row in data]

    x_max = max(x)
    x_min = min(x)

    y_max = max(y)
    y_min = min(y)

    sx = width / float((x_max - x_min))
    sy = height / float(y_max - y_min) 

    print "X: {%04f,%04f}" % (x_min,x_max)
    print "Y: {%04f,%04f}" % (y_min,y_max)
    print "S: {%04f,%04f}" % (sx,sy)

    # get the max and min of the x value
    last = []

    for row in data:
        px = int((row[0]-x_min) * sx) 
        py = int((row[1]-y_min) * sy)
        
        if lines and last != []:
            canvas.line(last[0],last[1],px,py)
        else: canvas.point(px,py)

        if lines: last = (px,py)

    # write to file
    f = open("test.png", "wb")
    f.write(canvas.dump())
    f.close()


if __name__ == '__main__':
    
    outfile = "test.png"
    data = compute(sys.argv[1])
    genPng(outfile,data)
