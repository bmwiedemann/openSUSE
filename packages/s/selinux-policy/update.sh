#!/bin/sh

date=$(date '+%Y%m%d')

echo Update to $date

rm -rf fedora-policy container-selinux

git clone --depth 1 https://github.com/fedora-selinux/selinux-policy.git
git clone --depth 1 https://github.com/containers/container-selinux.git

mv selinux-policy fedora-policy-$date
rm -rf fedora-policy-$date/.git*
mv container-selinux/container.* fedora-policy-$date/policy/modules/services/

rm -f fedora-policy?$date.tar*
tar cf fedora-policy-$date.tar fedora-policy-$date
bzip2 fedora-policy-$date.tar
rm -rf fedora-policy-$date container-selinux

sed -i -e "s/^Version:.*/Version:        $date/" selinux-policy.spec

echo "remove old tar file, then osc addremove"
