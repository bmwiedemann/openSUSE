#!/bin/bash
# extract ascii armored signature from a PE binary
set -e

infile="$1"

if [ -z "$infile" -o ! -e "$infile" ]; then
	echo "USAGE: $0 file.efi"
	exit 1
fi

# wtf?
(pesign -h -P -i "$infile";
perl $(dirname $0)/timestamp.pl "$infile";
pesign -a -f -e /dev/stdout -i "$infile")|cat
