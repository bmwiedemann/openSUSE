#!/bin/sh
  
#======================================
# Functions...
#--------------------------------------
test -f /.profile && . /.profile

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

# fix shell of root, bash does not exist
sed -i -e 's|/bin/bash|/bin/sh|g' /etc/passwd

# Make sure su is working
rm /usr/bin/su
ln /usr/bin/busybox /usr/bin/su
chmod 4755 /usr/bin/su
