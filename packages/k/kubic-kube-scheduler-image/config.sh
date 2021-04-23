#!/bin/sh
  
#--------------------------------------
#test -f /.profile && . /.profile

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

ln -sf /usr/bin/kube-scheduler /usr/local/bin/kube-scheduler 

exit 0
