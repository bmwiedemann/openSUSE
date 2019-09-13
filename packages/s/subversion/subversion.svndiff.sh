#!/bin/bash
# stupid svn has no 'svn diff -v -R $bignum' to grab all info for a single patch
export TZ=UTC
export LANG=C
export LC_ALL=C
shopt -s extglob
case "$1" in
	r+([0-9]))
	rev=${1#?}
	shift
	;;
	+([0-9]))
	rev=$1
	shift
	;;
esac
if test -z "$rev"
then
	echo "Usage: $0 <svnrepo revision number>"
	exit 1
fi
revprev=$(($rev - 1 ))
svn log -v -r $rev "$@"
svn diff -r $revprev:$rev "$@"
