#!/bin/bash

#======================================
# Functions...
#--------------------------------------
test -f /.kconfig && . /.kconfig
test -f /.profile && . /.profile

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

#======================================
# Imitate upstream image:
# velero/velero
# same file structure
#--------------------------------------
ln -sf /usr/bin/velero /velero

exit 0
