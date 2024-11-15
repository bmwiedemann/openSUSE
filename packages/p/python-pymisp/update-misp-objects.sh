#!/bin/bash

set -x

version=$(awk '/^Version:/ {print $2}' python-pymisp.spec)
echo "Detected version $version"
revision=$(wget "https://github.com/MISP/PyMISP/tree/v$version/pymisp/data" -O - | awk '/\/MISP\/misp-objects\/tree\//' | grep -Eo 'misp-objects/tree/[[:alnum:]]{40}' | egrep -Eo "[[:alnum:]]{40}")
echo "Detected revision $revision"
sed -i "s/^\%define misp_objects_revision.*$/%define misp_objects_revision ${revision}/" python-pymisp.spec
rm misp-objects.tar.gz
osc service runall download_files
