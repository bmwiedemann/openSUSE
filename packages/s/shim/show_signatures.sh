#!/bin/bash
# show signatures on a PE binary
set -e

infile="$1"

if [ -z "$infile" -o ! -e "$infile" ]; then
	echo "USAGE: $0 file.efi"
	exit 1
fi

pesign -S -i "$infile"
