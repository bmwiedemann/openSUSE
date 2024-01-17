#!/bin/sh
  
#======================================
# Functions...
#--------------------------------------
test -f /.profile && . /.profile

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

/usr/sbin/adduser -S -g "SpamAssassin Milter" -h /var/lib/spamass-milter sa-milter
