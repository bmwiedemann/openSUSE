#!/bin/bash
# bash -x $0 linux.git tag
set -e
kernel=$1
if test $# -ne 2 || ! test -d "$1" || test "$2" = "${2#v}"; then
  echo "Usage: ${0##*/} linux.git tag"
  exit 1
fi
case $PWD in
  *:*)
    echo "do not call this in a directory with : - make will fail"
    exit 1
    ;;
esac

version=${2#v}
kernel_dir=linux-$version
header_dir="$PWD/linux-glibc-devel-$version"
if test -d "$kernel_dir"; then
  echo "$kernel_dir exists, remove it first."
  exit 1
fi
if ! mkdir "$header_dir"; then
  echo "$header_dir exists, remove it first."
  exit 1
fi
git clone --single-branch -b "$2" "$1" "$kernel_dir"
pushd "$kernel_dir"
cp Makefile "$header_dir"
make O="$header_dir" headers_install_all
# kvm.h and aout.h are only installed if SRCARCH is an architecture
# that has support for them. As the package is noarch we need to make
# sure we get the full support on x86
make SRCARCH=x86 O="$header_dir" headers_install_all
popd
pushd "$header_dir"
remove="arc c6x csky h8300 hexagon microblaze nds32 nios2 openrisc sh unicore32 xtensa"
for asm in $remove; do
  rm -rf usr/include/arch-$asm
done
rm -f Makefile .cache.mk
find -type f \( -name "..install.cmd" -or  -name ".install" \) -exec rm {} +
#-------------------------------------------------------------------
#Fri Sep  5 10:43:49 CEST 2008 - matz@suse.de

#- Remove the kernel version of drm headers, they conflict
#  with the libdrm ones, and those are slightly newer.
#
rm -rf usr/include/drm/
# Remove confusing empty uapi directory
test ! -d usr/include/uapi || rmdir usr/include/uapi
for dir in *; do
  case "$dir" in
    usr) ;;
    *) 
      if test -d "$dir"; then
	rm -rf "$dir"
      fi
      ;;
  esac
done
popd
du -sh "$header_dir/usr"
tar -cJf "$header_dir.tar.xz" --owner=root --group=root "${header_dir##*/}"
rm -rf "$header_dir" "$kernel_dir"

