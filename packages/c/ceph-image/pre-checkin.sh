#!/bin/bash
#
# Generate the kiwi file for the given target.

image="ceph-image"
history="$(sed -n "s/^-[ ]//p" <${image}.changes | head -1)"
target=${1:-tumbleweed}
if [ ! -e ${target}.xml ]; then
  echo "Unknown target: ${target}.xml must exist!"
  exit 1
fi
xsltproc --stringparam history "$history" "${image}.xsl" "${target}.xml" > "${image}.kiwi"

