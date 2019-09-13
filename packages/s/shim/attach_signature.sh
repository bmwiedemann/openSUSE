#!/bin/bash
# attach ascii armored signature to a PE binary
set -e

sig="$1"
infile="$2"
if [ -z "$sig" -o ! -e "$sig" -o -z "$infile" -o ! -e "$infile" ]; then
	echo "USAGE: $0 sig.asc file.efi"
	exit 1
fi

outfile="${infile%.efi}-signed.efi"

pesign -m "$sig" -i "$infile" -o "$outfile"
