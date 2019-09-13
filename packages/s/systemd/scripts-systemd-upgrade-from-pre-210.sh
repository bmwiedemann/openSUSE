#! /bin/bash

#
# This script is supposed to be executed from the %post section. It
# contains all hacks needed to update a system which was running
# systemd < v210. This also includes systems migrating from SysV.
#
# All hacks can potentially break the admin settings since they work
# in /etc...

# Try to read default runlevel from the old inittab if it exists. If
# it fails fallback to runlevel 3 which should still be better than
# the rescue shell.
#
# Note: /etc/inittab was part of the aaa_base package which can be
# upgraded before systemd is. Therefore this file is likely to be
# missing.
if [ ! -e /etc/systemd/system/default.target -a -e /etc/inittab ]; then
        runlevel=$(sed -n -r "s/^id:([[:digit:]]):initdefault:/\1/p" /etc/inittab)
        : ${runlevel:=3}
        echo "Initializing default.target to runlevel${runlevel}.target"
        ln -s /usr/lib/systemd/system/runlevel${runlevel}.target /etc/systemd/system/default.target
fi

# migrate any symlink which may refer to the old path
for f in $(find /etc/systemd/system -type l -xtype l); do
        new_target="/usr$(readlink $f)"
        [ -f "$new_target" ] && ln -s -f $new_target $f
done

