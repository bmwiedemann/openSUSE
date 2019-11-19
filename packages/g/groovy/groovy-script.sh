#!/bin/bash
set -e

if [ -f /usr/share/java-utils/java-functions ] ; then
  . /usr/share/java-utils/java-functions
  set_jvm
  set_javacmd
fi

export GROOVY_HOME="${GROOVY_HOME:-/usr/share/groovy}"
export GROOVY_CONF="${GROOVY_CONF:-/etc/groovy-starter.conf}"
export JAVA_HOME
export JAVACMD

. ${GROOVY_HOME}/bin/startGroovy
startGroovy @CLASS@ "${@}"
