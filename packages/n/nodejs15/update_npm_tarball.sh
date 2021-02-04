#!/bin/bash

#
# Fetch npm module tarball that is required to run unit tests
# which are not provided by upstream tarball
#
# This is only needed for NodeJS 10.x+
#
set -e

tar Jxf node-v1*.tar.xz
cd node-v1*/tools/doc
npm i
cd ../..
exec tar Jcf ../node_modules.tar.xz tools/doc/node_modules
