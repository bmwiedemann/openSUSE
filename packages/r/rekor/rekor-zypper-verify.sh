#!/bin/bash
#
# This scripts verifies presence of the current repomd signatures in the rekor log
# for each of existing libzypp tracked repos.
#

zypper -q refresh

for repo in /etc/zypp/repos.d/*.repo
do
	if grep enabled=1 $repo >/dev/null; then
		repodirname=`grep '^\[' "$repo"|sed -e 's/.*\[//;s/\].*//;'`
		name="`grep ^name= $repo|sed -e 's/name=//;'`"
		if [ "x$name" == "x" ]; then
			name="$repodirname"
		fi

		# echo "name: $name, repodirname $repodirname"

		repodata="/var/cache/zypp/raw/$repodirname/repodata"
		if [ -d "$repodata" ]; then
			if rekor-cli verify --artifact "$repodata/repomd.xml" --signature "$repodata/repomd.xml.asc" --public-key "$repodata/repomd.xml.key" >/dev/null 2>&1; then
				echo "$name repomd.xml signature is in rekor log"
			else
				echo "$name repomd.xml signature is NOT in rekor log"
			fi
		else
			echo "$name has no repodata/ directory in $repodata, not a RPM-MD repository?"
		fi
	fi
done
