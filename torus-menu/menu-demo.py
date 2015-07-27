#!/usr/bin/env python

import os
import sys

def ww(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def ee(s):
    sys.stderr.write(s+'\n')
    sys.stderr.flush()

def vtboot()  : ww('\033[!p')
def vtchide() : ww('\033[?25l')
def vtcdisp() : ww('\033[?25h')
def vtg0()    : ww('\033(A')
def vtg1()    : ww('\033(0')
def vthome()  : ww('\033[H')
def vted()    : ww('\033[2J')
def vtreset() : ww('\033[0m')
def vthili()  : ww('\033[7m')
def vtcup(r,c): ww('\033[%d;%dH'%(r,c))
vtalt="""
j Lower-right corner
k Upper-right corner
l Upper-left corner
m Lower-left corner
n Crossing lines
q Horizontal line
t Left "T"
u Right "T"
v Bottom "T"
w Top "T"
x Vertical bar
"""

def box(nr,nc):
    vthome()
    vted()
    vtg1()
    wid0=12
    nchars=wid0*nc-1
    ww('%s%s%s'%('l','q'*nchars,'k'))
    for r in range(2,nr+2):
        #vtcup(r,1)
        #ww('%s%s%s'%('x',' '*nchars,'x'))
        vtcup(r,1)
        ww('x')
        vtcup(r,nchars+2)
        ww('x')
    vtcup(nr+2,1)
    ww('%s%s%s'%('m','q'*nchars,'j'))
    vtg0()

def word(r,c,hili=False):
    txt='r%02dc%02di%02d'%(r,c,r+c*NROWS)
    cwid=len(txt)+3
    if hili: vthili()
    else: vtreset()
    vtcup(r+2,(c*cwid)+3)
    ww(txt)
    if hili: vtreset()
    else: vthili()

NROWS=22
NCOLS=7
NROWS=6
NCOLS=4

def allwords():
    for r in range(NROWS):
        for c in range(NCOLS):
            word(r,c)

def desc(rr,cc,calc):
    vtreset()
    vtcup(1,3)
    ww("%2d %2d %-8s"%(rr,cc,str(calc).split()[1]))

def rect(r,c):
    if r < 0: r = 0
    if r > NROWS-1: r=NROWS-1
    if c < 0: c = 0
    if c > NCOLS-1: c=NCOLS-1
    return (r,c)

def hcyl(r,c):
    # wrap
    if r < 0: r = NROWS-1
    if r > NROWS-1: r=0
    # c same as for rect
    if c < 0: c = 0
    if c > NCOLS-1: c=NCOLS-1
    return (r,c)

def vcyl(r,c):
    # r same as for rect
    if r < 0: r = 0
    if r > NROWS-1: r=NROWS-1
    # wrap
    if c < 0: c = NCOLS-1
    if c > NCOLS-1: c=0
    return (r,c)


def torus1(r,c):
    # wrap
    if r < 0: r = NROWS-1
    if r > NROWS-1: r=0
    # wrap
    if c < 0: c = NCOLS-1
    if c > NCOLS-1: c=0
    return (r,c)

def torus2(r,c):
    # wrap
    if r < 0: r = NROWS-1
    if r > NROWS-1: r=0
    # wrap and shift
    if c < 0:
        c = NCOLS-1
        r=r-1
        if r < 0: r=NROWS-1
    if c > NCOLS-1:
        c=0
        r=r+1
        if r > NROWS-1: r=0
    return (r,c)

def torus3(r,c):
    # wrap and shift
    if r < 0:
        r = NROWS-1
        c=c-1
        if c < 0: c=NCOLS-1
    if r > NROWS-1:
        r=0
        c=c+1
        if c > NCOLS-1: c=0
    # wrap
    if c < 0: c = NCOLS-1
    if c > NCOLS-1: c=0
    return (r,c)


def torus4(r,c):
    # wrap and shift
    if r < 0:
        r = NROWS-1
        c=c-1
        if c < 0: c=NCOLS-1
    if r > NROWS-1:
        r=0
        c=c+1
        if c > NCOLS-1: c=0
    # wrap and shift
    if c < 0:
        c = NCOLS-1
        r=r-1
        if r < 0: r=NROWS-1
    if c > NCOLS-1:
        c=0
        r=r+1
        if r > NROWS-1: r=0
    return (r,c)


def main():

    calc=rect
    rr=0
    cc=0

    os.system('stty raw -echo')
    box(NROWS,NCOLS)

    vtchide()
    word(rr,cc,True)
    allwords()

    word(rr,cc,True)
    desc(rr,cc,calc)
    while True:
        (dx,dy)=(0,0)
        k=sys.stdin.read(1)
        if   k=='1': calc=rect
        elif k=='2': calc=hcyl
        elif k=='3': calc=vcyl
        elif k=='4': calc=torus1
        elif k=='5': calc=torus2
        elif k=='6': calc=torus3
        elif k=='7': calc=torus4
        elif k in ('\033','['): pass
        elif k in ('D','h'): (dx,dy)=(0,-1)
        elif k in ('B','j'): (dx,dy)=(1,0)
        elif k in ('A','k'): (dx,dy)=(-1,0)
        elif k in ('C','l'): (dx,dy)=(0,1)
        elif k=='q': break

        word(rr,cc,False)
        (rr,cc)=calc(rr+dx,cc+dy)
        word(rr,cc,True)
        desc(rr,cc,calc)

    cleanup()

def cleanup():
    vtboot()
    vtcup(NROWS+3,1)
    os.system('stty sane')

try:
    main()
except Exception,e:
    cleanup()
    raise e
