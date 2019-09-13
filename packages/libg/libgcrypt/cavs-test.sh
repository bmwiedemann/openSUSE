#!/bin/bash
#
# This is the driver script around the actual FIPS testing
# Written by: Stephan Müller <sm@atsec.com>
# (c) atsec information security corporation

# The easiest way to perform the cipher compliance testing
# is the following:
#
# 1. patch/compile/copy the openssl binary with the patch if necessary
#    (old versions hang when running the MC test if unpatched)
#
# 2. unpack the test vector ZIP file to a local dir
#
# 3. set PATH in a way that cavs_driver.pl is found
#
# 4. go to the local dir where you unzipped the test vector archive and execute
#    $0 
#
# 5. send atsec the prepared CAVS_results-*.zip archive found in the same dir

DATE=$(date +%Y%m%d)
ARCH=$(uname -m)
PATH=$PATH:$(pwd)

# test interface to be used
# can be overridden by passing an argument to this script
# possible values are:
#	openssl     OpenSSL (default)
#	libgcrypt   Libgcrypt
#	cryptoapi   Kernel
INTERFACE="libgcrypt"

if [ "$1" == "-I" -a -n "$2" ]; then
	INTERFACE="$2"
fi

for i in $(find ./ -name "*.req");
do
(
	cd $(dirname $i) || exit 1

	# We have to see whether we check on DSA based on path name
	echo $(dirname $i) | if [ ! $(grep -v DSA) ]; then
		/usr/lib/libgcrypt/cavs_driver.pl -I $INTERFACE -D $(basename $i)
	else
		/usr/lib/libgcrypt/cavs_driver.pl -I $INTERFACE $(basename $i)
	fi


	# for CAVS, we have path/req/<testvectors>
	# and want to have the responses in path/resp/*.rsp
	if [ $(basename $(dirname $i)) = "req" ]; then
		mkdir ../resp > /dev/null 2>&1
		outfile="$(basename $i .req).rsp"
		mv "$outfile" ../resp/
	fi
) &
done
wait
zip -r CAVS_results-$ARCH-$DATE.zip $(find ./ -name "*.rsp")
