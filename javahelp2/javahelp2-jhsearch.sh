#!/bin/sh
# 
# jhsearch script
# JPackage project (http://jpackage.sourceforge.net)
# $Id$

# Source functions library
. /usr/share/java-utils/java-functions

# Allow system prefs
if [ -f /etc/jhsearch.conf ] ; then 
  . /etc/jhsearch.conf
fi

# Allow user-defined prefs
if [ -f $HOME/.jhsearchrc ] ; then 
  . $HOME/.jhsearch
fi

# Configuration
MAIN_CLASS=com.sun.java.help.search.QueryEngine
BASE_JARS=javahelp2

# Set parameters
set_jvm
set_classpath $BASE_JARS
set_flags $BASE_FLAGS
set_options $BASE_OPTIONS

# Let's start
run "$@"
