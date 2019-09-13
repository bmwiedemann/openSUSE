#!/bin/sh
  
#--------------------------------------
#test -f /.profile && . /.profile

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

ln -sf /usr/bin/kube-apiserver /usr/local/bin/kube-apiserver 

exit 0
