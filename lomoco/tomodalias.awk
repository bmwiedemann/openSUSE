#!/bin/awk -f
BEGIN {
	FS = ","
	ORS=""
	print "Supplements:"
}

$1 ~ /0xc[a-f0-9][a-f0-9][a-f0-9]/ {
	printf " modalias(usb:v%04Xp%04X*dc*dsc*dp*ic*isc*ip*)", 0x46d, strtonum(substr($1, index($1, "x")-1))
}

END {
	print "\n"
}
