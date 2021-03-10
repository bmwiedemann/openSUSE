#!/bin/bash
# strip the signature from a PE binary
set -e

infile="$1"
if [ -z "$infile" -o ! -e "$infile" ]; then
	echo "USAGE: $0 file.efi"
	exit 1
fi

outfile="${infile%.efi}-unsigned.efi"

pesign -r -i "$infile" -o "$outfile"
