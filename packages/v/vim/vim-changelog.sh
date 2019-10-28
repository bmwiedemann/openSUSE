#!/usr/bin/env zsh

directory=http://ftp.vim.org/pub/vim/patches
version=8.1

echo "Updated to version $version.$(echo $2 | sed 's/^*//'), fixes the following problems"
for i in {$1..$2}; do
    curl $directory/$version/$version.$i -s | grep -v "Binary file (standard input) matches" | \
    tr -d '\n' | grep -oP "Problem:.*Solution:" | sed s,"Problem:    ","  * ", | sed s,"Solution:",, | \
    tr '\t' '\n' | sed  s,'           ','', | fmt -w 80
done
