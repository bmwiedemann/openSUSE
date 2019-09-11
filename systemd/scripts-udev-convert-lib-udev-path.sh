#! /bin/bash
#
# When upgrading from systems predating systemd (SLE11, openSUSE
# 12.x), udev libexec directory was changed from /lib/udev to
# /usr/lib/udev. Some customer scripts might still rely on the old
# path, therefore try to create a symlink that preserves the old path
# (see bsc#1050152).
#
# This script is supposed to be called from the %posttrans scection of
# the udev package.
#
convert_lib_udev_path () {
	local failed=/bin/false

	# Sanity check: /usr/lib/udev must exist at that point since
	# the new udev package should have been installed.
	if ! test -d /usr/lib/udev; then
		echo >&2 "/usr/lib/udev does not exist, refusing to create"
		echo >&2 "/lib/udev compat symlink."
		return 1
	fi

	# If the symlink is missing it probably means that we're
	# upgrading and the old /lib/udev path was removed as it was
	# empty at the time the old version of udev was uninstalled.
	if ! test -e /lib/udev; then
		echo "Creating /lib/udev -> /usr/lib/udev symlink."
		ln -s /usr/lib/udev /lib/udev
		return
	fi

	# If a symlink already exists, simply assume that we already
	# did the job. IOW we're just doing a simple update of
	# systemd/udev (not upgrading).
	if test -L /lib/udev; then
		return
	fi

	# Sanity check: refuse to deal with anything but a directory.
	if ! test -d /lib/udev; then
		echo >&2 "/lib/udev is not either a directory nor a symlink !"
		echo >&2 "It won't be converted into a symlink to /usr/lib/udev."
		echo >&2 "Please create it manually."
		return 1
	fi

	# /lib/udev exists and is still a directory (probably not
	# empty otherwise it would have been removed when the old
	# version of udev was uninstalled), we try to merge its
	# content with the new location and if it fails we warn the
	# user and let him sort this out.
	shopt -s globstar
	for f in /lib/udev/**; do
		if test -d "$f"; then
			continue
		fi
		if test -e /usr/"$f"; then
			echo >&2 "Failed to migrate '$f' to /usr/lib/udev because it already exists."
			failed=/bin/true
			continue
		fi

		echo "Migrating '$f' in /usr/lib/udev"
		if ! cp -a --parents "$f" /usr; then
			echo >&2 "Failed to move '$f' in /usr/lib/udev."
			failed=/bin/true
			continue
		fi
		rm "$f"
	done
	shopt -u globstar

	if ! $failed; then
		rm -fr /lib/udev &&
		ln -s ../usr/lib/udev /lib/udev &&
		echo "The content of /lib/udev has been moved in /usr/lib/udev successfully" &&
		echo "and /lib/udev is now a symlink pointing to /usr/lib/udev." &&
		echo "Please note /lib/udev is deprecated and shouldn't be used by" &&
		echo "new scripts/applications anymore." ||
		failed=/bin/true
	fi

	if $failed; then
		echo >&2 "Converting /lib/udev into a symlink pointing to /usr/lib/udev was not"
		echo >&2 "possible due to previous error(s)."
		echo >&2 "Please fix them and then create the symlink with:"
		echo >&2 "      'ln -s ../usr/lib/udev /lib/udev'."
		return 1
	fi
}

convert_lib_udev_path
