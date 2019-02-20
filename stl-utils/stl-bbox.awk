#!/bin/sh
# note: works with ascii stl only
awk '
BEGIN {
    m = 1000000;	# Make larger if your model is really large
    maxx = -m;
    minx = m;
    maxy = -m;
    miny = m;
    maxz = -m;
    minz = m;
}

$1 == "vertex" {
    maxx = ($2>maxx ? $2 : maxx);
    minx = ($2<minx ? $2 : minx);
    maxy = ($3>maxy ? $3 : maxy);
    miny = ($3<miny ? $3 : miny);
    maxz = ($4>maxz ? $4 : maxz);
    minz = ($4<minz ? $4 : minz);
}

END {
    print minx,miny,minz;
    print maxx,maxy,maxz;
}
' $*
