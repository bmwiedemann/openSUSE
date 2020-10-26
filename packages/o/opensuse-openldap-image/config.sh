#!/bin/sh
  
#======================================
# Functions...
#--------------------------------------
test -f /.profile && . /.profile

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

echo "Move /etc/sysconfig/openldap away"
mv /etc/sysconfig/openldap /etc/sysconfig/openldap.example

# No default domain and standard password ...
rm /etc/openldap/slapd.conf

