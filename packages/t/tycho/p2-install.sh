#!/bin/sh
set -e

_prefer_jre="true"
. /usr/share/java-utils/java-functions

set_jvm

set_classpath \
    beust-jcommander \
    eclipse/osgi \
    slf4j/api \
    slf4j/simple \
    tycho/org.fedoraproject.p2 \
    tycho/xmvn-p2-installer-plugin \
    xmvn/xmvn-api \
    xmvn/xmvn-core \

MAIN_CLASS=org.fedoraproject.p2.app.P2InstallerApp
run "$@"
