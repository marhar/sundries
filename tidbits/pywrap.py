#!/usr/bin/env python

import sys
import os

template="""
// %(prog)s -- generated by pywrap, don't modify

#include "Python.h"
#include <stdio.h>

char %(prog)s_py[] = {
    %(bytes)s
};

int main(int argc, char** argv)
{
    int rc;
    putenv("PYTHONHOME=/u0/mh/py/bin");
    Py_SetProgramName(argv[0]);
    Py_Initialize();
    rc = PyRun_SimpleString(%(prog)s_py);
    Py_Finalize();
    exit(rc);
}
"""

make="""
pywrap ora.py>ora.c;cc -o ora -I/u0/mh/py/include/python2.5
ora.c -L/u0/mh/py/lib/python2.5/config -lpython2.5 -lm -ldl -lSDL -lutil
"""

def file2str(fn):
    """encode a file of bytes to C array of numbers"""
    max=14
    s=''
    fd=open(fn)
    n=max
    for byte in fd.read():
        if n <= 0:
            n=max
            s+='\n    '
        n-=1
        s += '0x%02x,'%(ord(byte))
    return s

def main():
    prog=sys.argv[1]
    bytes=file2str(prog)
    prog2=os.path.splitext(os.path.basename(prog))[0]
    print template%{'prog':prog2,'bytes':bytes}

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
