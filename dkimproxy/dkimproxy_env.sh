#!/bin/sh
  
# extract configuration from /etc/sysconfig/dkimproxy and write
# environment to /run/sysconfig/dkimproxy to be used by
# systemd unit files.

if [ -r /etc/sysconfig/dkimproxy ]; then
	cat /etc/sysconfig/dkimproxy > /run/sysconfig/dkimproxy
fi

echo "#Fully qualified hostanme" >> /run/sysconfig/dkimproxy
echo "HFQHN=$( hostname -f )" >> /run/sysconfig/dkimproxy


