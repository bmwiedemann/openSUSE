#!/bin/sh
  
#======================================
# Functions...
#--------------------------------------
test -f /.profile && . /.profile

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

for i in install run uninstall ; do
  sed -i 's|^PATH="/bin:/sbin"|PATH="/usr/bin:/usr/sbin:/bin:/sbin"|g' /container/atomic-${i}
done

rm -f /usr/lib/os-release && ln -sv /host/usr/lib/os-release /usr/lib/os-release

ln -s /host/proc/1 /container/target-namespace
chmod -v +x /container/atomic-install
chmod -v +x /container/atomic-uninstall
chmod -v +x /container/atomic-run
