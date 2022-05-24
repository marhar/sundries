#!/bin/bash
# populate git with some linear revisions
# start by: git init

for i in able baker; do
echo $i >> a.txt
git add .
git commit -m zz-$i
done

for i in charlie dog; do
echo $i >> a.txt
echo $i >> b.txt
git add .
git commit -m zz-$i
done

for i in echo foxtrot; do
echo $i >> a.txt
echo $i >> b.txt
echo $i >> c.txt
git add .
git commit -m zz-$i
done
