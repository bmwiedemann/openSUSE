#!/bin/bash

version=$(awk '/^Version:/ {print $2}' python-pymisp.spec)
revision=$(wget "https://github.com/MISP/PyMISP/tree/v$version/pymisp/data" -O - | awk '/\/MISP\/misp-objects\/tree\//' | egrep -o "[[:alnum:]]{40}")
sed -i "s/^\%define misp_objects_revision.*$/%define misp_objects_revision $revision/" python-pymisp.spec
