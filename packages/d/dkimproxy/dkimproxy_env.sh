#!/bin/sh
  
# extract configuration from /etc/sysconfig/dkimproxy and write
# environment to /run/sysconfig/dkimproxy to be used by
# systemd unit files.

if [ -r /etc/sysconfig/dkimproxy ]; then
	cat /etc/sysconfig/dkimproxy > /run/dkimproxy/sysconfig
fi

echo "#Fully qualified hostanme" >> /run/dkimproxy/sysconfig
echo "FQHN=$( hostname -f )" >> /run/dkimproxy/sysconfig


