#!/bin/bash
#
# Updates documentation generation files to latest upstream version

export PATH=/bin:/usr/bin

rx='^%define documentation[[:space:]]+([a-f0-9]+)[[:space:]]*$'

ver=`cat tidy.spec | grep '^%define documentation'`
[[ $ver =~ $rx ]]
ver=${BASH_REMATCH[1]}

git clone https://github.com/htacg/html-tidy.org.api.git
new_ver=`cd html-tidy.org.api; git log -1 --pretty=%h`
if [[ $new_ver = $ver ]]; then
    echo "Currently up to date."
    exit 0
fi

cd html-tidy.org.api
osc log -p $ver..$new_ver -- tidy-html5-doxygen/
echo "Last chance to abort before update .... and abort if upstream did nothing interesting"
read
if [ $? -ne 0 ]; then
    echo "Aborting update."
    exit 1
fi

echo "Updating version $ver to $new_ver"

cd html-tidy.org.api
git archive --format=tar $new_ver tidy-html5-doxygen/ | gzip -9 > ../tidy-html5-doxygen-$new_ver.tar.gz
cd ..

sed -ie "s/\(define documentation\)\(\W\+\)\($ver\)/\1\2$new_ver/" tidy.spec
osc rm  tidy-html5-doxygen-$ver.tar.gz
osc add tidy-html5-doxygen-$new_ver.tar.gz

