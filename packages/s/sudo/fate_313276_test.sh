#!/bin/sh

if [ $(id -u) -ne 0 ]; then
	printf "Please run the test as root.\n"
	exit 1
fi

if sudo -V | grep -q -- --with-sssd; then
	printf "OK: Sudo has support for SSSD compiled in.\n"
	exit 0
fi

printf "Error: SSSD support isn't compiled in.\n"
exit 1
