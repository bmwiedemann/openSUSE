#!/bin/sh

# compares symbols of $1 vs. $2
#    returns diff of the two global function tables
#

if test $# -ne 2; then
   echo "$0 library1 library2"
   exit 2
fi

PARAMS='[0-9a-f]\+[[:space:]]\+g[[:space:]]\+F[[:space:]]\+\.text[[:space:]]\+[0-9a-f]\+[[:space:]]\+'

objdump -t $1 | grep $PARAMS | sed -e 's#'$PARAMS'##' | sort > temp.$$
objdump -t $2 | grep $PARAMS | sed -e 's#'$PARAMS'##' | sort | diff temp.$$ -

RET=$?

rm temp.$$

exit $RET
