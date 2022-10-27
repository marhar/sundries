#!/bin/bash

#echo -n 'E[H'
#sed 's/$/E[0K/'
#echo -n 'E[J'
printf '\033[H'; sed "s/$/$(printf '\033[0K')/"; printf '\033[J'
