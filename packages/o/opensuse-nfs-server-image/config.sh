#!/bin/sh
  
#--------------------------------------
#test -f /.kconfig && . /.kconfig
#test -f /.profile && . /.profile

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

# Disable NFSv3 by default
sed -i -e 's|NFS3_SERVER_SUPPORT=.*|NFS3_SERVER_SUPPORT="no"|g' /etc/sysconfig/nfs

# delete some default files
rm -fv /etc/exports

# make sure correct directories exist
mkdir -p /export
mkdir -p /var/lib/nfs
touch /var/lib/nfs/etab
touch /var/lib/nfs/rmtab

exit 0
