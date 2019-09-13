#!/bin/sh
  
#--------------------------------------
#test -f /.profile && . /.profile

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

mknod /var/log/ulogd.pcap p
mv /etc/ulogd.conf.weave /etc/ulogd.conf

exit 0
