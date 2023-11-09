#!/bin/sh
  
# extract configuration from /etc/sysconfig/dkimproxy and write
# environment to /run/dkimproxy/sysconfig to be used by
# systemd unit files.

if [ -r /etc/sysconfig/dkimproxy ]; then
	cat /etc/sysconfig/dkimproxy > /run/dkimproxy/sysconfig
fi

echo "# Fully qualified hostname" >> /run/dkimproxy/sysconfig
echo "FQHN=$( hostname -f )" >> /run/dkimproxy/sysconfig


