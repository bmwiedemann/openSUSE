#!/bin/sh
  
#--------------------------------------
#test -f /.profile && . /.profile

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

# Disable binding to localhost only, doesn't make sense in a container
sed -i -e 's|^\(bind-address.*\)|#\1|g' /etc/my.cnf
# Disable log_error to log to stderr
sed -i -e 's|^\(log-error.*\)|#\1|g' /etc/my.cnf

exit 0
