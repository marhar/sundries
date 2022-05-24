#!/bin/bash
# populate git with some parallel revisions
# start by: git init

# create a feature branch and commit a file to it.
addone () {
	git branch feature_$1
	git checkout feature_$1
	echo $2 >>$1.txt
	echo $3 >>$1.txt
	git add $1.txt
	git commit -m "adding $1"
}

# create one file so we don't have an empty repo.
echo first > first.txt
git add .
git commit -m 'first commit'

addone rose 'O my Luve is like a red, red rose' 'That’s newly sprung in June'
addone shadow 'I have a little shadow' 'that goes in and out with me'
addone king 'I often wish I were a King' 'And then I could do anything.'
