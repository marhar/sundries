#!/bin/bash
# visual git helper

while true;do
	clear
	git status|cat
	echo --
	git branch
	echo --
	git log --pretty=oneline --abbrev-commit --graph|cat
	sleep 1
done
