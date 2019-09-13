#!/bin/bash
# This script is called automatically during autobuild checkin.
# to remove unneccesary files that make legal checks hard

if tar tf OpenGL-*.tar.gz|grep -q glu.h ; then
    set -x
    set -e
    gzip -cd OpenGL-*.tar.gz > .tar.tmp
    tar --wildcards --delete -f .tar.tmp OpenGL-\*/include/GL/{glu,glut,freeglut}.h
    gzip -c9n .tar.tmp > OpenGL-*.tar.gz
fi
true
