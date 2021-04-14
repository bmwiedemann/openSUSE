#!/bin/sh
JAVA=java
test -e "$JAVA_ROOT/../jre-1.8.0-openjdk/bin/java" && JAVA="$JAVA_ROOT/../jre-1.8.0-openjdk/bin/java"
pushd /usr/share/rescue
exec "$JAVA" -jar Rescue.jar "${@}"
popd
