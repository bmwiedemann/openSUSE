#!/bin/sh
zypper -n in openSUSE-release -dummy-release
zypper -n in --no-recommends python3-pika nfs-client procmail perl-Text-Glob pinentry haveged git-core osc
systemctl enable --now haveged

mkdir -p /data/
echo "/dev/vdb /data   ext4 noatime,nodiratime 2 2" >> /etc/fstab
echo "hilbert.suse.de:/work /mounts/work nfs ro,rsize=1048576,namlen=255 0 0" >> /etc/fstab

useradd -m opensusegit
useradd -m opensuserabbit
useradd -m git
chsh git -s $(which git-shell)

# get git repo as non-root
cd /data
su - obsbugzilla -c opensusegit git clone git@github.com:bmwiedemann/openSUSE.git
cd openSUSE

for s in opensuserabbit.service opensusegit1.service ; do
  install -m 644 -p setup/$s /etc/systemd/system
  systemctl enable --now $s
done

#TODO install ipfs
#su - obsbugzilla -c opensusegit ipfs init
