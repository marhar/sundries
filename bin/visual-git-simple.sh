#!/bin/bash
# visual git helper

if [ $# -eq 0 ] ; then
	DD=.
else
	DD=$*
fi

rungit () {
	(
	cd $d
	echo ================================= $d
	git status|cat
	echo --
	git branch
	echo --
	git log --pretty=oneline --abbrev-commit --graph|cat
	) 2>&1 | sed 's/$/[0K/'
}

while true; do
	echo -n '[H'$(date +%S)
	for d in $DD; do
		rungit $d
	done
	echo -n '[J'
	sleep 1
done
