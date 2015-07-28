a=6         -- columns to split picture into
b=6         -- rows to split picture into
c=1         -- measure mode (Y,U,V R,G,B) <96> U=0, Y=1, V=2, R=3, G=4, B=5
d=300000    -- timeout (mSec)
e=200       -- comparison interval (msec)
f=5         -- threshold (difference in cell to trigger detection)
g=1         -- draw grid (0=no, 1=yes)  
h=0         -- not used in LUA
i=2         -- region masking mode: 0=no regions, 1=include, 2=exclude
j=1         --      first column
k=1         --      first row
l=5         --      last column
m=5         --      last row
n=0         -- optional parameters  (1=shoot immediate)
o=2         -- pixel step
p=10       -- triggering delay (msec)
 
repeat
 
   zones = md_detect_motion( a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p)
 
   if( zones > 0 ) then
        shoot()
   end
 
until (false)
