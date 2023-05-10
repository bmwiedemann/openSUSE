#!/bin/bash

#
# Fetch npm module tarball that is required to run unit tests
# which are not provided by upstream tarball
#
set -e

tar Jxf node-v*.tar.xz
cd node-v.*/tools/doc
npm ci
cd ../..
exec tar Jcf ../node_modules.tar.xz tools/doc/node_modules
