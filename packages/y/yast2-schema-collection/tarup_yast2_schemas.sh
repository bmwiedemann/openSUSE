#!/bin/bash

repos="tw leap15.3 sle-15-sp3 sle-15-sp2 sle-12-sp5 sle-12-sp4 sles-11-sp4"

url_repos="leap15.2 leap15.1"

# Leap updates are not internally available
# Therefore file system regular expression on arch/version do not work
# leap15.x therefore need to be modified manually on every new avail
# update and are only packaged for x86_64

declare -A locs
locs=(
    "tw"          "/mounts/dist/openSUSE/openSUSE-Tumbleweed/*/DVD1/*/yast2-schema*.rpm"
    "leap15.3"    "/mounts/dist/openSUSE/openSUSE-Leap-15.3/*/DVD1/*/yast2-schema*.rpm"
    "sle-15-sp3"  "/mounts/dist/updates/ibs/SUSE:/SLE-15-SP3:/GA/standard/*/yast2-schema*.rpm"
    "sle-15-sp2"  "/mounts/dist/updates/ibs/SUSE:/SLE-15-SP2:/Update/standard/*/yast2-schema*.rpm"
    "sle-12-sp5"  "/mounts/dist/updates/ibs/SUSE:/SLE-12-SP5:/Update/standard/*/yast2-schema*.rpm"
    "sle-12-sp4"  "/mounts/dist/updates/ibs/SUSE:/SLE-12-SP4:/Update/standard/*/yast2-schema*.rpm"
    "sles-11-sp4" "/mounts/dist/updates/ibs/SUSE:/SLE-11-SP4:/Update/standard/*/yast2-schema*.rpm"
)

declare -A url_locs
url_locs=(
    "leap15.2"    "http://download.opensuse.org/update/leap/15.2/oss/x86_64/yast2-schema-4.2.13-lp152.2.3.1.x86_64.rpm"
    "leap15.1"    "http://download.opensuse.org/update/leap/15.1/oss/x86_64/yast2-schema-4.1.8-lp151.2.6.1.x86_64.rpm"
)

archs="x86_64 aarch64 ppc64le ppc64 s390x"
prefix="/usr/share/yast2-schemas"
pkg_name="/yast2-schema-collection"
dir=$(mktemp -d)
t_dir=$(mktemp -d)
root_dir="$dir/$pkg_name"
mkdir "$root_dir"

set -x

pushd "$root_dir"
for repo in $repos;do
    for arch in $archs;do
	for file in $(ls -1 ${locs["$repo"]}|grep "$arch.rpm$"); do
	    if [ -r $file  ];then
		echo $file
		rpm2cpio "$file" |cpio -i -d -D "$t_dir"
		mkdir -p "$root_dir/$repo/$arch"
		rpm -qp -i "$file" >"$root_dir/$repo/$arch/rpm.info"
		if [ ! -d "$t_dir"/usr/share/YaST2/schema/autoyast/rng ];then
		    echo "Could not find rng files [${t_dir}/usr/share/YaST2/schema/autoyast/rng] extracted from rpm [$file]"
		    exit 1
		fi
		mv "$t_dir"/usr/share/YaST2/schema/autoyast/rng/* "$root_dir/$repo/$arch"
	    fi
	done
    done
done

for repo in $url_repos;do
    tmp_f=$(mktemp)
    echo "Getting rpm via URL ${url_locs[$repo]}"
    wget ${url_locs[$repo]} -O $tmp_f
    rpm2cpio "$tmp_f" |cpio -i -d -D "$t_dir"
    mkdir -p "$root_dir/$repo/x86_64"
    rpm -qp -i "$tmp_f" >"$root_dir/$repo/x86_64/rpm.info"
    if [ ! -d "$t_dir"/usr/share/YaST2/schema/autoyast/rng ];then
	echo "Could not find rng files [${t_dir}/usr/share/YaST2/schema/autoyast/rng] extracted from rpm [$file]"
	exit 1
    fi
    mv "$t_dir"/usr/share/YaST2/schema/autoyast/rng/* "$root_dir/$repo/x86_64"
    rm -rf ${tmp_f}
done

popd
#rm -rf "$t_dir"
echo $dir
tar -cJf yast2-schema-collection.tar.xz -C "$dir" yast2-schema-collection


