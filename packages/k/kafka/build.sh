#!/bin/bash
set -xe

cleanup()
  {
  rm -rf /tmp/gradle*
  }

cleanup # Since we're making a mess in /tmp let's make sure previous runs of this script
        # haven't left their mess in there.

# We need a writable copy of everything in the kit package because of...reasons, among them:
# * Gradle attempts to create a lock file alongside its native library when
#   opening it
# * Gradle may mess with files in its cache.
# * gradle-project/ probably gets written to as well at some stage.

# tar appears to be the only way to create a proper copy of
# /usr/share/tetra/gradle/. `cp -a` and `cp -r` create symlinks in the gradle/
# copy in /tmp which will break the build.
tar -C /usr/share/tetra -cf - gradle gradle-project gradle-5.1 | tar -C /tmp -xf - || cleanup
/tmp/gradle-5.1/bin/gradle -PscalaVersion=2.11 --offline --gradle-user-home /tmp/gradle --project-cache-dir /tmp/gradle-project releaseTarGz -x signArchives || cleanup

cleanup
