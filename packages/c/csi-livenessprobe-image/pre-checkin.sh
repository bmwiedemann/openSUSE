#!/bin/bash
#
# Generate the kiwi file for the given target.

image="csi-livenessprobe-image"
target=${1:-tumbleweed}
if [ ! -e ${target}.xml ]; then
  echo "Unknown target: ${target}.xml must exist!"
  exit 1
fi
xsltproc "${image}.xsl" "${target}.xml" > "${image}.kiwi"

