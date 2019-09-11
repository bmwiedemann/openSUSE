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

/usr/bin/busybox ln -sf ../usr/bin/busybox /bin/ln
/usr/bin/busybox ln -sf ../usr/bin/busybox /bin/rm
/usr/bin/busybox ln -sf ../usr/bin/busybox /bin/mkdir
/usr/bin/busybox ln -sf ../usr/bin/busybox /bin/chmod
/usr/bin/busybox ln -sf busybox /usr/bin/sort
/usr/bin/busybox ln -sf busybox /usr/bin/uniq
/usr/bin/busybox ln -sf busybox /usr/bin/install
/usr/bin/busybox ln -sf busybox /usr/bin/dirname
/usr/bin/busybox ln -sf busybox /usr/bin/basename
/usr/bin/busybox.install / --symlinks
/bin/rm linuxrc
/bin/rm /usr/bin/busybox
/bin/rm /usr/bin/busybox.install
/bin/rm -rf /usr/share/busybox

exit 0
