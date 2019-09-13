#!/bin/bash
#
# Copyright (c) 2017 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# Author: Christian Goll <CGoll@suse.de>
#
TEST_FILE_NAME=no_btrfs_check
function usage() {
cat <<EOF
	$0 /DIR/TO/TEST
	The test will exactly fail if TEST is on the same fs as / and its 
	btrfs fs. As an overwrite option you can touch the file /etc/TEST/$TEST_FILE_NAME
	which will make the test always to suceed.
	Goal of this test is to have a handy script to create the awareness, that the 
	date in /DIR/TO/TEST my be lost on a fs-rollback.
EOF
}

if [ $# -ne "1" ] ; then 
	usage
	exit 1
fi
testdir=$1
# Test for every entry entry in /proc/mounts if the maximum depth
basedir="/"
depth=0
fstype=unknown
mountops=unknown
while IFS='' read -r entry || [[ -n "$entry" ]] ; do
	path=$(echo $entry | cut -f 2 -d ' ')
	echo $testdir | grep $path > /dev/null
	if [ x$? == "x1" ] ; then
		continue
	fi
	newdepth=$(echo $path | tr -d -c '/' | wc -m)
	if [ $newdepth -lt $depth ] ; then 
		echo "continue"
		continue
	fi
	depth=$newdepth
	fstype=$(echo $entry | cut -f 3 -d ' ')
	mountopts=$(echo $entry | cut -f 4 -d ' ')
	basedir=$path
done < /proc/mounts
if [ $fstype != "btrfs" ] ; then 
	exit 0
fi
echo $mountops | grep 'subvolid' > /dev/null
if [ $basedir != "/" ] ; then
	exit 0
fi
if [ -e "/etc/$(basename $testdir)/$TEST_FILE_NAME" ] ; then
	exit 0
fi
cat << EOF 
The start of the service failed as the directory $testdir" is located under
a btrfs root. On a filesystem rollback data could so become unaccessible or corrupted.
To start the service anyway run "touch /etc/$(basename $testdir)/$TEST_FILE_NAME" or
install the package with the suffix "skip-bcheck" associtated with the package of the
service
EOF
exit 1
