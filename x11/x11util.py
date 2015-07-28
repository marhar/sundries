import subprocess
import time
import os

#-----------------------------------------------------------------------
def mapstate(winid):
    """
    what is the mapped state of this window?
    returns 'NoWindow','IsUnMapped','IsViewable'
    """

    fd=subprocess.Popen('xwininfo -id "%s" 2>/dev/null'%(winid),shell=True,
                         stdout=subprocess.PIPE).stdout
    for line in fd:
        x=line.split()
        if x[0:2] ==['Map','State:']:
            return x[2]
    return 'NoWindow'

#-----------------------------------------------------------------------
def waitfor(winid,delay=0.5):
    """wait for a window to become visible"""

    while True:
        state=mapstate(winid)
        if state=='IsViewable':
            break
        time.sleep(delay)

#-----------------------------------------------------------------------
def windowid(name):
    """map a window name to a window id"""
    fd=subprocess.Popen('xlsclients -l',shell=True,
                         stdout=subprocess.PIPE).stdout
    for line in fd:
        x=line.split()
        if x[0]=='Window':
            id=x[1][:-1]
        if x[0]=='Name:' and x[1]==name:
            return id
    raise Exception('no window named: %s'%(name))

#-----------------------------------------------------------------------
def windowpos(winid):
    """get the position of a window"""
    fd=subprocess.Popen('xwininfo -id %s'%(winid),shell=True,
                         stdout=subprocess.PIPE).stdout
    for line in fd:
        x=line.split()
        if x[0:1]==['Width:']:  ww=int(x[1])
        if x[0:1]==['Height:']: hh=int(x[1])
        if x[0:3]==['Absolute', 'upper-left', 'X:']: aulx=int(x[3])
        if x[0:3]==['Absolute', 'upper-left', 'Y:']: auly=int(x[3])
        if x[0:3]==['Relative', 'upper-left', 'X:']: rulx=int(x[3])
        if x[0:3]==['Relative', 'upper-left', 'Y:']: ruly=int(x[3])

    return (aulx-rulx,auly-ruly,ww,hh)

#-----------------------------------------------------------------------
def windowraise(winid):
    """raise the window"""
    os.system('xdotool windowraise %s'%(winid))

#-----------------------------------------------------------------------
def moveto(winid, x, y):
    """move window to (x,y)"""
    os.system('xdotool windowmove %s %d %d'%(winid,x,y))

#-----------------------------------------------------------------------
def slideto(winid,destx,desty,SLICES=25):
    """slide window to (x,y)"""
    posa=windowpos(winid)

    (startx,starty)=posa[0:2]
    dx=(destx-startx)/float(SLICES)
    dy=(desty-starty)/float(SLICES)
    for i in range(SLICES):
        cmd='xdotool windowmove %s %d %d'%(winid,startx+dx*i,starty+dy*i)
        os.system(cmd)
    os.system('xdotool windowmove %s %d %d'%(winid,destx,desty))


def position(winid1,pos,winid2,func):
    """move win1 relative to win2"""

    macoffset=22

    (x1,y1,w1,h1)=windowpos(winid1)
    (x2,y2,w2,h2)=windowpos(winid2)

    if pos == 'topof':
        dx=x2
        dy=y2-h1    - macoffset
    elif pos == 'bottomof':
        dx=x2
        dy=y2+h2    + macoffset
    elif pos == 'leftof':
        dx=x2-w1
        dy=y2
    elif pos == 'rightof':
        dx=x2+w2
        dy=y2

    func(winid1,dx,dy)
