#!/bin/sh
  
#--------------------------------------
#test -f /.profile && . /.profile

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

# Create configuration file to find manual page
echo "MANPATH /usr/share/man" > /etc/man.conf

exit 0
