#!/bin/sh

date=$(date '+%Y%m%d')

echo Update to $date

rm -rf fedora-policy container-selinux selinux-policy-contrib

git clone --depth 1 https://github.com/fedora-selinux/selinux-policy.git
git clone --depth 1 https://github.com/fedora-selinux/selinux-policy-contrib.git
git clone --depth 1 https://github.com/containers/container-selinux.git

mv selinux-policy fedora-policy
rm -rf fedora-policy/.git*
mv selinux-policy-contrib/* fedora-policy/policy/modules/contrib/
mv container-selinux/container.* fedora-policy/policy/modules/contrib/

rm -f fedora-policy.$date.tar*
tar cf fedora-policy.$date.tar fedora-policy
bzip2 fedora-policy.$date.tar
rm -rf fedora-policy container-selinux selinux-policy-contrib

sed -i -e "s/^Version:.*/Version:        $date/" selinux-policy.spec

echo "remove old tar file, then osc addremove"
