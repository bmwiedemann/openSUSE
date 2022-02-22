#!/bin/bash

# Autobuild doesn't support package names with macros. This script will update versions in package names.

ORIG_SPEC=${2%-mono}
ORIG_SPEC=${ORIG_SPEC%-qt5}
# Never update -mono file when it is already opened. It will break advanced build scripts:
if test "$2" != "$ORIG_SPEC" ; then
    exit
fi

if ! test -f $1/$ORIG_SPEC.spec ; then
    exit
fi

# Edit file to fit -glib2 build needs:
sed '
    s/spec file for package avahi/spec file for package avahi-glib2/;
    s/build_core\ 1/build_core 0/;
    s/build_glib2\ 0/build_glib2 1/;
    s/^.ame:.*/&-glib2/;
    # No more needed.
    #s/^..hangelog.*/& qt/;
    /^# WARNING: After editing/,/^# to update spec files/d
    /^%define[[:space:]]*_name/i \
# Do not edit this auto generated file! Edit avahi.spec.
' <$1/$ORIG_SPEC.spec >$1/$ORIG_SPEC-glib2.spec.new
perl $1/update_spec.pl $1/$ORIG_SPEC-glib2.spec.new attributes > $1/$ORIG_SPEC-glib2.spec
rm $1/$ORIG_SPEC-glib2.spec.new

# Edit file to fit -qt5 build needs:
sed '
    s/spec file for package avahi/spec file for package avahi-qt5/;
    s/build_core\ 1/build_core 0/;
    s/build_qt5\ 0/build_qt5 1/;
    s/^.ame:.*/&-qt5/;
    # No more needed.
    #s/^..hangelog.*/& qt/;
    /^# WARNING: After editing/,/^# to update spec files/d
    /^%define[[:space:]]*_name/i \
# Do not edit this auto generated file! Edit avahi.spec.
' <$1/$ORIG_SPEC.spec >$1/$ORIG_SPEC-qt5.spec.new
perl $1/update_spec.pl $1/$ORIG_SPEC-qt5.spec.new attributes > $1/$ORIG_SPEC-qt5.spec
rm $1/$ORIG_SPEC-qt5.spec.new

# Not wanted for avahi:
#cp -a $1/$ORIG_SPEC.changes $1/$ORIG_SPEC-glib2.changes
#cp -a $1/$ORIG_SPEC.changes $1/$ORIG_SPEC-qt5.changes
