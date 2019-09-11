#!/bin/sh
#
# Slide WebDAV client script
# JPackage Project <http://www.jpackage.org/>
# $Id$

# Source functions library
. /usr/share/java-utils/java-functions

# Configuration
MAIN_CLASS=org.apache.webdav.cmd.Slide

# Set parameters
set_jvm
CLASSPATH=$(build-classpath slide jakarta-commons-httpclient antlr)
set_flags $BASE_FLAGS
set_options $BASE_OPTIONS

# Let's start
run "$@"
