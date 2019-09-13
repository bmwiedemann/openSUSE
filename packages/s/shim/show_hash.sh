#!/bin/bash
# show hash of PE binary
set -e

infile="$1"

if [ -z "$infile" -o ! -e "$infile" ]; then
	echo "USAGE: $0 file.efi"
	exit 1
fi

pesign -h -P -i "$infile"
