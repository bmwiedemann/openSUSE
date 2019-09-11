#!/bin/sh
# this script has a few assumptions:
# 1. if port 1026 is in use, another lighttpd test suite is running
# 2. if the php on port 1026 is shut down. the lighttpd on 2048 is taken down aswell
# 
# start php fast cgi for the test suite
function startphp() {
  MAX_WAIT=120
  SLEEP_TIME=2
  for ((i = $MAX_WAIT ; i> 0 ; i-$SLEEP_TIME)) ; do
    $PHP -b 1026 &
    PHP_PID="$!"
    sleep $SLEEP_TIME
    kill -0 $PHP_PID && return 0
  done
  return 1
}
startphp || exit 1
make check
RC="$?"
kill $PHP_PID ||:
exit $RC
