#!/Users/marhar/anaconda2/bin/python
#!/usr/bin/python

# Python script to find STL dimensions
# Requirements: sudo pip install numpy-stl

import math
import os
import sys

import stl
from stl import mesh
import numpy

if len(sys.argv) < 2:
    sys.exit('Usage: %s [stl file]' % sys.argv[0])

if not os.path.exists(sys.argv[1]):
    sys.exit('ERROR: file %s was not found!' % sys.argv[1])

# this stolen from numpy-stl documentation
# https://pypi.python.org/pypi/numpy-stl

# find the max dimensions, so we can know the bounding box, getting the height,
# width, length (because these are the step size)...
def find_mins_maxs(obj):
    minx = maxx = miny = maxy = minz = maxz = None
    for p in obj.points:
        # p contains (x, y, z)
        if minx is None:
            minx = p[stl.Dimension.X]
            maxx = p[stl.Dimension.X]
            miny = p[stl.Dimension.Y]
            maxy = p[stl.Dimension.Y]
            minz = p[stl.Dimension.Z]
            maxz = p[stl.Dimension.Z]
        else:
            maxx = max(p[stl.Dimension.X], maxx)
            minx = min(p[stl.Dimension.X], minx)
            maxy = max(p[stl.Dimension.Y], maxy)
            miny = min(p[stl.Dimension.Y], miny)
            maxz = max(p[stl.Dimension.Z], maxz)
            minz = min(p[stl.Dimension.Z], minz)
    return minx, maxx, miny, maxy, minz, maxz

def bounding_box(obj):
    minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(obj)
    return (maxx - minx, maxy - miny, maxz - minz)

main_body = mesh.Mesh.from_file(sys.argv[1])
bbx, bby, bbz = bounding_box(main_body)

print "%.0f x %.0f x %.0f" % (bbx, bby,bbz)
