#!/bin/sh
  
#--------------------------------------
#test -f /.profile && . /.profile

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

for i in /usr/bin/etcdctl* ; do
  ln -sf $i /usr/local/bin/`basename $i`
done
for i in /usr/sbin/etcd* ; do
  ln -sf $i /usr/local/bin/`basename $i`
done
ln -sf /usr/bin/migrate /usr/local/bin/
ln -sf /usr/bin/migrate-if-needed.sh /usr/local/bin/

exit 0
