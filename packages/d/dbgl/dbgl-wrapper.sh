#!/bin/bash
# use right java version
#JAVA_HOME=/etc/alternatives/jre_11
# set jar-entry-class
MAIN_CLASS="org.dbgl.gui.Launcher"
# source the jpackage helpers and set environment
VERBOSE=1
. /usr/share/java-utils/java-functions
set_javacmd
check_java_env
set_jvm_dirs
# If the memory run short it can help to use set_options
# Xms set the initial and minimum Java heap size, Xmx set the maximum Java heap size
# default: Xms (25% of the amount of free physical memory in the system, up to 16 MB and at least 8 MB)
# default: Xmx (32bit: 50% of available physical memory up to 1 GB, 64bit: 50% of available physical memory up to 32 GB)
set_options "-Xms256M" "-Xmx1G" "-Ddbgl.data.userhome=true"
CLASSPATH=`build-classpath dbgl`
run "$@"

