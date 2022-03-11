#! /bin/bash

#
# This script is supposed to be executed from the %post section. It contains all
# hacks needed to update a system which was running systemd < v210. This also
# includes systems migrating from SysV.
#
# All hacks can potentially break the admin settings since they work in /etc...
#

#
# During migration from sysvinit to systemd, we used to set the systemd default
# target to one of the 'runlevel*.target' after reading the default runlevel
# from /etc/inittab. We don't do that anymore because in most cases using the
# graphical.target target, which is the default, will do the right
# thing. Moreover the runlevel targets are considered as deprecated, so we
# convert them into "true" systemd targets instead here.
#
if target=$(readlink /etc/systemd/system/default.target); then
	target=$(basename $target)
	case "$target" in
	runlevel?.target)
		echo "Default systemd target is '$target' but use of runlevels is deprecated"
		systemctl --no-reload set-default $target
	esac
fi

#
# Migrate any symlink which may refer to the old path.
#
for f in $(find /etc/systemd/system -type l -xtype l); do
        new_target="/usr$(readlink $f)"
        [ -f "$new_target" ] && ln -s -f $new_target $f
done
