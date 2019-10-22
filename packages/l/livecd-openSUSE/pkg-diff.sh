#!/bin/bash
if [ $# -ne 2 ]; then
	printf "Show a diff of installed packages in the various flavors.\nUsage: $0 project arch\n" 
	exit 1
fi

project=$1
arch=$2

fetch_pkglist() {
	local project=$1
	local package=$2
	local repo=$3
	local arch=$4
	local binaryname=$(osc ls -b ${project} ${package} -a ${arch} -r ${repo} | grep .packages | xargs)

	osc api /build/${project}/${repo}/${arch}/${package}/${binaryname} | awk -F\| '{ print $1 }' | sort -u
}

tmpdir=$(mktemp -d)
trap 'rm -rf ${tmpdir}' EXIT

for i in {x11,xfce,kde,gnome}; do
	fetch_pkglist openSUSE:Factory:Live livecd-tumbleweed-$i images ${arch} > ${tmpdir}/list-old
	fetch_pkglist ${project} livecd-tumbleweed-$i openSUSE_Tumbleweed ${arch} > ${tmpdir}/list-new
	echo "$i"
	diff -u ${tmpdir}/list-{old,new}	
done
