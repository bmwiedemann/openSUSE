#!/bin/bash
set -euxo pipefail
# Fix the filesystem label of the ignition partition, uppercase doesn't work with ignition
e2label /dev/loop0p3 ignition
# Create ignition directory
mkdir /ignition/ignition
chown -R tik:users /ignition
