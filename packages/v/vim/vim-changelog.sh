#!/usr/bin/env zsh

directory=https://ftp.nluug.nl/pub/vim/patches/
version=9.0

if [ $# -ne 2 ]; then
    echo "usage: $0 <old-minor-version> <new-minor-version>" 1>&2
    exit 1
fi

echo "Updated to version $version.$(echo $2 | sed 's/^*//'), fixes the following problems"
for i in $(seq -w $1 $2); do
    curl $directory/$version/$version.$i -s | grep -v "Binary file (standard input) matches" | \
    tr -d '\n' | grep -oP "Problem:.*Solution:" | sed s,"Problem:    ","  * ", | sed s,"Solution:",, | \
    tr '\t' '\n' | sed  s,'           ','', | fmt -w 80
done
