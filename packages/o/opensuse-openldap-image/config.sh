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

# Fix path so that update-ca-certificates does not complain
# [bsc#1175340]
rm /etc/ssl/certs && ln -sf /var/lib/ca-certificates/pem /etc/ssl/certs
