#!/usr/bin/busybox sh
  
#======================================
# Functions...
#--------------------------------------
# don't source .kconfig, works only with bash
#test -f /.kconfig && . /.kconfig
test -f /.profile && . /.profile

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

/usr/bin/busybox ln -sf busybox /usr/bin/rpm
/usr/bin/busybox ln -sf busybox /usr/bin/rpm2cpio

exit 0
